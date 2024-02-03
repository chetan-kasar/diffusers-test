from flask import Flask

app = Flask(__name__)

from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalleV1.1')

@app.route('/')
def hello_world():
    image = pipeline('Airoplane with red colour passing through clouds ').images[0]
    print(image)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
