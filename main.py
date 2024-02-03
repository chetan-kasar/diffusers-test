from flask import Flask
import torch
from diffusers import LCMScheduler, AutoPipelineForText2Image

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
adapter_id = "latent-consistency/lcm-lora-sdxl"

pipe = AutoPipelineForText2Image.from_pretrained(model_id, torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
pipe.to("cuda")

pipe.load_lora_weights(adapter_id)
pipe.fuse_lora()

app = Flask(__name__)



@app.route('/hello')
def hello_world():
    prompt = "realistic boy"
    image = pipe(prompt=prompt, num_inference_steps=6, guidance_scale=0).images[0]
    print(image)
    return 'Hello, World!'
    
@app.route("/")
def index():
    return "Index page !!!!!";
    
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
