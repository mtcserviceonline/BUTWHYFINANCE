const stato = document.getElementById('stato');
const bottone = document.getElementById('salva');
const dire = (t, classe = '') => { stato.textContent = t; stato.className = classe; };

async function esporta(tabId) {
  const r = await chrome.tabs.sendMessage(tabId, { tipo: 'ESPORTA' });
  if (!r || !r.ok) throw new Error((r && r.errore) || 'nessuna risposta dalla pagina');
  return r.dati;
}

function riepilogo(d) {
  const p = d.schede.panoramica || {};
  const m = p.metriche ? Object.keys(p.metriche).length : 0;
  const tr = p.fonti_traffico ? Object.keys(p.fonti_traffico).length : 0;
  const s = d.schede.spettatori || {};
  const eta = s.eta ? Object.keys(s.eta).length : 0;
  return `Metriche lette: ${m} · fonti di traffico: ${tr} · fasce di età: ${eta}\n` +
    `Risposte di rete salvate: ${d.risposte_rete.length} · curve numeriche trovate: ${d.indizi.curve_numeriche.length}`;
}

async function salvaFile(dati) {
  const data = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  const stampa = `${data.getFullYear()}${pad(data.getMonth() + 1)}${pad(data.getDate())}-${pad(data.getHours())}${pad(data.getMinutes())}`;
  const nome = `BWF-metriche/tiktok-studio_${dati.video_id || 'post'}_${stampa}.json`;
  const url = URL.createObjectURL(new Blob([JSON.stringify(dati, null, 2)], { type: 'application/json' }));
  const id = await chrome.downloads.download({ url, filename: nome, saveAs: false, conflictAction: 'uniquify' });
  setTimeout(() => URL.revokeObjectURL(url), 60000);
  return { id, nome };
}

async function clic() {
  bottone.disabled = true;
  dire('Leggo le tre schede… (qualche secondo, non cambiare pagina)');
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab || !/^https:\/\/www\.tiktok\.com\//.test(tab.url || '')) {
      throw new Error('Apri prima i dettagli di un post in TikTok Studio.');
    }
    let dati;
    try { dati = await esporta(tab.id); }
    catch (e) { throw new Error('La pagina non risponde. Ricarica la pagina (F5) e riprova.\n(' + e.message + ')'); }
    const file = await salvaFile(dati);
    let testo = `Salvato: ${file.nome}\n${riepilogo(dati)}`;
    if (!dati.hook_attivo || dati.risposte_rete.length === 0) {
      testo += '\n\nNessuna risposta di rete registrata: ricarica la pagina del post (F5) e riclicca, così le registro dall\'inizio.';
    }
    dire(testo, 'ok');
  } catch (e) {
    dire(e.message, 'err');
  } finally {
    bottone.disabled = false;
  }
}

bottone.addEventListener('click', clic);
window.bwfEsporta = esporta;      // per i test
window.bwfSalvaFile = salvaFile;  // per i test
