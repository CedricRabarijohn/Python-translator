
from pydantic import BaseModel

class TranslationModelV1(BaseModel):
    text: str = 'The text to translate'
    to_language: str = 'fr'