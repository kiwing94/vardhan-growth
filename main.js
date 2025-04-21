function suggestMetaphor() {
  const ideas = ["Memories drift like clouds.", "The heart is a flame.", "Dreams grow from silence."];
  document.getElementById('metaphorBox').innerText = ideas[Math.floor(Math.random() * ideas.length)];
}
function savePoem() {
  const text = document.getElementById('poemInput').value;
  fetch('/save_poem', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username: 'user', text})
  }).then(res => res.json()).then(data => alert("✅ Poem saved!"));
}
function translateText() {
  const text = document.getElementById('translateInput').value;
  const source = document.getElementById('sourceLang').value;
  const target = document.getElementById('targetLang').value;
  fetch('/translate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({text, source, target})
  }).then(res => res.json()).then(data => {
    if (data.error) {
      document.getElementById('translatedOutput').innerText = "❌ " + data.error;
    } else {
      document.getElementById('translatedOutput').innerText = data.data.translations[0].translatedText;
    }
  });
}
