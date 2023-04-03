from translate import Translator

from_lang = input("Select a language to translate from: \n1. English\n2. Spanish\n")
to_lang = input("Select a language to translate to: \n1. English\n2. Spanish\n")

def main():
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    text = input("Enter a word or phrase: ")
    translation = translator.translate(text)
    print("Translation: " + translation)

main()