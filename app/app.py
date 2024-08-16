from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from app.services import Services
from db.mysql_repository import MysqlRepository
import os

app = Flask(__name__)
CORS(app)

# Initialize services with MySQL repository
repo = MysqlRepository(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', 'rootpassword'),
    database=os.getenv('DB_NAME', 'devanagari')
)
services = Services(repo)

@app.route('/')
def home():
    return "Welcome to the Devanagari Translator API"

@app.route("/identify", methods=["POST"])
def identify_character():
    data = request.get_json()
    character = data.get('character')
    if not character:
        return jsonify({"error": "No character provided"}), 400
    response = services.get_character_info(character)
    return jsonify(response)

@app.route("/transliterate", methods=["POST"])
def transliterate_word():
    data = request.get_json()
    word = data.get('word')
    if not word:
        return jsonify({"error": "No word provided"}), 400
    response = services.transliterate_word(word)
    return jsonify({"transliterated_word": response})

@app.route("/characters", methods=["GET"])
def get_all_characters():
    characters = services.get_all_characters()
    return jsonify(characters)

@app.route('/ui')
def serve_ui():
    return send_from_directory('web', 'devanagari.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')