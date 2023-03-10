import os
import cv2
import tqdm
from PIL import Image
from clip_interrogator import Config, Interrogator

conf = Config(clip_model_name = "ViT-L-14/openai")
#conf.apply_low_vram_defaults()
ci = Interrogator(conf)

folderpath = '/apdcephfs/share_1159505/hosizhao/ft_local/vimeo_septuplet/sequences'
for i in range(1, 97):
    for j in range(1, 1001):
        for k in range(1, 8):
            imgpath = os.path.join(folderpath, str(i).zfill(5), str(j).zfill(4), 'im' + str(k) + '.png')
            image = Image.open(imgpath).convert('RGB')
            image = cv2.resize(image, (896, 512))
            print(imgpath)
            print(ci.interrogate_best(image))
