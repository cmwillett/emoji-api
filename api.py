from fastapi import FastAPI
from rembg import remove
from fastapi import File, UploadFile
from fastapi.responses import Response

from PIL import Image
import io

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)
    return Response(content=output_image, media_type="image/png")
