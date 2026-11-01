# -*- coding: utf-8 -*-
import os
import shutil
import numpy as np
from PIL import Image, ImageEnhance
from collections import deque

artifact_dir = r"C:\Users\rigob\.gemini\antigravity\brain\2dfe657c-4e76-4940-b591-8aa8444b03a8"
signs_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\signs"
ui_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\ui"

# Copy the new 8K Apps banner
src_apps_banner = os.path.join(artifact_dir, "banner_apps_vortice_1793201170669.jpg")
dst_apps_banner = os.path.join(ui_dir, "banner_apps_vortice.jpg")
if os.path.exists(src_apps_banner):
    shutil.copy2(src_apps_banner, dst_apps_banner)
    print(f"Copied Apps Banner -> {dst_apps_banner}")

def extract_sign_from_white_bg(raw_path, out_path):
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im)
    h, w, _ = arr.shape
    r, g, b = arr[:, :, 0].astype(int), arr[:, :, 1].astype(int), arr[:, :, 2].astype(int)

    # White background flood-fill from image borders
    is_bg = (r > 228) & (g > 228) & (b > 228) & (np.abs(r - g) < 22) & (np.abs(g - b) < 22)
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
        x0, x1 = max(0, xs.min() - 4), min(w, xs.max() + 5)
        y0, y1 = max(0, ys.min() - 4), min(h, ys.max() + 5)
        arr = arr[y0:y1, x0:x1]

    out_im = Image.fromarray(arr, "RGBA")
    out_im = out_im.resize((1260, 590), Image.Resampling.LANCZOS)
    out_im.save(out_path, "PNG")
    print(f"Extracted CTB sign -> {os.path.basename(out_path)} ({out_im.size})")

# 1. Extract the 3 new wide rectangular CTB traffic signs
new_ctb_pairs = [
    (os.path.join(artifact_dir, "raw_sign_02_sacronia_ctb_1793201091250.jpg"), os.path.join(signs_dir, "sign_02_sacronia.png")),
    (os.path.join(artifact_dir, "raw_sign_07_trono_ctb_1793201114868.jpg"), os.path.join(signs_dir, "sign_07_trono.png")),
    (os.path.join(artifact_dir, "raw_sign_09_aliens_ctb_1793201139601.jpg"), os.path.join(signs_dir, "sign_09_aliens.png")),
]
for rp, dp in new_ctb_pairs:
    if os.path.exists(rp):
        extract_sign_from_white_bg(rp, dp)

# 2. Enhance gloss, vibrancy, contrast, sharpness, and metallic storm texture on ALL 10 signs
all_signs = [
    "sign_01_rock.png",
    "sign_02_sacronia.png",
    "sign_03_neon.png",
    "sign_04_iago.png",
    "sign_05_patinhas.png",
    "sign_06_aguas.png",
    "sign_07_trono.png",
    "sign_08_incorruptivel.png",
    "sign_09_aliens.png",
    "sign_10_aquario.png",
]

np.random.seed(42)

for idx, fn in enumerate(all_signs):
    p = os.path.join(signs_dir, fn)
    if not os.path.exists(p):
        continue
    im = Image.open(p).convert("RGBA")
    alpha = im.split()[3]
    rgb = im.convert("RGB")

    # Boost color saturation, contrast, and crisp metallic micro-texture
    rgb = ImageEnhance.Color(rgb).enhance(1.30)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.16)
    rgb = ImageEnhance.Sharpness(rgb).enhance(1.40)

    arr = np.array(rgb, dtype=np.float32)
    h, w, _ = arr.shape

    # Create diagonal glossy reflective road-sign enamel sheen + subtle wind-scratched storm wear
    yy, xx = np.mgrid[0:h, 0:w]
    nx = xx / float(w)
    ny = yy / float(h)

    band1 = np.exp(-((nx * 0.85 + ny * 0.55 - 0.50) ** 2) / (2 * (0.095 ** 2)))
    band2 = np.exp(-((nx * 0.85 + ny * 0.55 - 0.80) ** 2) / (2 * (0.045 ** 2)))
    gloss = (band1 * 32.0 + band2 * 20.0)[:, :, None]

    scratch_lines = np.zeros((h, w), dtype=np.float32)
    num_scratches = 16 + (idx % 4) * 5
    for _ in range(num_scratches):
        sy = np.random.randint(int(h * 0.08), int(h * 0.92))
        sx0 = np.random.randint(int(w * 0.05), int(w * 0.70))
        slen = np.random.randint(int(w * 0.06), int(w * 0.25))
        sx1 = min(w - 1, sx0 + slen)
        intensity = np.random.uniform(18.0, 38.0) if np.random.rand() > 0.4 else np.random.uniform(-26.0, -12.0)
        scratch_lines[max(0, sy - 1):min(h, sy + 2), sx0:sx1] = intensity

    arr = np.clip(arr + gloss + scratch_lines[:, :, None], 0, 255).astype(np.uint8)
    final_rgb = Image.fromarray(arr, "RGB")
    final_rgba = Image.merge("RGBA", (*final_rgb.split(), alpha))
    final_rgba.save(p, "PNG")
    print(f"Enhanced high-gloss & storm texture -> {fn}")
