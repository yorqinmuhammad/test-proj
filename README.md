# AlphaChanger

AlphaChanger is a FlaskAPI-based application that allows users to convert text between Latin and Cyrillic alphabets. This can be particularly useful for users who need to transliterate text between these two alphabets.

## Features

- Convert text from Latin to Cyrillic and vice versa.
- Lightweight and easy to integrate into other applications.

## Usage

To use AlphaChanger, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/muhammadjon-dev/AlphaChanger.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python flask_app.py
    ```

4. Access the application in your browser at `http://muhammadyorqin.pythonanywhere.com`.

5. Use the provided API endpoint (`/translate`) to convert text programmatically. Send a POST request with JSON data containing the `context` and `pattern` fields to convert text.

## API Endpoint

### POST /translate

Convert text between Uzbek Latin and Uzbek Cyrillic alphabets.

#### Request

```json
{
    "context": "Text to convert",
    "pattern": "latin" or "cyrillic"
}
```
context: The text to be converted.
pattern: The desired output pattern, either "latin" or "cyrillic".

Response
```json
{
    "result": "Converted text"
}
```

### Contributing
Contributions are welcome! 

### Acknowledgements
* [Flask](https://flask.palletsprojects.com/en/3.0.x/api/): The web framework used for building the application.
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/): A Flask extension for handling Cross-Origin Resource Sharing (CORS).
