from flask import Flask
import warnings

from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7")

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    prompt = "Real boy"
    images = pipe(prompt=prompt, num_inference_steps=20, guidance_scale=0).images[0]
    images.save("./image.png")
    print(images)
    return 'Hello, World!'
    
@app.route("/")
def index():
    return "Index page !!!!!";
    
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
