from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask('Web Translator')


@app.route('/englishToFrench')
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    return translator.english_to_french(text_to_translate)


@app.route('/frenchToEnglish')
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    return translator.french_to_english(text_to_translate)


@app.route('/')
def render_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
