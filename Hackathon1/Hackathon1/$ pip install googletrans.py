from googletrans import Translator
import sys

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

if __name__ == "__main__":
    text = sys.argv[1]
    dest_language = sys.argv[2]
    translated_text = translate_text(text, dest_language)
    print(translated_text)