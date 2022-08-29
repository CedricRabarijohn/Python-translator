from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from module.models.translation.TranslationModelV1 import TranslationModelV1
from module.models.translation.TranslationModelV2 import TranslationModelV2
from module.controllers.translation.translation_controller import translate_v1
from module.controllers.translation.translation_controller import translate_v2

app = FastAPI()
# Adding CORS MiddleWare
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# HTML showing where to read the documentations
@app.get("/")
async def home():
    html_content = """
    <html>
        <head>
            <title>Python translator</title>
        </head>
        <body style="min-height:100vh;display:flex;justify-content:center;align-items:center">
            <h1>Read the documentation <a href="https://github.com/CedricRabarijohn/Python-translator#python-translator">here</a></h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# A simple endpoint to ping so the server don't sleep (Ex : UptimeRobot)
@app.get("/ping")
async def ping():
    return {
        "message":"Pinged successfully"
    }

# !! (NEW)
# Translate V2
@app.post("/v2/translate")
async def translate_function_v2(translation_body_v2: TranslationModelV2):
    res = await translate_v2(translation_body_v2)
    return res

# Translate V1
@app.post("/v1/translate")
async def translate_function_v1(translation_body_v1: TranslationModelV1):
    res = await translate_v1(translation_body_v1)
    return res

