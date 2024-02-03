from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalleV1.1')
image = pipeline('Airoplane with red colour passing through clouds ').images[0]
print(image)
