from fastapi import FastAPI
from translate.translate import translate
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

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

@app.get("/")
async def home():
    html_content = """
    <html>
        <head>
            <title>Python translator</title>
        </head>
        <body style="min-height:100vh;display:flex;justify-content:center;align-items:center">
            <h1>Read the documentation here : <a href="https://github.com/CedricRabarijohn/Python-translator#python-translator">https://github.com/CedricRabarijohn/Python-translator</a></h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
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