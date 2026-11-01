# -*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw
from collections import deque

artifact_dir = r"C:\Users\rigob\.gemini\antigravity\brain\2dfe657c-4e76-4940-b591-8aa8444b03a8"
signs_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\signs"
raw_tornado_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\assets\tornado\Site_Vortice_Midia_Tornado\images"

def extract_white_bg_clean(raw_path, out_path):
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
    out_im.save(out_path, "PNG")

# 1. Extract Sacronia from raw_sign_02_sacronia_ctb by detecting the grey concrete outside the plate
sac_raw = os.path.join(artifact_dir, "raw_sign_02_sacronia_ctb_1793201091250.jpg")
im_sac = Image.open(sac_raw).convert("RGBA")
arr_sac = np.array(im_sac)
sh, sw, _ = arr_sac.shape
r, g, b = arr_sac[:, :, 0].astype(int), arr_sac[:, :, 1].astype(int), arr_sac[:, :, 2].astype(int)
# Concrete is low-saturation grey: |r-g| < 18 and |g-b| < 18 and 95 < r < 220
is_concrete = (np.abs(r - g) < 18) & (np.abs(g - b) < 18) & (np.abs(r - b) < 20) & (r > 80) & (r < 225)
# Find bounding box of the colorful sign (where saturation is high: r - b > 35)
is_sign_color = (r - b > 35)
ys, xs = np.where(is_sign_color)
x0, x1 = max(0, xs.min() - 8), min(sw, xs.max() + 8)
y0, y1 = max(0, ys.min() - 8), min(sh, ys.max() + 8)
cropped_sac = Image.fromarray(arr_sac[y0:y1, x0:x1], "RGBA").resize((1260, 590), Image.Resampling.LANCZOS)

# Apply clean rounded-rectangle alpha mask matching the metal plate corners
mask = Image.new("L", (1260, 590), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle([(4, 4), (1255, 585)], radius=42, fill=255)
cropped_sac.putalpha(mask)
cropped_sac.save(os.path.join(signs_dir, "sign_02_sacronia.png"), "PNG")
print("Cleaned & cropped sign_02_sacronia.png with rounded metal corners!")

# 2. Re-extract Trono and Aliens cleanly from their raw high-res files
extract_white_bg_clean(
    os.path.join(artifact_dir, "raw_sign_07_trono_ctb_1793201114868.jpg"),
    os.path.join(signs_dir, "sign_07_trono.png")
)
extract_white_bg_clean(
    os.path.join(artifact_dir, "raw_sign_09_aliens_ctb_1793201139601.jpg"),
    os.path.join(signs_dir, "sign_09_aliens.png")
)

# 3. Also re-extract the other 7 signs from raw_tornado_dir and apply clean gloss/color enhancement (no synthetic horizontal lines!)
raw_map = {
    "sign_01_rock.png": "26_Front-facing_flat_orthographic_view_of_a_distressed_heavy-metal_crimson-red_and_.jpg",
    "sign_03_neon.png": "37_Front-facing_flat_orthographic_view_of_a_wide_horizontal_rectangular_midnight-bl.jpg",
    "sign_04_iago.png": "29_Front-facing_flat_orthographic_view_of_a_vintage_weathered_forest-green_and_warm.jpg",
    "sign_05_patinhas.png": "30_Front-facing_flat_orthographic_view_of_a_warm_rustic_wooden_and_enamel_park_trai.jpg",
    "sign_06_aguas.png": "31_Front-facing_flat_orthographic_view_of_a_serene_midnight-blue_and_silver_reflect.jpg",
    "sign_08_incorruptivel.png": "33_Front-facing_flat_orthographic_view_of_a_gritty_black_and_hazard-yellow_chevron_.jpg",
    "sign_10_aquario.png": "35_Front-facing_flat_orthographic_view_of_a_whimsical_3D_turquoise-aqua_and_coral-o.jpg",
}

for dst_fn, raw_fn in raw_map.items():
    rp = os.path.join(raw_tornado_dir, raw_fn)
    if os.path.exists(rp):
        extract_white_bg_clean(rp, os.path.join(signs_dir, dst_fn))

# 4. Apply natural glossy enamel sheen + vibrancy boost to all 10 signs
for fn in sorted(os.listdir(signs_dir)):
    if not fn.startswith("sign_") or not fn.endswith(".png"):
        continue
    p = os.path.join(signs_dir, fn)
    im = Image.open(p).convert("RGBA")
    alpha = im.split()[3]
    rgb = im.convert("RGB")

    rgb = ImageEnhance.Color(rgb).enhance(1.32)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.16)
    rgb = ImageEnhance.Sharpness(rgb).enhance(1.38)

    arr = np.array(rgb, dtype=np.float32)
    h, w, _ = arr.shape
    yy, xx = np.mgrid[0:h, 0:w]
    nx = xx / float(w)
    ny = yy / float(h)

    # Smooth diagonal specular gloss reflection across the metal plate
    band1 = np.exp(-((nx * 0.82 + ny * 0.58 - 0.48) ** 2) / (2 * (0.11 ** 2)))
    band2 = np.exp(-((nx * 0.82 + ny * 0.58 - 0.78) ** 2) / (2 * (0.05 ** 2)))
    gloss = (band1 * 30.0 + band2 * 18.0)[:, :, None]

    arr = np.clip(arr + gloss, 0, 255).astype(np.uint8)
    final_rgb = Image.fromarray(arr, "RGB")
    final_rgba = Image.merge("RGBA", (*final_rgb.split(), alpha))
    final_rgba.save(p, "PNG")
    print(f"Polished high-gloss CTB sign -> {fn}")
