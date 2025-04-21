from flask import Flask, request, jsonify, send_from_directory
import requests, os, json

app = Flask(__name__)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/main.js")
def js():
    return send_from_directory(".", "main.js")

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()
        text = data.get("text")
        target = data.get("target")
        source = data.get("source", "")
        if not GOOGLE_API_KEY:
            return jsonify({"error": "Missing GOOGLE_API_KEY"}), 500
        payload = {
            "q": text,
            "target": target,
            "source": source,
            "key": GOOGLE_API_KEY
        }
        response = requests.post(TRANSLATE_URL, data=payload)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/save_poem", methods=["POST"])
def save_poem():
    try:
        data = request.json
        username = data.get('username', 'user')
        text = data.get('text', '')
        os.makedirs('poems', exist_ok=True)
        path = f'poems/{username}_poems.json'
        poems = []
        if os.path.exists(path):
            with open(path, 'r') as f:
                poems = json.load(f)
        poems.append({'text': text})
        with open(path, 'w') as f:
            json.dump(poems, f, indent=2)
        return jsonify({"status": "saved"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
