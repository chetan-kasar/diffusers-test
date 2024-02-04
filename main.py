from flask import Flask
import warnings
from flask_cors import CORS
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7")

app = Flask(__name__)
CORS(app)

@app.route("/home", methods=["POST"])
def home():
    data = request.get_json()
    prompt = data.get('prompt')
    print(prompt)'
    image = pipe(prompt=prompt, num_inference_steps=20, guidance_scale=0).images[0]
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str
    
@app.route("/")
def index():
    return "Index page !!!!!";
    
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
