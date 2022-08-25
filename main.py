from fastapi import FastAPI
from services.translation.translationService import translateFromGoogle
from models.translation.TranslationModelV1 import TranslationModelV1
from models.translation.TranslationModelV2 import TranslationModelV2
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from controllers.translation.TranslationController import translateV1
from controllers.translation.TranslationController import translateV2

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

@app.post("/v1/translate")
async def translateFunctionV1(translationBody: TranslationModelV1):
    res = await translateV1(translationBody)
    return res

@app.post("/v2/translate")
async def translateFunctionV2(translationBodyV2: TranslationModelV2):
    res = await translateV2(translationBodyV2)
    return res
