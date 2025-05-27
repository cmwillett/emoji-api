from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Emoji background removal API is running..."}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes)
    return Response(content=output_bytes, media_type="image/png")