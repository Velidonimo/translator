from googletrans import Translator
import database


def translate(word):
    """Translate the word to russian"""
    try:
        word = str(word)
    except:
        return 'Слово неопознано'

    translation = Translator().translate(word, 'ru', 'en')

    database.save_translate(word, translation.text)

    return translation.text
