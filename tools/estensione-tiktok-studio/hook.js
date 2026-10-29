// Gira nel contesto della pagina, prima del resto. Si limita a ricordare le risposte
// JSON/testo che la pagina di TikTok Studio scarica per conto suo. Non fa richieste proprie.
(() => {
  if (window.__bwfHook) return;
  window.__bwfHook = true;

  const MAX_CORPO = 1500000;   // caratteri per risposta
  const MAX_RISPOSTE = 300;
  const registro = [];

  const paginaStudio = () => /tiktokstudio|creator-center|analytics|studio/i.test(location.href);
  const SENSIBILE = /(token|sign|bogus|verify|cookie|session|device|odin|uid|user_id|sec_uid|ttwid|fp)/i;

  const pulisciUrl = (u) => {
    try {
      const url = new URL(u, location.href);
      for (const k of [...url.searchParams.keys()]) {
        if (SENSIBILE.test(k)) url.searchParams.set(k, 'REDATTO');
      }
      return url.toString();
    } catch (_) {
      return String(u).slice(0, 500);
    }
  };

  const registra = (url, metodo, stato, tipo, testo) => {
    if (!paginaStudio() || typeof testo !== 'string' || !testo.length) return;
    const t = testo.trim();
    const sembraJson = t[0] === '{' || t[0] === '[';
    if (!sembraJson && !/json/i.test(tipo || '')) return;
    const rec = { url: pulisciUrl(url), metodo, stato, tipo, ricevuta_il: new Date().toISOString(), lunghezza: t.length };
    if (t.length > MAX_CORPO) {
      rec.troncata = true;
      rec.corpo_testo = t.slice(0, 2000);
    } else {
      try { rec.corpo = JSON.parse(t); } catch (_) { rec.corpo_testo = t.slice(0, 20000); }
    }
    if (registro.length >= MAX_RISPOSTE) registro.shift();
    registro.push(rec);
  };

  const fetchOriginale = window.fetch;
  window.fetch = function (...args) {
    const risultato = fetchOriginale.apply(this, args);
    try {
      const req = args[0];
      const url = typeof req === 'string' ? req : (req && req.url) || String(req);
      const metodo = (args[1] && args[1].method) || (req && req.method) || 'GET';
      risultato.then((res) => {
        try {
          const copia = res.clone();
          const tipo = copia.headers.get('content-type') || '';
          copia.text().then((txt) => registra(url, metodo, res.status, tipo, txt)).catch(() => {});
        } catch (_) {}
      }).catch(() => {});
    } catch (_) {}
    return risultato;
  };

  const apri = XMLHttpRequest.prototype.open;
  const invia = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function (metodo, url) {
    this.__bwf = { metodo, url };
    return apri.apply(this, arguments);
  };
  XMLHttpRequest.prototype.send = function () {
    this.addEventListener('loadend', () => {
      try {
        if (this.responseType === '' || this.responseType === 'text') {
          registra(this.__bwf && this.__bwf.url, (this.__bwf && this.__bwf.metodo) || 'GET', this.status,
            this.getResponseHeader('content-type'), this.responseText);
        }
      } catch (_) {}
    });
    return invia.apply(this, arguments);
  };

  window.addEventListener('message', (e) => {
    if (e.source !== window || !e.data || e.data.bwf !== 'REQ') return;
    window.postMessage({ bwf: 'RES', id: e.data.id, json: JSON.stringify(registro) }, '*');
  });
})();
