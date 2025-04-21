from flask import Flask, render_template, request, jsonify
import requests
import os, json

app = Flask(__name__)

GOOGLE_API_KEY = "AIzaSyDRo0A6b-LQpzIXV5XiVYimZWBA2pGTgd4"
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    target = data.get("target")
    source = data.get("source", "")
    payload = {
        "q": text,
        "target": target,
        "source": source,
        "key": GOOGLE_API_KEY
    }
    response = requests.post(TRANSLATE_URL, data=payload)
    return jsonify(response.json())

@app.route("/save_poem", methods=["POST"])
def save_poem():
    data = request.json
    username = data.get('username')
    text = data.get('text')
    os.makedirs('poems', exist_ok=True)
    path = f'poems/{username}_poems.json'
    if os.path.exists(path):
        with open(path, 'r') as f:
            poems = json.load(f)
    else:
        poems = []
    poems.append({'text': text})
    with open(path, 'w') as f:
        json.dump(poems, f, indent=2)
    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(debug=True)
