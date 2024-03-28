from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

lat = {'O\'': 'Ў', 'o\'': 'ў','Ch': 'Ч', 'ch': 'ч', 'Sh': 'Ш', 'sh': 'ш', 'ʼ':'ъ', '\'': 'ъ', 'Yu': 'Ю', 'yu': 'ю', 'Ya': 'Я', 'ya': 'я', 'Oʻ': 'Ў', 'oʻ': 'ў', 'Q': 'Қ', 'q': 'қ', 'Gʻ': 'Ғ', 'gʻ': 'ғ', 'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в', 'G': 'Г', 'g': 'г', 'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е', 'Yo': 'Ё', 'yo': 'ё', 'J': 'Ж', 'j': 'ж',
       'Z': 'З', 'z': 'з', 'I': 'И', 'i': 'и', 'Y': 'Й', 'y': 'й', 'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н', 'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у', 'F': 'Ф', 'f': 'ф', 'X': 'Х', 'x': 'х', 'H': 'Ҳ', 'h': 'ҳ', 'W': 'В', 'w': 'в'}

cyr = {'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Yo', 'ё': 'yo', 'Ж': 'J', 'ж': 'j', 'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'Y', 'й': 'y', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p',
       'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'X', 'х': 'x', 'Ц': 'S', 'ц': 's', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Ъ': 'ʼ', 'ъ': 'ʼ', 'Э': 'E', 'э': 'e', 'Ю': 'Yu', 'ю': 'yu', 'Я': 'Ya', 'я': 'ya', 'Ў': 'Oʻ', 'ў': 'oʻ', 'Қ': 'Q', 'қ': 'q', 'Ғ': 'Gʻ', 'ғ': 'gʻ', 'Ҳ': 'H', 'ҳ': 'h'}


def alphachanger(context, pattern):
    patterns = {"latin": cyr, "cyrillic": lat}
    if patterns.get(pattern):
        for before, after in patterns[pattern].items():
            context = context.replace(before, after)
        return context
    else:
        return False


@app.route('/')
def index():
    return 'AlphaChanger'


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


if __name__ == '__main__':
    app.run(debug=False)
