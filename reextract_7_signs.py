# -*- coding: utf-8 -*-
import os
import glob
import numpy as np
from PIL import Image, ImageEnhance
from collections import deque

signs_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\signs"
raw_tornado_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\tornado\Site_Vortice_Midia_Tornado\images"

def extract_and_polish(raw_path, out_path):
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im)
    h, w, _ = arr.shape
    r, g, b = arr[:, :, 0].astype(int), arr[:, :, 1].astype(int), arr[:, :, 2].astype(int)

    is_bg = (r > 225) & (g > 225) & (b > 225) & (np.abs(r - g) < 24) & (np.abs(g - b) < 24)
    visited = np.zeros((h, w), dtype=bool)
    q = deque()

    for x in range(w):
        if is_bg[0, x]:
            visited[0, x] = True
            q.append((0, x))
        if is_bg[h - 1, x]:
            visited[h - 1, x] = True
            q.append((h - 1, x))
    for y in range(h):
        if is_bg[y, 0]:
            visited[y, 0] = True
            q.append((y, 0))
        if is_bg[y, w - 1]:
            visited[y, w - 1] = True
            q.append((y, w - 1))

    while q:
        cy, cx = q.popleft()
        for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and is_bg[ny, nx]:
                visited[ny, nx] = True
                q.append((ny, nx))

    arr[visited, 3] = 0
    alpha = arr[:, :, 3]
    ys, xs = np.where(alpha > 20)
    if len(xs) > 0 and len(ys) > 0:
        x0, x1 = max(0, xs.min() - 2), min(w, xs.max() + 3)
        y0, y1 = max(0, ys.min() - 2), min(h, ys.max() + 3)
        arr = arr[y0:y1, x0:x1]

    out_im = Image.fromarray(arr, "RGBA").resize((1260, 590), Image.Resampling.LANCZOS)
    alpha_ch = out_im.split()[3]
    rgb = out_im.convert("RGB")
    rgb = ImageEnhance.Color(rgb).enhance(1.36)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.18)
    rgb = ImageEnhance.Sharpness(rgb).enhance(1.42)

    f_arr = np.array(rgb, dtype=np.float32)
    fh, fw, _ = f_arr.shape
    yy, xx = np.mgrid[0:fh, 0:fw]
    nx = xx / float(fw)
    ny = yy / float(fh)

    band1 = np.exp(-((nx * 0.82 + ny * 0.58 - 0.48) ** 2) / (2 * (0.11 ** 2)))
    band2 = np.exp(-((nx * 0.82 + ny * 0.58 - 0.78) ** 2) / (2 * (0.05 ** 2)))
    gloss = (band1 * 34.0 + band2 * 20.0)[:, :, None]

    f_arr = np.clip(f_arr + gloss, 0, 255).astype(np.uint8)
    final_rgb = Image.fromarray(f_arr, "RGB")
    final_rgba = Image.merge("RGBA", (*final_rgb.split(), alpha_ch))
    final_rgba.save(out_path, "PNG")
    print(f"Re-extracted & polished -> {os.path.basename(out_path)}")

prefix_map = {
    "26_": "sign_01_rock.png",
    "37_": "sign_03_neon.png",
    "29_": "sign_04_iago.png",
    "30_": "sign_05_patinhas.png",
    "31_": "sign_06_aguas.png",
    "33_": "sign_08_incorruptivel.png",
    "35_": "sign_10_aquario.png",
}

for pref, dst_fn in prefix_map.items():
    matches = glob.glob(os.path.join(raw_tornado_dir, f"{pref}*.jpg"))
    if matches:
        extract_and_polish(matches[0], os.path.join(signs_dir, dst_fn))
