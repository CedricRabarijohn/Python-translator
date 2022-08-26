from pydantic import BaseModel

class TranslationModelV3(BaseModel):
    texts: dict = {}
    to_language: str = 'fr'