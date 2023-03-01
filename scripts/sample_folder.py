import os
import tqdm
from PIL import Image
from clip_interrogator import Config, Interrogator

conf = Config(clip_model_name="ViT-L-14/openai")
#conf.apply_low_vram_defaults()
ci = Interrogator(conf)

folderpath = './samples'
for i in tqdm(range(1, 11)):
    imgname = str(i).zfill(5) + '.png'
    imgpath = os.path.join(folderpath, imgname)
    image = Image.open(imgpath).convert('RGB')
    print(imgname)
    print(ci.interrogate(image))
