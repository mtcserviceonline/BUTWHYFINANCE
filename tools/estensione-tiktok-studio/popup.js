const stato = document.getElementById('stato');
const dove = document.getElementById('dove');
const bottone = document.getElementById('salva');
const dire = (t, classe = '') => { stato.textContent = t; stato.className = classe; };

async function esporta(tabId) {
  const r = await chrome.tabs.sendMessage(tabId, { tipo: 'ESPORTA' });
  if (!r || !r.ok) throw new Error((r && r.errore) || 'nessuna risposta dalla pagina');
  return r.dati;
}

async function mostraDestinazione() {
  const modo = await bwfMemoria.modoEffettivo();
  const cartella = await bwfMemoria.get('cartella');
  dove.textContent = modo === 'cartella' ? `Salvo in: ${cartella.name} · ` : 'Ti chiedo dove salvare ogni volta · ';
  const a = document.createElement('a');
  a.textContent = modo === 'cartella' ? 'cambia cartella' : 'scegli una cartella fissa';
  a.addEventListener('click', () => chrome.runtime.openOptionsPage());
  dove.appendChild(a);
}

// "Chiedi ogni volta": i dati passano alla scheda salva.html, dove la finestra "Salva con nome" resta aperta.
async function chiediDove(dati, nome) {
  await bwfMemoria.set('ultimo_export', { dati, nome });
  await chrome.tabs.create({ url: chrome.runtime.getURL('salva.html') });
}

async function clic() {
  bottone.disabled = true;
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab || !/^https:\/\/www\.tiktok\.com\//.test(tab.url || '')) {
      throw new Error('Apri prima i dettagli di un post in TikTok Studio.');
    }
    const modo = await bwfMemoria.modoEffettivo();
    let cartella = null;
    if (modo === 'cartella') {
      cartella = await bwfMemoria.get('cartella');
      // Subito, mentre vale il clic: dopo qualche secondo il browser non permette più di chiedere il permesso.
      let ok = false;
      try { ok = await bwfMemoria.permesso(cartella, true); } catch (_) {}
      if (!ok) {
        dire('Il browser non ha dato il permesso di scrivere nella cartella. Ti chiederò dove salvare questa volta.', 'err');
        cartella = null;
      }
    }
    dire('Leggo le tre schede… (qualche secondo, non cambiare pagina)');
    let dati;
    try { dati = await esporta(tab.id); }
    catch (e) { throw new Error('La pagina non risponde. Ricarica la pagina (F5) e riprova.\n(' + e.message + ')'); }
    const nome = bwfMemoria.nomeFile(dati);
    let testo = bwfMemoria.riepilogo(dati);
    if (!dati.hook_attivo || dati.risposte_rete.length === 0) {
      testo += '\n\nNessuna risposta di rete registrata: ricarica la pagina del post (F5) e riclicca, così le registro dall\'inizio.';
    }
    if (cartella) {
      try {
        await bwfMemoria.scrivi(cartella, nome, JSON.stringify(dati, null, 2));
        dire(`Salvato: ${cartella.name}/${nome}\n${testo}`, 'ok');
        return;
      } catch (e) {
        testo = `Non riesco a scrivere in "${cartella.name}" (${e.name}). Scegli dove salvare nella scheda che si apre.\n` + testo;
      }
    }
    await chiediDove(dati, nome);
    dire(`Letto.\n${testo}\n\nSi è aperta una scheda: scegli lì dove salvare il file.`, 'ok');
  } catch (e) {
    dire(e.message, 'err');
  } finally {
    bottone.disabled = false;
  }
}

bottone.addEventListener('click', clic);
mostraDestinazione();
window.bwfEsporta = esporta;        // per i test
window.bwfChiediDove = chiediDove;  // per i test
