# api.py

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from rembg import remove
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Emoji API is running."}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes)
    return JSONResponse(content={"message": "background removed!"})
