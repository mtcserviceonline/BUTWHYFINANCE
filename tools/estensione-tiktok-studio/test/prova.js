// Collaudo: carica l'estensione in Chromium, apre la pagina finta, esegue l'esportazione come il popup.
// Uso: node prova.js   (richiede playwright, già installato nell'ambiente cloud)
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), os = require('os'), path = require('path'), crypto = require('crypto');

const estensione = path.resolve(__dirname, '..');
const base = process.env.BWF_TEST_DIR || os.tmpdir();   // cartella per estensione di prova, profilo e download
const tmp = fs.mkdtempSync(path.join(base, 'e-'));
for (const f of ['hook.js', 'content.js', 'popup.html', 'popup.js']) fs.copyFileSync(path.join(estensione, f), path.join(tmp, f));
fs.cpSync(path.join(estensione, 'icons'), path.join(tmp, 'icons'), { recursive: true });
const man = JSON.parse(fs.readFileSync(path.join(estensione, 'manifest.json')));
man.content_scripts.forEach((c) => { c.matches = ['http://localhost/*']; });   // solo per il collaudo
man.permissions.push('tabs');   // solo per il collaudo: serve a leggere l'URL delle schede
fs.writeFileSync(path.join(tmp, 'manifest.json'), JSON.stringify(man));
const extDir = fs.realpathSync(tmp);

const curva = Array.from({ length: 34 }, (_, i) => Math.round(100 * Math.exp(-i / 6) + 4));
const server = http.createServer((req, res) => {
  const u = req.url.split('?')[0];
  const json = (o) => { res.setHeader('content-type', 'application/json'); res.end(JSON.stringify(o)); };
  if (u.startsWith('/tiktokstudio/')) { res.setHeader('content-type', 'text/html'); return res.end(fs.readFileSync(path.join(__dirname, 'pagina-finta.html'))); }
  if (u === '/api/overview') return json({ data: { retention: { curve: curva }, views: 237 } });
  if (u === '/api/hourly') return json({ data: { points: [0, 94, 32, 73, 38, 2, 0, 0, 1, 0, 0, 0, 3] } });
  if (u === '/api/audience') return json({ data: { gender: { male: 78, female: 22 } } });
  if (u === '/api/likes') return json({ data: { like_curve: Array.from({ length: 34 }, (_, i) => (i === 2 ? 30 : i === 28 ? 12 : 1)) } });
  res.statusCode = 404; res.end('no');
});

(async () => {
  await new Promise((r) => server.listen(0, r));
  const porta = server.address().port;
  const idEst = (() => { const h = crypto.createHash('sha256').update(extDir).digest('hex').slice(0, 32);
    return [...h].map((c) => String.fromCharCode('a'.charCodeAt(0) + parseInt(c, 16))).join(''); })();
  const dl = fs.mkdtempSync(path.join(base, 'd-'));
  const ctx = await chromium.launchPersistentContext(fs.mkdtempSync(path.join(base, 'p-')), {
    headless: false, acceptDownloads: true, downloadsPath: dl,
    args: ['--headless=new', `--disable-extensions-except=${extDir}`, `--load-extension=${extDir}`, '--no-sandbox'],
  });
  const pagina = await ctx.newPage();
  await pagina.goto(`http://localhost:${porta}/tiktokstudio/analytics/7123456789012345678/overview`);
  await pagina.waitForSelector('text=Visualizzazioni video');
  const popup = await ctx.newPage();
  await popup.goto(`chrome-extension://${idEst}/popup.html`);
  const risultato = await popup.evaluate(async () => {
    const tabs = await chrome.tabs.query({});
    const t = tabs.find((x) => /tiktokstudio/.test(x.url || ''));
    const dati = await window.bwfEsporta(t.id);
    const file = await window.bwfSalvaFile(dati);
    return { dati, file };
  });
  const d = risultato.dati;
  const p = d.schede.panoramica, s = d.schede.spettatori, c = d.schede.coinvolgimento;
  const verifiche = [
    ['video_id', d.video_id === '7123456789012345678'],
    ['titolo post', (p.titolo_post || '').startsWith('Se ti bevi un caffè')],
    ['data pubblicazione', p.pubblicato === '28/10/2026'],
    ['contatori', p.contatori && p.contatori.visualizzazioni.numero === 237 && p.contatori.mi_piace.numero === 10],
    ['visualizzazioni', p.metriche.visualizzazioni_video.numero === 237],
    ['tempo totale (s)', p.metriche.tempo_riproduzione_totale.numero === 2145],
    ['tempo medio (s)', p.metriche.tempo_medio_visualizzazione.numero === 8.51],
    ['completo %', p.metriche.guarda_video_completo.numero === 4.8],
    ['nuovi follower', p.metriche.nuovi_follower.numero === 3],
    ['picco abbandono', p.retention_picco_abbandono === '0:01'],
    ['traffico Per te', p.fonti_traffico && p.fonti_traffico['Per te'].numero === 94.8],
    ['età 25-34', s.eta && s.eta['25-34'].numero === 43],
    ['sesso uomini', s.sesso && s.sesso['Uomini'].numero === 78],
    ['Italia', s.posizioni && s.posizioni['Italia'].numero === 96.4],
    ['picco mi piace', c.mi_piace_picco === '0:02'],
    ['hook attivo', d.hook_attivo === true],
    ['risposte >= 4', d.risposte_rete.length >= 4],
    ['XHR registrata', d.risposte_rete.some((r) => /api\/hourly/.test(r.url))],
    ['token redatti', d.risposte_rete.every((r) => !/SEGRETO|ZZZ|=123/.test(r.url))],
    ['curve trovate', d.indizi.curve_numeriche.length >= 2],
    ['file scaricato', !!risultato.file.id],
  ];
  let ko = 0;
  for (const [n, ok] of verifiche) { console.log(ok ? 'OK ' : 'KO ', n); if (!ok) ko++; }
  const scaricato = fs.existsSync(dl) ? fs.readdirSync(dl) : [];
  console.log('Cartella download playwright:', scaricato);
  fs.writeFileSync(path.join(base, 'risultato.json'), JSON.stringify(d, null, 2));
  console.log('Esito:', ko === 0 ? 'TUTTO OK' : `${ko} verifiche fallite`);
  await ctx.close(); server.close();
  process.exit(ko ? 1 : 0);
})().catch((e) => { console.error('ERRORE', e); process.exit(2); });
