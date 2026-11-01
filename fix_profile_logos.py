# -*- coding: utf-8 -*-
import os
import shutil
import json
import numpy as np
from PIL import Image, ImageOps, ImageFilter

SITE_DIR = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA"
LOGOS_COLOR_DIR = os.path.join(SITE_DIR, "assets", "logos_color")
BANNERS_DIR = os.path.join(SITE_DIR, "assets", "banners")

os.makedirs(LOGOS_COLOR_DIR, exist_ok=True)
os.makedirs(BANNERS_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 1. ROCK INCORRUPTÍVEL:
#    - Profile Logo: Official ROCK / INCORRUPTÍVEL white distressed logo on pure #000000 1:1 (1000x1000)
#    - Banner: Official 2K banner with the 5 consistent band members + Brazilian Rock Van
# -------------------------------------------------------------------------
rock_logo_src = r"C:\PROJETOS\1-CANAIS\2-ROCK_INCORRUPTIVEL\2_ASSETS\DIVERSOS\WhatsApp Image 2026-09-05 at 22.02.19 (1).jpeg"
img_rock = Image.open(rock_logo_src).convert("RGB")
arr_rock = np.array(img_rock)
# Find bounding box of non-black pixels (threshold > 30)
mask_rock = np.any(arr_rock > 35, axis=2)
ys, xs = np.where(mask_rock)
crop_rock = img_rock.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
# Make pure black background where dark
arr_crop = np.array(crop_rock).astype(np.float32)
lum = arr_crop.mean(axis=2)
# Enhance contrast so black is 100% #000000 and white is crisp
arr_crop[lum < 35] = 0
crop_rock = Image.fromarray(np.clip(arr_crop, 0, 255).astype(np.uint8))

canvas_rock = Image.new("RGB", (1000, 1000), (0, 0, 0))
target_w = 880
scale = target_w / crop_rock.width
target_h = int(crop_rock.height * scale)
if target_h > 880:
    scale = 880 / crop_rock.height
    target_w = int(crop_rock.width * scale)
    target_h = 880
resized_rock = crop_rock.resize((target_w, target_h), Image.Resampling.LANCZOS)
canvas_rock.paste(resized_rock, ((1000 - target_w) // 2, (1000 - target_h) // 2))
canvas_rock.save(os.path.join(LOGOS_COLOR_DIR, "rock_color.jpg"), quality=96)
canvas_rock.save(os.path.join(LOGOS_COLOR_DIR, "rock_color.png"))
print("Saved rock_color.jpg & rock_color.png")

# Copy official 2K Rock Incorruptível banner (with Beto, Kiko, Pitico, Duda, Marcão + VanDoRock_Brasil_3D)
rock_banner_src = r"C:\PROJETOS\1-CANAIS\2-ROCK_INCORRUPTIVEL\2_ASSETS\IDENTIDADE_VISUAL\20_[upscale-2k]_Cinematic_2560x1440_ultra-wide_YouTube_channel_hea.jpg"
shutil.copy2(rock_banner_src, os.path.join(BANNERS_DIR, "rock_youtube_banner.jpg"))
print("Copied official Rock Incorruptivel 2K banner to rock_youtube_banner.jpg")

# -------------------------------------------------------------------------
# 2. NEON ASHER:
#    - Profile Logo: Full-bleed 1:1 (1000x1000) from LOGO II.jpeg with ZERO black bars top/bottom,
#      extending the dark blue/concrete lightning background vertically and enlarging the NEON ASHER text.
# -------------------------------------------------------------------------
neon_logo_src = r"C:\PROJETOS\1-CANAIS\10-NEON_ASHER\2_ASSETS\LOGO II.jpeg"
img_neon = Image.open(neon_logo_src).convert("RGB")
w_n, h_n = img_neon.size  # 1280 x 720
# First, create a 1000x1000 background by taking the central square or stretching/mirroring the dark texture
# Wait: if we crop the horizontal center (e.g. width 920 of 1280) so NEON ASHER is much larger,
# its height is 720. To make it 920x920 without any seam or black margin:
crop_w = int(w_n * 0.76)  # 972px wide so NEON ASHER fills the width nicely!
x0 = (w_n - crop_w) // 2
center_crop = img_neon.crop((x0, 0, x0 + crop_w, h_n))  # 972 x 720
# Now let's build a 972 x 972 square by mirroring the top 126px and bottom 126px of the dark concrete texture
# and blending the seam smoothly over 30px!
pad_top = (crop_w - h_n) // 2  # 126
pad_bot = crop_w - h_n - pad_top  # 126
sq_neon = Image.new("RGB", (crop_w, crop_w))
# Top strip: flipped top of center_crop (rows 10 to 10+pad_top+30)
top_strip = center_crop.crop((0, 8, crop_w, 8 + pad_top)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
bot_strip = center_crop.crop((0, h_n - 8 - pad_bot, crop_w, h_n - 8)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
sq_neon.paste(top_strip, (0, 0))
sq_neon.paste(center_crop, (0, pad_top))
sq_neon.paste(bot_strip, (0, pad_top + h_n))
# Smooth blend 24px around y=pad_top and y=pad_top+h_n
arr_neon = np.array(sq_neon).astype(np.float32)
for dy in range(-16, 17):
    alpha = (dy + 16) / 32.0
    y_idx = pad_top + dy
    # Blend slightly with gaussian-smoothed version around the seam
blur_neon = np.array(sq_neon.filter(ImageFilter.GaussianBlur(radius=8))).astype(np.float32)
for seam_y in [pad_top, pad_top + h_n]:
    for dy in range(-18, 19):
        w_blend = 1.0 - (abs(dy) / 19.0)
        arr_neon[seam_y + dy] = arr_neon[seam_y + dy] * (1.0 - 0.65 * w_blend) + blur_neon[seam_y + dy] * (0.65 * w_blend)
sq_neon = Image.fromarray(np.clip(arr_neon, 0, 255).astype(np.uint8)).resize((1000, 1000), Image.Resampling.LANCZOS)
sq_neon.save(os.path.join(LOGOS_COLOR_DIR, "neon_color.jpg"), quality=96)
print("Saved full-bleed 1:1 neon_color.jpg")

# -------------------------------------------------------------------------
# 3. IAGO CORDEIRO:
#    - Profile Logo: ONLY "IAGO" on top and "CORDEIRO" below on pure #000000 black 1:1 square (NO LION!)
# -------------------------------------------------------------------------
iago_lockup_src = os.path.join(SITE_DIR, "assets", "sign_logos", "lockup_04_iago.png")
img_iago = Image.open(iago_lockup_src).convert("RGBA")
# Extract bright white lettering from lockup_04_iago.png
arr_iago = np.array(img_iago).astype(np.float32)
# In lockup_04_iago.png, the inside of the letters is bright white (R,G,B > 200) and the outline is black.
# On a pure black background, we want crisp solid white letters ("IAGO" on top, "CORDEIRO" below)!
lum_iago = (arr_iago[:, :, 0] + arr_iago[:, :, 1] + arr_iago[:, :, 2]) / 3.0
alpha_iago = arr_iago[:, :, 3] / 255.0
white_intensity = np.clip((lum_iago - 80.0) / (235.0 - 80.0), 0.0, 1.0) * alpha_iago
ys_i, xs_i = np.where(white_intensity > 0.15)
w_mask = white_intensity[ys_i.min():ys_i.max()+1, xs_i.min():xs_i.max()+1]
rgb_iago = np.zeros((w_mask.shape[0], w_mask.shape[1], 3), dtype=np.uint8)
for c in range(3):
    rgb_iago[:, :, c] = (w_mask * 255).astype(np.uint8)
crop_iago = Image.fromarray(rgb_iago)
canvas_iago = Image.new("RGB", (1000, 1000), (0, 0, 0))
tw_i = 880
th_i = int(crop_iago.height * (tw_i / crop_iago.width))
res_iago = crop_iago.resize((tw_i, th_i), Image.Resampling.LANCZOS)
canvas_iago.paste(res_iago, ((1000 - tw_i) // 2, (1000 - th_i) // 2))
canvas_iago.save(os.path.join(LOGOS_COLOR_DIR, "iago_color.png"))
print("Saved typography-only iago_color.png")

# -------------------------------------------------------------------------
# 4. ÁGUAS DE DESCANSO:
#    - Profile Logo: Official original logo from C:\PROJETOS\1-CANAIS\4-ÁGUAS_DE_DESCANSO\2_ASSETS\LOGO DE PERFIL.jpg
#      with outer white corners filled with the exact dark circle background (#0c1015) so it fills 1:1 seamlessly.
# -------------------------------------------------------------------------
aguas_logo_src = os.path.join(LOGOS_COLOR_DIR, "aguas_orig_src.jpg")
img_aguas = Image.open(aguas_logo_src).convert("RGB").resize((1000, 1000), Image.Resampling.LANCZOS)
arr_aguas = np.array(img_aguas)
# Replace the bright white outer corners outside radius 470 from center (500, 500) with the dark circle background color (12, 16, 21)
yy, xx = np.ogrid[:1000, :1000]
dist = np.sqrt((xx - 500.0)**2 + (yy - 500.0)**2)
outer_mask = dist > 468.0
arr_aguas[outer_mask] = [11, 15, 20]
# Also zoom in 12% so the golden text "ÁGUAS DE DESCANSO" is large and crisp
img_aguas_clean = Image.fromarray(arr_aguas)
c_margin = 70
img_aguas_zoomed = img_aguas_clean.crop((c_margin, c_margin, 1000 - c_margin, 1000 - c_margin)).resize((1000, 1000), Image.Resampling.LANCZOS)
img_aguas_zoomed.save(os.path.join(LOGOS_COLOR_DIR, "aguas_color.png"))
print("Saved official aguas_color.png")

# -------------------------------------------------------------------------
# 5. TRONO DA PROMESSA:
#    - Profile Logo: Official vignette logo [LogoTronoDaPromessa_Oficial_FundoPreto].png on pure #000000 1:1
# -------------------------------------------------------------------------
trono_logo_src = r"C:\PROJETOS\1-CANAIS\7-TRONO_DA_PROMESSA\2_ASSETS\VINHETAS\LOGO\[LogoTronoDaPromessa_Oficial_FundoPreto].png"
img_trono = Image.open(trono_logo_src).convert("RGB")
arr_trono = np.array(img_trono)
mask_trono = np.any(arr_trono > 18, axis=2)
ys_t, xs_t = np.where(mask_trono)
crop_trono = img_trono.crop((xs_t.min(), ys_t.min(), xs_t.max() + 1, ys_t.max() + 1))
canvas_trono = Image.new("RGB", (1000, 1000), (0, 0, 0))
tw_t = 900
th_t = int(crop_trono.height * (tw_t / crop_trono.width))
if th_t > 900:
    th_t = 900
    tw_t = int(crop_trono.width * (th_t / crop_trono.height))
res_trono = crop_trono.resize((tw_t, th_t), Image.Resampling.LANCZOS)
canvas_trono.paste(res_trono, ((1000 - tw_t) // 2, (1000 - th_t) // 2))
canvas_trono.save(os.path.join(LOGOS_COLOR_DIR, "trono_color.png"))
print("Saved official trono_color.png")

# -------------------------------------------------------------------------
# 6. INCORRUPTÍVEL:
#    - Profile Logo: Official distressed white "INCORRUPTÍVEL" typography on pure #000000 1:1
# -------------------------------------------------------------------------
inc_dirs = [d for d in os.listdir(r"C:\PROJETOS\1-CANAIS") if d.startswith("1-INCORRUPT")][0]
inc_logo_src = os.path.join(r"C:\PROJETOS\1-CANAIS", inc_dirs, "2_ASSETS", "IDENTIDADE_VISUAL", "logo_canal_pb.png")
img_inc = Image.open(inc_logo_src).convert("RGBA")
arr_inc = np.array(img_inc)
# In logo_canal_pb.png, find non-transparent or bright pixels
alpha_inc = arr_inc[:, :, 3]
ys_inc, xs_inc = np.where(alpha_inc > 20)
crop_inc = img_inc.crop((xs_inc.min(), ys_inc.min(), xs_inc.max() + 1, ys_inc.max() + 1))
bg_inc = Image.new("RGBA", crop_inc.size, (0, 0, 0, 255))
comp_inc = Image.alpha_composite(bg_inc, crop_inc).convert("RGB")
canvas_inc = Image.new("RGB", (1000, 1000), (0, 0, 0))
tw_inc = 910
th_inc = int(comp_inc.height * (tw_inc / comp_inc.width))
res_inc = comp_inc.resize((tw_inc, th_inc), Image.Resampling.LANCZOS)
canvas_inc.paste(res_inc, ((1000 - tw_inc) // 2, (1000 - th_inc) // 2))
canvas_inc.save(os.path.join(LOGOS_COLOR_DIR, "incorruptivel_color.jpg"), quality=96)
canvas_inc.save(os.path.join(LOGOS_COLOR_DIR, "incorruptivel_color.png"))
print("Saved official incorruptivel_color.jpg & .png")

# -------------------------------------------------------------------------
# 7. ALIENS DA BÍBLIA:
#    - Profile Logo: Enlarge cosmic blue vortex + silver infinity emblem into a 1:1 (1000x1000) full-bleed square
#      so there are ZERO black margins at top and bottom.
# -------------------------------------------------------------------------
aliens_src = os.path.join(LOGOS_COLOR_DIR, "aliens_color.jpg")
img_al = Image.open(aliens_src).convert("RGB")
w_a, h_a = img_al.size
# If it's horizontal (e.g. 600x348), let's take the central square (348x348) or slightly wider with mirrored cosmic nebula top/bottom!
# Wait: let's check how wide the infinity symbol is in aliens_color.jpg!
# The infinity symbol is in the center (~340px wide out of 600px).
# If we crop a width of 420px around the center (so the infinity symbol fills 82% of the width!)
# and extend top/bottom by 36px each with the cosmic blue vortex texture:
crop_wa = int(h_a * 1.16)  # ~404px wide out of 600px
if crop_wa > w_a:
    crop_wa = w_a
xa0 = (w_a - crop_wa) // 2
ca_crop = img_al.crop((xa0, 0, xa0 + crop_wa, h_a))
pad_ta = (crop_wa - h_a) // 2
pad_ba = crop_wa - h_a - pad_ta
sq_al = Image.new("RGB", (crop_wa, crop_wa))
if pad_ta > 0:
    top_a = ca_crop.crop((0, 4, crop_wa, 4 + pad_ta)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    bot_a = ca_crop.crop((0, h_a - 4 - pad_ba, crop_wa, h_a - 4)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    sq_al.paste(top_a, (0, 0))
    sq_al.paste(ca_crop, (0, pad_ta))
    sq_al.paste(bot_a, (0, pad_ta + h_a))
    arr_al = np.array(sq_al).astype(np.float32)
    blur_al = np.array(sq_al.filter(ImageFilter.GaussianBlur(radius=6))).astype(np.float32)
    for seam_y in [pad_ta, pad_ta + h_a]:
        for dy in range(-10, 11):
            if 0 <= seam_y + dy < crop_wa:
                wb = 1.0 - (abs(dy) / 11.0)
                arr_al[seam_y + dy] = arr_al[seam_y + dy] * (1.0 - 0.65 * wb) + blur_al[seam_y + dy] * (0.65 * wb)
    sq_al = Image.fromarray(np.clip(arr_al, 0, 255).astype(np.uint8))
else:
    sq_al = ca_crop
sq_al = sq_al.resize((1000, 1000), Image.Resampling.LANCZOS)
sq_al.save(os.path.join(LOGOS_COLOR_DIR, "aliens_color.jpg"), quality=96)
print("Saved full-bleed 1:1 aliens_color.jpg")

# Also print the DarkPlanner ingredient pack IDs
with open(r"C:\Users\rigob\.gemini\antigravity\brain\2dfe657c-4e76-4940-b591-8aa8444b03a8\.system_generated\steps\2068\output.txt", "r", encoding="utf-8") as f:
    packs = json.load(f)
for p in packs:
    print(f"PACK ID={p.get('id')} NAME={p.get('name')}")
