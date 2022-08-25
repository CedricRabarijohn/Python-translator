import translators as ts

def translate_from_google(phrase, from_language, to_language):
    return ts.google(phrase, from_language, to_language)
