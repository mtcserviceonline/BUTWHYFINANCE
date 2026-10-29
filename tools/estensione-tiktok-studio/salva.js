const riepilogo = document.getElementById('riepilogo');
const bottone = document.getElementById('salva');
const esito = document.getElementById('esito');

(async () => {
  const ultimo = await bwfMemoria.get('ultimo_export');
  if (!ultimo) {
    riepilogo.textContent = 'Non c\'è niente da salvare. Apri i dettagli di un post in TikTok Studio e clicca sull\'icona dell\'estensione.';
    return;
  }
  riepilogo.textContent = `${ultimo.nome}\n${bwfMemoria.riepilogo(ultimo.dati)}`;
  bottone.hidden = false;
  bottone.addEventListener('click', async () => {
    try {
      const file = await window.showSaveFilePicker({
        suggestedName: ultimo.nome,
        types: [{ description: 'File JSON', accept: { 'application/json': ['.json'] } }],
      });
      const w = await file.createWritable();
      await w.write(JSON.stringify(ultimo.dati, null, 2));
      await w.close();
      esito.textContent = `Salvato: ${file.name}`;
      esito.className = 'ok';
    } catch (e) {
      if (e.name === 'AbortError') return;
      esito.textContent = `Non sono riuscito a salvare: ${e.message}`;
      esito.className = 'err';
    }
  });
})();
