# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import deepl

app = FastAPI()

DEEPL_API_KEY = "dein_deepl_api_key"
translator = deepl.Translator(DEEPL_API_KEY)

class TranslateRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

@app.post("/translate")
async def translate(req: TranslateRequest):
    result = translator.translate_text(req.text, source_lang=req.source_lang, target_lang=req.target_lang)
    return {"translated_text": result.text}
