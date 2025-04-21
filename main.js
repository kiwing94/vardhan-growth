function suggestMetaphor() {
  const ideas = [
    "یادیں بارش کی بوندوں کی مانند ٹپکتی ہیں۔",
    "دل ایک بند سمندر ہے۔",
    "خیال ایک پرواز کرتا پرندہ ہے۔"
  ];
  document.getElementById('metaphorBox').innerText = ideas[Math.floor(Math.random() * ideas.length)];
}

function savePoem() {
  const text = document.getElementById('poemInput').value;
  fetch('/save_poem', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username: 'user', text})
  })
  .then(res => res.json())
  .then(data => alert("✅ نظم محفوظ ہو گئی!"));
}

function translateText() {
  const text = document.getElementById('translateInput').value;
  const source = document.getElementById('sourceLang').value;
  const target = document.getElementById('targetLang').value;
  fetch('/translate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({text, source, target})
  })
  .then(res => res.json())
  .then(data => {
    const output = data.data.translations[0].translatedText;
    document.getElementById('translatedOutput').innerText = output;
  });
}
