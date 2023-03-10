import os
import tqdm
from PIL import Image
from clip_interrogator import Config, Interrogator

def get_files(path):
    # read a folder, return the complete path of all files
    ret = []
    for root, dirs, files in os.walk(path):
        for filespath in files:
            ret.append(os.path.join(root, filespath))
    return ret

conf = Config(clip_model_name = "ViT-L-14/openai")
#conf.apply_low_vram_defaults()
ci = Interrogator(conf)

folderpath = './samples'
imglist = get_files(folderpath)
for i in tqdm(len(imglist)):
    imgpath = imglist[i]
    image = Image.open(imgpath).convert('RGB')
    print(imgpath)
    print(ci.interrogate(image))
