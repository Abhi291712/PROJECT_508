# Devanagari Translator API

This API provides two main functionalities: identifying Devanagari characters and transliterating Devanagari words to Latin script.

## 1. Identify Devanagari Character

### Description
This endpoint identifies a single Devanagari character and provides information about it.

### Endpoint
POST /identify

### Request Format
{
  "character": "अ"
}

### Response Format
{

  "symbol": "अ",
  "name": "a",
  "type": "Vowel",
  "pronunciation": "/a/ (like 'a' in 'about')"
}

### Example cURL Command
curl -X POST "http://localhost:5000/identify" \
     -H "Content-Type: application/json" \
     -d '{"character":"अ"}'

### Example Python Request
import requests

url = "http://localhost:5000/identify"
data = {"character": "अ"}
response = requests.post(url, json=data)
print(response.json())

## 2. Transliterate Devanagari Word

### Description
This endpoint transliterates a Devanagari word to Latin script.

### Endpoint
POST /transliterate

### Request Format
{
  "word": "नमस्ते"
}

### Response Format
{
  "transliterated_word": "namaste"
}

### Example cURL Command
curl -X POST "http://localhost:5000/transliterate" \
     -H "Content-Type: application/json" \
     -d '{"word":"नमस्ते"}'

### Example Python Request
import requests

url = "http://localhost:5000/transliterate"
data = {"word": "नमस्ते"}
response = requests.post(url, json=data)
print(response.json())

## Error Handling

If an error occurs, the API will return a JSON object with an "error" key describing the issue.

Example error response:
{
  "error": "Invalid input: character not found"
}

## Notes

- Ensure that your requests use UTF-8 encoding to properly handle Devanagari characters.

