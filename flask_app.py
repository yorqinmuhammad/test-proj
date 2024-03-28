from flask import Flask, jsonify, request
from flask_cors import CORS
from alphachanger.alphachanger import alphachanger
from spamfinder.spamchecker import checkspam
app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return '<h1>Muhammad Yorqin</h1><a href="https://yorqin.com/">yorqin.com</a> '


@app.route("/translate", methods=["POST"])
def changealph():
    data = request.get_json()

    if not data or "context" not in data or "pattern" not in data:
        return jsonify({'error': 'Invalid input.'}), 400

    context = data["context"]
    pattern = data["pattern"]

    # returning the context itself if it has only spaces
    if not context.strip():
        return jsonify({"result": context}), 200

    translated_text = alphachanger(context, pattern)

    if translated_text is False:
        return jsonify({'error': 'Invalid pattern.'}), 400

    return jsonify({"result": translated_text}), 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route("/spamcheck", methods=["POST"])
def spam_checker():
    data = request.get_json()
    email = data["email"]
    
    if not data or "email" not in data:
        return jsonify({'error': 'Invalid input.'}), 400
    
    if not email.strip():
        return jsonify({'error': 'Please enter valid mail.'}), 400
    
    result = checkspam(email)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=False)
