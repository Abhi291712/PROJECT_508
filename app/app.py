from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from app.service import Services
from db.mysql_repository import MysqlRepository

app = Flask(__name__)
CORS(app)

# Initialize services with MySQL repository
repo = MysqlRepository(host="localhost", user="root", password="root", database="devanagari")
services = Services(repo)

@app.route('/')
def index():
    return render_template('devanagari.html')

@app.route("/identify", methods=["POST"])
def identify_character():
    data = request.get_json()
    character = data.get('character')
    response = services.get_character_info(character)
    return jsonify(response)

@app.route("/transliterate", methods=["POST"])
def transliterate_word():
    data = request.get_json()
    word = data.get('word')
    response = services.transliterate_word(word)
    return jsonify({"transliterated_word": response})

if __name__ == "__main__":
    app.run(debug=True)