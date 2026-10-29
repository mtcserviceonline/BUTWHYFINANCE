const esito = document.getElementById('esito');
const etichetta = document.getElementById('cartella');
const dire = (t, classe = '') => { esito.textContent = t; esito.className = classe; };

async function aggiorna() {
  const cartella = await bwfMemoria.get('cartella');
  const modo = await bwfMemoria.modoEffettivo();
  etichetta.textContent = cartella ? `Cartella scelta: ${cartella.name}` : 'Nessuna cartella scelta';
  document.querySelector(`input[name=modo][value=${modo}]`).checked = true;
}

document.getElementById('scegli').addEventListener('click', async () => {
  try {
    const cartella = await window.showDirectoryPicker({ id: 'bwf-metriche', mode: 'readwrite' });
    await bwfMemoria.set('cartella', cartella);
    await bwfMemoria.set('modo', 'cartella');
    await aggiorna();
    dire(`Fatto: da ora salvo in "${cartella.name}".`, 'ok');
  } catch (e) {
    if (e.name !== 'AbortError') dire(`Non posso usare questa cartella: ${e.message}`, 'err');
  }
});

document.getElementById('verifica').addEventListener('click', async () => {
  const cartella = await bwfMemoria.get('cartella');
  if (!cartella) { dire('Scegli prima una cartella.', 'err'); return; }
  try {
    const ok = await bwfMemoria.permesso(cartella, true);
    dire(ok ? 'Permesso di scrittura attivo.' : 'Permesso negato: riscegli la cartella.', ok ? 'ok' : 'err');
  } catch (e) { dire(`Controllo non riuscito: ${e.message}`, 'err'); }
});

for (const r of document.querySelectorAll('input[name=modo]')) {
  r.addEventListener('change', async () => {
    if (r.value === 'cartella' && !(await bwfMemoria.get('cartella'))) {
      dire('Scegli prima una cartella con "Scegli cartella…".', 'err');
      await aggiorna();
      return;
    }
    await bwfMemoria.set('modo', r.value);
    await aggiorna();
    dire('Impostazione salvata.', 'ok');
  });
}
aggiorna();
