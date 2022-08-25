from module.services.translation.translation_service import translate_from_google
from module.models.translation.TranslationModelV1 import TranslationModelV1
from module.models.translation.TranslationModelV2 import TranslationModelV2

# V1 of translation
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
    
# V2 of translation
async def translate_v2(translation_body_v2: TranslationModelV2):
    from_lang = "auto"
    texts = translation_body_v2.texts
    to_lang = translation_body_v2.to_language
    text_arr = []
    for attr in texts:
        text_arr.append(texts[attr])
    text_concatened = '|||'.join(text_arr)
    translated_text = translate_from_google(text_concatened, from_language=from_lang, to_language=to_lang)
    translated_arr = translated_text.split(' ||| ')
    i = 0
    for attr in texts:
        texts[attr] = translated_arr[i]
        i += 1
    res = {
        "from_language": from_lang,
        "to_language":to_lang,
        "translated": texts
    }
    return res