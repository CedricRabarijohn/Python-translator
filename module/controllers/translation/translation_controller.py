from cgitb import text
import imp
from module.services.translation.translation_service import translate_from_google
from module.models.translation.TranslationModelV1 import TranslationModelV1
from module.models.translation.TranslationModelV2 import TranslationModelV2
from module.services.utils import utils

# V2
async def translate_v2(translation_body_v2: TranslationModelV2):
    # The base language (ex: en, fr, es)
    from_lang = "auto"
    # The texts to translate
    texts = translation_body_v2.texts
    # The language to translate the texts to (ex: en, fr, es)
    to_lang = translation_body_v2.to_language
    # translate
    i = 0
    for attr in texts:
        texts[attr] = translate_from_google(texts[attr], from_language=from_lang, to_language=to_lang)
        i += 1
    # Payload of the response
    res = {
        "from_language": from_lang,
        "to_language":to_lang,
        "translated": texts
    }
    return res

# V1
async def translate_v1(translation_body_v1: TranslationModelV1):
    fromLang = "auto"
    text = translation_body_v1.text
    to_lang = translation_body_v1.to_language
    res = {
        "from_language": fromLang,
        "to_language": to_lang,
        # "translated":"Ceci est la traduction"
        "translated": translate_from_google(text, from_language=fromLang, to_language=to_lang)
    }
    return res