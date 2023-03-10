from PIL import Image
from clip_interrogator import Config, Interrogator

conf = Config(clip_model_name = "ViT-L-14/openai")
#conf.apply_low_vram_defaults()
ci = Interrogator(conf)

imagepath = './samples/00002.png'
image = Image.open(imagepath).convert('RGB')
print(ci.interrogate(image))
