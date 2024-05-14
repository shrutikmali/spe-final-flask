from flask import Flask
import pytesseract
from PIL import Image
from flask import request
from io import BytesIO
import base64
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/recognise", methods=["POST"])
def helloWord():
    requestData = request.get_json()
    encoded = requestData["img"]
    encoded = encoded.split(",")[1]
    decoded = base64.b64decode(encoded)

    imageData = BytesIO(decoded)
    image = Image.open(imageData)
    text = str(pytesseract.image_to_string(image))
    return {
        "text": text
    }
