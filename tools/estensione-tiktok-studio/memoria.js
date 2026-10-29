// Funzioni condivise da popup, opzioni e pagina di salvataggio: impostazioni in IndexedDB
// (le cartelle scelte con il selettore del browser si possono conservare solo lì).
(() => {
  const DB = 'bwf', ARCHIVIO = 'impostazioni';
  const apri = () => new Promise((ok, ko) => {
    const r = indexedDB.open(DB, 1);
    r.onupgradeneeded = () => r.result.createObjectStore(ARCHIVIO);
    r.onsuccess = () => ok(r.result);
    r.onerror = () => ko(r.error);
  });
  async function get(chiave) {
    const db = await apri();
    return new Promise((ok, ko) => { const r = db.transaction(ARCHIVIO).objectStore(ARCHIVIO).get(chiave); r.onsuccess = () => ok(r.result); r.onerror = () => ko(r.error); });
  }
  async function set(chiave, valore) {
    const db = await apri();
    return new Promise((ok, ko) => { const t = db.transaction(ARCHIVIO, 'readwrite'); t.objectStore(ARCHIVIO).put(valore, chiave); t.oncomplete = () => ok(); t.onerror = () => ko(t.error); });
  }
  // Se richiedi=true va chiamata subito dopo un clic dell'utente (serve il gesto) e può mostrare un avviso del browser.
  async function permesso(cartella, richiedi) {
    if (!cartella) return false;
    const opz = { mode: 'readwrite' };
    if ((await cartella.queryPermission(opz)) === 'granted') return true;
    if (!richiedi) return false;
    return (await cartella.requestPermission(opz)) === 'granted';
  }
  async function scrivi(cartella, nome, testo) {
    const file = await cartella.getFileHandle(nome, { create: true });
    const w = await file.createWritable();
    await w.write(testo);
    await w.close();
  }
  // 'cartella' = salva sempre nella cartella scelta; 'chiedi' = finestra "Salva con nome" ogni volta.
  async function modoEffettivo() {
    const modo = await get('modo');
    const cartella = await get('cartella');
    return modo === 'chiedi' || !cartella ? 'chiedi' : 'cartella';
  }
  function nomeFile(dati) {
    const d = new Date(), p = (n) => String(n).padStart(2, '0');
    const stampa = `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}`;
    return `tiktok-studio_${dati.video_id || 'post'}_${stampa}.json`;
  }
  function riepilogo(d) {
    const p = d.schede.panoramica || {}, s = d.schede.spettatori || {};
    const n = (o) => (o ? Object.keys(o).length : 0);
    return `Metriche lette: ${n(p.metriche)} · fonti di traffico: ${n(p.fonti_traffico)} · fasce di età: ${n(s.eta)}\n` +
      `Risposte di rete salvate: ${d.risposte_rete.length} · curve numeriche trovate: ${d.indizi.curve_numeriche.length}`;
  }
  window.bwfMemoria = { get, set, permesso, scrivi, modoEffettivo, nomeFile, riepilogo };
})();
