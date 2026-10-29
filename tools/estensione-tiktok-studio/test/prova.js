// Collaudo: carica l'estensione in Chromium, apre la pagina finta, esegue l'esportazione come il popup.
// Uso: node prova.js   (richiede playwright, già installato nell'ambiente cloud)
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), os = require('os'), path = require('path'), crypto = require('crypto');

const estensione = path.resolve(__dirname, '..');
const base = process.env.BWF_TEST_DIR || os.tmpdir();   // cartella per estensione di prova, profilo e download
const tmp = fs.mkdtempSync(path.join(base, 'e-'));
for (const f of ['hook.js', 'content.js', 'memoria.js', 'popup.html', 'popup.js', 'opzioni.html', 'opzioni.js', 'salva.html', 'salva.js']) fs.copyFileSync(path.join(estensione, f), path.join(tmp, f));
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
    return { dati: await window.bwfEsporta(t.id), tabId: t.id };
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
  ];
  let ko = 0;
  for (const [n, ok] of verifiche) { console.log(ok ? 'OK ' : 'KO ', n); if (!ok) ko++; }
  // ---- Scenario A: cartella fissa (qui una cartella OPFS al posto di quella scelta con il selettore) ----
  const A = await popup.evaluate(async (tabId) => {
    const radice = await navigator.storage.getDirectory();
    const cartella = await radice.getDirectoryHandle('cartella-prova', { create: true });
    await bwfMemoria.set('cartella', cartella); await bwfMemoria.set('modo', 'cartella');
    const veri = chrome.tabs.query;
    chrome.tabs.query = async () => [{ id: tabId, url: 'https://www.tiktok.com/tiktokstudio/analytics/7123456789012345678' }];
    document.getElementById('salva').click();
    for (let i = 0; i < 60 && !/Salvato|Non riesco|Apri prima|non risponde/.test(document.getElementById('stato').textContent); i++) await new Promise((r) => setTimeout(r, 500));
    chrome.tabs.query = veri;
    await mostraDestinazione();
    const testo = document.getElementById('stato').textContent;
    const nomi = []; for await (const [n] of cartella.entries()) nomi.push(n);
    let contenuto = null;
    if (nomi[0]) contenuto = JSON.parse(await (await (await cartella.getFileHandle(nomi[0])).getFile()).text());
    return { testo, nomi, schema: contenuto && contenuto.schema, righe: document.getElementById('dove').textContent };
  }, risultato.tabId);
  console.log('A) stato:', A.testo.split('\n')[0], '| destinazione:', A.righe);
  const verificheNuove = [
    ['A: file scritto nella cartella scelta', A.nomi.length === 1 && /^tiktok-studio_7123456789012345678_\d{8}-\d{4}\.json$/.test(A.nomi[0])],
    ['A: contenuto valido', A.schema === 'bwf-tiktok-studio-v1'],
    ['A: popup mostra la cartella', /cartella-prova/.test(A.righe)],
  ];

  // ---- Scenario B: "chiedi ogni volta" -> si apre salva.html con il pulsante ----
  await popup.evaluate(async () => { await bwfMemoria.set('modo', 'chiedi'); });
  const nuovaScheda = ctx.waitForEvent('page');
  await popup.evaluate(async (tabId) => {
    const veri = chrome.tabs.query;
    chrome.tabs.query = async () => [{ id: tabId, url: 'https://www.tiktok.com/tiktokstudio/analytics/7123456789012345678' }];
    document.getElementById('salva').click();
    chrome.tabs.query = veri;
  }, risultato.tabId);
  const salva = await nuovaScheda;
  await salva.waitForLoadState();
  await salva.waitForSelector('#salva:not([hidden])', { timeout: 60000 });
  const B = await salva.evaluate(async () => {
    const radice = await navigator.storage.getDirectory();
    window.showSaveFilePicker = async (o) => radice.getFileHandle('scelto-' + o.suggestedName, { create: true });   // il selettore vero non si automatizza
    document.getElementById('salva').click();
    for (let i = 0; i < 20 && !/Salvato/.test(document.getElementById('esito').textContent); i++) await new Promise((r) => setTimeout(r, 250));
    const nomi = []; for await (const [n] of radice.entries()) nomi.push(n);
    const f = nomi.find((n) => n.startsWith('scelto-'));
    const j = f ? JSON.parse(await (await (await radice.getFileHandle(f)).getFile()).text()) : null;
    return { esito: document.getElementById('esito').textContent, riepilogo: document.getElementById('riepilogo').textContent, schema: j && j.schema };
  });
  console.log('B) esito:', B.esito);
  verificheNuove.push(['B: si apre la scheda con il riepilogo', /Metriche lette: 5/.test(B.riepilogo)]);
  verificheNuove.push(['B: file scritto dove scelto', /Salvato: scelto-tiktok-studio_/.test(B.esito) && B.schema === 'bwf-tiktok-studio-v1']);

  // ---- Scenario C: pagina opzioni, scelta della cartella ----
  const opz = await ctx.newPage();
  await opz.goto(`chrome-extension://${idEst}/opzioni.html`);
  const C = await opz.evaluate(async () => {
    const radice = await navigator.storage.getDirectory();
    window.showDirectoryPicker = async () => radice.getDirectoryHandle('cartella-opzioni', { create: true });
    document.getElementById('scegli').click();
    for (let i = 0; i < 20 && !/Fatto/.test(document.getElementById('esito').textContent); i++) await new Promise((r) => setTimeout(r, 250));
    document.getElementById('verifica').click();
    for (let i = 0; i < 20 && !/Permesso/.test(document.getElementById('esito').textContent); i++) await new Promise((r) => setTimeout(r, 250));
    return { etichetta: document.getElementById('cartella').textContent, esito: document.getElementById('esito').textContent,
      modo: (await bwfMemoria.modoEffettivo()), nome: (await bwfMemoria.get('cartella')).name };
  });
  verificheNuove.push(['C: cartella scelta e memorizzata', C.nome === 'cartella-opzioni' && C.modo === 'cartella' && /cartella-opzioni/.test(C.etichetta)]);
  verificheNuove.push(['C: verifica permesso', /Permesso di scrittura attivo/.test(C.esito)]);
  for (const [n, ok] of verificheNuove) { console.log(ok ? 'OK ' : 'KO ', n); if (!ok) ko++; }

  const scaricato = fs.existsSync(dl) ? fs.readdirSync(dl) : [];
  console.log('Cartella download playwright:', scaricato);
  fs.writeFileSync(path.join(base, 'risultato.json'), JSON.stringify(d, null, 2));
  console.log('Esito:', ko === 0 ? 'TUTTO OK' : `${ko} verifiche fallite`);
  await ctx.close(); server.close();
  process.exit(ko ? 1 : 0);
})().catch((e) => { console.error('ERRORE', e); process.exit(2); });
