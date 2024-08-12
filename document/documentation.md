# API Documentation

## Overview
The Devanagari Script Analyzer API provides functionality for transliterating words from Devanagari script to Latin script. It is built using Flask and allows for simple POST requests to achieve the transliteration.

## Endpoints

### `/transliterate`

- **URL**: `/transliterate`
- **Method**: POST
- **Description**: Transliterates a word from Devanagari script to Latin script.
- **Parameters**: None
- **Request Body**:
  - **Content-Type**: application/json
  - **Body Example**:
    ```json
    {
      "word": "नमस्ते"
    }
    ```
- **Response**:
  - **Success**:
    - **Status Code**: 200 OK
    - **Body Example**:
      ```json
      {
        "transliterated_word": "namaste"
      }
      ```
  - **Error**:
    - **Status Code**: 400 Bad Request (for invalid input)
    - **Body Example**:
      ```json
      {
        "error": "Invalid input"
      }
      ```
- **Examples**:
  - **Request Example**:
    ```bash
    curl -X POST "http://localhost:5000/transliterate" -H "Content-Type: application/json" -d '{"word":"नमस्ते"}'
    ```
  - **Response Example**:
    ```json
    {
      "transliterated_word": "namaste"
    }
    ```


