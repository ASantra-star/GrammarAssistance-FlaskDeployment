# translator.py
from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['target_language']
        translated_text = translate_text(text, target_language)
        return render_template('index.html', translated_text=translated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
