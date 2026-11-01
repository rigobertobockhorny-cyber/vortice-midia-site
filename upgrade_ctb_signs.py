# -*- coding: utf-8 -*-
import os
import math
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageChops

signs_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\signs"
raw_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\tornado\Site_Vortice_Midia_Tornado\images"

for fn in sorted(os.listdir(signs_dir)):
    if fn.endswith(".png"):
        p = os.path.join(signs_dir, fn)
        im = Image.open(p)
        print(f"{fn}: size={im.size}, mode={im.mode}")
