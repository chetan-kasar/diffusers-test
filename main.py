from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
import base64

from huggingface_hub import InferenceClient
client = InferenceClient(token= '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', model="dataautogpt3/OpenDalleV1.1")

# image = client.text_to_image("dog")
# image.save("dog.png")
# print("Image downloaded")
# print(image)

app = Flask(__name__)

@app.route("/home", methods=["POST"])
def home():
    prompt = request.form.get("prompt")
    image = client.text_to_image(prompt)
    image.save(f"./images/{prompt}.png")
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return render_template("display.html", img_str=img_str)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=9000)