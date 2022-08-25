from fastapi import FastAPI
from translate.translate import translate
from pydantic import BaseModel
class TranslationModel(BaseModel):
    text: str = 'The text to translate'
    to_language: str = 'fr'

app = FastAPI()

@app.post("/translate")
async def root(translationBody: TranslationModel):
    fromLang = "auto"
    text = translationBody.text
    toLang = translationBody.to_language
    res = {
    "from_language": fromLang,
    "to_language": toLang,
    # "translated":"Ceci est la traduction"
    "translated": translate(text, from_language=fromLang, to_language=toLang)
    }
    return res