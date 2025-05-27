from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route("/api/remove-bg", methods=["POST"])
def remove_bg():
    try:
        data = request.get_json()
        img_data = base64.b64decode(data["image"].split(",")[1])
        input_image = Image.open(io.BytesIO(img_data))
        output_image = remove(input_image)

        buffer = io.BytesIO()
        output_image.save(buffer, format="PNG")
        buffer.seek(0)

        return send_file(buffer, mimetype="image/png")
    except Exception as e:
        return {"error": str(e)}, 500
