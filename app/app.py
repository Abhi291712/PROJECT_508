from flask import Flask, request, jsonify
from flask_cors import CORS
from logging.config import dictConfig

app = Flask(__name__)
CORS(app)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# Mock data for demonstration
CHARACTER_DATA = {
    "अ": {"Character Symbol": "अ", "Name": "a", "Type": "Vowel", "Pronunciation": "/a/ (like 'a' in 'about')"},
}

TRANSLITERATIONS = {
    "नमस्ते": "namaste",
}

@app.route('/')
def doc() -> str:
    with open("app/doc.html", "r") as f:
        return f.read()

@app.route("/identify", methods=["POST"])
def identify_character():
    data = request.get_json()
    character = data.get('character')
    response = CHARACTER_DATA.get(character, {"error": "Character not found"})
    return jsonify(response)

@app.route("/transliterate", methods=["POST"])
def transliterate_word():
    data = request.get_json()
    word = data.get('word')
    if all('\u0900' <= char <= '\u097F' for char in word):  # Check if all characters are Devanagari
        transliterated_word = TRANSLITERATIONS.get(word, "Error: Word not found or invalid")
        return jsonify({"transliterated_word": transliterated_word})
    else:
        return jsonify({"error": "Input contains non-Devanagari characters"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
