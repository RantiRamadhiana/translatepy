from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        translated = translator.translate(text, dest='id').text
        return jsonify({"translatedText": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
