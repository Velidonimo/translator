from googletrans import Translator


def translate(word):
    try:
        word = str(word)
    except:
        return 'Слово неопознано'

    return Translator().translate(word, 'ru', 'en').text
