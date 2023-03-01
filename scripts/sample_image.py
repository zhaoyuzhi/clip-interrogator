from PIL import Image
from clip_interrogator import Config, Interrogator

conf = Config(clip_model_name="ViT-L-14/openai")
conf.apply_low_vram_defaults()
ci = Interrogator(conf)

image_path='./samples/10.png'
image = Image.open(image_path).convert('RGB')
print(ci.interrogate(image))
