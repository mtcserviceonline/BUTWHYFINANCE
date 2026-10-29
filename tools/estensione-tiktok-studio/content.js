// Gira nel mondo isolato dell'estensione. Quando il popup lo chiede, apre una dopo l'altra le tre
// schede del post (Panoramica, Spettatori, Coinvolgimento), legge il testo visibile e raccoglie le
// risposte registrate da hook.js. Non invia nulla fuori dal browser.
(() => {
  if (window.__bwfContent) return;
  window.__bwfContent = true;

  const SCHEDE = ['Panoramica', 'Spettatori', 'Coinvolgimento'];
  const pausa = (ms) => new Promise((r) => setTimeout(r, ms));

  const visibile = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };

  function trovaScheda(nome) {
    const cand = [...document.querySelectorAll('[role="tab"], a, button, li, div, span')]
      .filter((e) => e.textContent.trim() === nome && visibile(e));
    if (!cand.length) return null;
    const inAlto = cand.filter((e) => e.getBoundingClientRect().top < 200);
    const gruppo = inAlto.length ? inAlto : cand;
    return gruppo[gruppo.length - 1];   // l'elemento più interno
  }

  function clicca(el) {
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
  }

  async function aspettaStabile(timeout = 6000) {
    const t0 = Date.now();
    let prima = document.body.innerText.length;
    let stabile = 0;
    while (Date.now() - t0 < timeout) {
      await pausa(300);
      const ora = document.body.innerText.length;
      if (ora === prima) { if (++stabile >= 3) return; } else { stabile = 0; prima = ora; }
    }
  }

  async function scorri() {
    const els = [document.scrollingElement, ...document.querySelectorAll('main, [class*="scroll"], [class*="Scroll"]')];
    for (const e of els) { try { if (e) e.scrollTop = e.scrollHeight; } catch (_) {} }
    await pausa(500);
    for (const e of els) { try { if (e) e.scrollTop = 0; } catch (_) {} }
    await pausa(300);
  }

  // ---------- lettura del testo ----------
  const righe = (testo) => testo.split('\n').map((r) => r.trim()).filter(Boolean);

  function numero(testo) {
    if (testo == null) return null;
    const s = String(testo).trim();
    const hms = s.match(/^(?:(\d+)h:?)?\s*(?:(\d+)m:?)?\s*(?:(\d+(?:[.,]\d+)?)s)?$/i);
    if (hms && /[hms]/i.test(s)) {
      return (+hms[1] || 0) * 3600 + (+hms[2] || 0) * 60 + (parseFloat((hms[3] || '0').replace(',', '.')) || 0);
    }
    const m = s.match(/^[<>]?\s*(-?[\d.,]+)\s*([KkMm])?\s*%?$/);
    if (!m) return null;
    let n = parseFloat(m[1].replace(/\.(?=\d{3}(\D|$))/g, '').replace(',', '.'));
    if (m[2]) n *= /k/i.test(m[2]) ? 1e3 : 1e6;
    return Number.isNaN(n) ? null : n;
  }
  const voce = (testo) => ({ testo, numero: numero(testo) });
  const eNumero = (r) => /^[<>]?\s*-?[\d.,]+\s*[KkMm]?\s*%?$/.test(r);

  const ETICHETTE = {
    visualizzazioni_video: 'Visualizzazioni video',
    tempo_riproduzione_totale: 'Tempo di riproduzione totale',
    tempo_medio_visualizzazione: 'Tempo medio di visualizzazione',
    guarda_video_completo: 'Guarda il video completo',
    nuovi_follower: 'Nuovi follower',
  };
  const TITOLI = ['Spettatori totali', 'Tipi di spettatori', 'Età', 'Sesso', 'Posizioni', 'Fonti di traffico', 'Termini di ricerca', 'Tasso di mantenimento', 'Mi piace', 'Le parole più usate nei commenti'];

  function coppie(rr, da, fino) {
    const out = {};
    for (let i = da; i < Math.min(fino, rr.length - 1); i++) {
      if (eNumero(rr[i + 1]) && !eNumero(rr[i]) && !TITOLI.includes(rr[i]) && rr[i].length < 60) out[rr[i]] = voce(rr[i + 1]);
    }
    return out;
  }
  function sezione(rr, titolo) {
    const i = rr.indexOf(titolo);
    if (i < 0) return null;
    let fine = rr.length;
    for (let j = i + 1; j < rr.length; j++) if (TITOLI.includes(rr[j])) { fine = j; break; }
    return coppie(rr, i + 1, fine);
  }

  function leggiPanoramica(testo) {
    const rr = righe(testo);
    const res = {};
    const iPub = rr.findIndex((r) => /^Pubblicato il giorno/i.test(r));
    if (iPub >= 0) {
      res.titolo_post = rr[iPub - 1] || null;
      res.pubblicato = (rr[iPub].match(/(\d{1,2}\/\d{1,2}\/\d{4})/) || [])[1] || rr[iPub];
      const num = [];
      for (let k = iPub + 1; k < rr.length && num.length < 5; k++) {
        if (Object.values(ETICHETTE).includes(rr[k])) break;
        if (eNumero(rr[k])) num.push(voce(rr[k]));
      }
      if (num.length === 5) {
        res.contatori = { visualizzazioni: num[0], mi_piace: num[1], commenti: num[2], condivisioni: num[3], salvataggi: num[4], nota: "ordine presunto dalle icone: play, cuore, commenti, condividi, salvataggi" };
      } else if (num.length) res.contatori_grezzi = num;
    }
    res.metriche = {};
    for (const [chiave, et] of Object.entries(ETICHETTE)) {
      const i = rr.indexOf(et);
      if (i >= 0 && rr[i + 1] != null) res.metriche[chiave] = voce(rr[i + 1]);
    }
    const ret = testo.match(/smesso di vedere il video in questo momento:\s*(\d+:\d+)/);
    res.retention_picco_abbandono = ret ? ret[1] : null;
    res.fonti_traffico = sezione(rr, 'Fonti di traffico');
    return res;
  }
  function leggiSpettatori(testo) {
    const rr = righe(testo);
    return { sesso: sezione(rr, 'Sesso'), eta: sezione(rr, 'Età'), posizioni: sezione(rr, 'Posizioni'),
      in_elaborazione: /in fase di elaborazione/i.test(testo) };
  }
  function leggiCoinvolgimento(testo) {
    const m = testo.match(/ha messo Mi piace al tuo video in questo momento:\s*(\d+:\d+)/);
    return { mi_piace_picco: m ? m[1] : null, in_elaborazione: /in fase di elaborazione/i.test(testo) };
  }
  const LETTORI = { panoramica: leggiPanoramica, spettatori: leggiSpettatori, coinvolgimento: leggiCoinvolgimento };

  // ---------- risposte di rete registrate da hook.js ----------
  function chiediRisposte() {
    return new Promise((res) => {
      const id = Math.random().toString(36).slice(2);
      const gestore = (e) => {
        if (e.source !== window || !e.data || e.data.bwf !== 'RES' || e.data.id !== id) return;
        window.removeEventListener('message', gestore);
        try { res(JSON.parse(e.data.json)); } catch (_) { res([]); }
      };
      window.addEventListener('message', gestore);
      window.postMessage({ bwf: 'REQ', id }, '*');
      setTimeout(() => { window.removeEventListener('message', gestore); res(null); }, 3000);
    });
  }

  function cercaCurve(risposte) {
    const trovate = [];
    const visita = (nodo, percorso, i, prof) => {
      if (prof > 9 || nodo == null || trovate.length > 60) return;
      if (Array.isArray(nodo)) {
        if (nodo.length >= 10 && nodo.every((x) => typeof x === 'number')) {
          trovate.push({ risposta: i, percorso, lunghezza: nodo.length, primi_valori: nodo.slice(0, 12) });
          return;
        }
        nodo.slice(0, 200).forEach((x, k) => visita(x, `${percorso}[${k}]`, i, prof + 1));
      } else if (typeof nodo === 'object') {
        for (const k of Object.keys(nodo)) visita(nodo[k], percorso ? `${percorso}.${k}` : k, i, prof + 1);
      }
    };
    (risposte || []).forEach((r, i) => visita(r.corpo, '', i, 0));
    return trovate;
  }

  async function esporta() {
    const out = {
      schema: 'bwf-tiktok-studio-v1',
      estratto_il: new Date().toISOString(),
      url: location.href,
      titolo_pagina: document.title,
      video_id: (location.href.match(/(\d{15,})/) || [])[1] || null,
      schede: {},
    };
    for (const nome of SCHEDE) {
      const chiave = nome.toLowerCase();
      const el = trovaScheda(nome);
      if (!el) { out.schede[chiave] = { errore: 'scheda non trovata' }; continue; }
      clicca(el);
      await aspettaStabile();
      await scorri();
      const testo = document.body.innerText;
      out.schede[chiave] = { ...LETTORI[chiave](testo), testo_grezzo: testo.slice(0, 40000) };
    }
    const iniziale = trovaScheda('Panoramica');
    if (iniziale) clicca(iniziale);
    await pausa(300);
    const risposte = await chiediRisposte();
    out.hook_attivo = risposte !== null;
    out.risposte_rete = risposte || [];
    out.indizi = { curve_numeriche: cercaCurve(out.risposte_rete) };
    return out;
  }

  chrome.runtime.onMessage.addListener((msg, _mittente, rispondi) => {
    if (msg && msg.tipo === 'ESPORTA') {
      esporta().then((dati) => rispondi({ ok: true, dati })).catch((e) => rispondi({ ok: false, errore: String(e) }));
      return true;
    }
  });
})();
