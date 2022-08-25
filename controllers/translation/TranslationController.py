import imp
from services.translation.translationService import translateFromGoogle
from models.translation.TranslationModelV1 import TranslationModelV1
from models.translation.TranslationModelV2 import TranslationModelV2

# V1 of translation
async def translateV1(translationBody: TranslationModelV1):
    fromLang = "auto"
    text = translationBody.text
    toLang = translationBody.to_language
    res = {
        "from_language": fromLang,
        "to_language": toLang,
        # "translated":"Ceci est la traduction"
        "translated": translateFromGoogle(text, from_language=fromLang, to_language=toLang)
    }
    return res
    
# V2 of translation
async def translateV2(translationBodyV2: TranslationModelV2):
    fromLang = "auto"
    texts = translationBodyV2.texts
    toLang = translationBodyV2.to_language
    textArr = []
    for attr in texts:
        textArr.append(texts[attr])
    textConcatened = '|||'.join(textArr)
    translatedText = translateFromGoogle(textConcatened, from_language=fromLang, to_language=toLang)
    translatedArr = translatedText.split(' ||| ')
    i = 0
    for attr in texts:
        texts[attr] = translatedArr[i]
        i += 1
    res = {
        "from_language": fromLang,
        "to_language":toLang,
        "translated": texts
    }
    return res