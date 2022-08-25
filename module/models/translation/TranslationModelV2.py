from pydantic import BaseModel

class TranslationModelV2(BaseModel):
    texts: object = {}
    to_language: str = 'fr'