from pydantic import BaseModel

class TranslationModelV2(BaseModel):
    texts: object = {}
    from_language: str = 'auto'
    to_language: str = 'eng'