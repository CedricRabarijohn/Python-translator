import translators as ts

def translateFromGoogle(phrase, from_language, to_language):
    return ts.google(phrase, from_language, to_language)
