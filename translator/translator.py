from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

if __name__ == "__main__":
    while True:
        print("Enter text to translate (or 'exit' to quit):")
        user_input = input()

        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        print("Choose target language code (e.g., 'en' for English, 'es' for Spanish):")
        target_language = input()

        translated_text = translate_text(user_input, target_language)

        print("Translated text:")
        print(translated_text)