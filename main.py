from fastapi import FastAPI
from translate.translate import translate
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class TranslationModel(BaseModel):
    text: str = 'The text to translate'
    to_language: str = 'fr'

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    return {
        "message":"Pinged successfully"
    }

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