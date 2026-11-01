import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SITE_DIR = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA"
CANAIS_DIR = r"C:\PROJETOS\1-CANAIS"

BANNERS_OUT = os.path.join(SITE_DIR, "assets", "banners")
LOGOS_COLOR_OUT = os.path.join(SITE_DIR, "assets", "logos_color")
AUDIO_OUT = os.path.join(SITE_DIR, "assets", "audio")
SIGNS_DIR = os.path.join(SITE_DIR, "assets", "signs")

os.makedirs(BANNERS_OUT, exist_ok=True)
os.makedirs(LOGOS_COLOR_OUT, exist_ok=True)
os.makedirs(AUDIO_OUT, exist_ok=True)

# 1. Clean any faint rectangular alpha border on all 10 road signs so NO transparent box ever appears
for fname in sorted(os.listdir(SIGNS_DIR)):
    if not fname.endswith(".png"):
        continue
    fpath = os.path.join(SIGNS_DIR, fname)
    img = Image.open(fpath).convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    alpha = arr[:, :, 3]
    # Zero out any low-alpha halo (< 45) and feather cleanly
    alpha = np.where(alpha < 45, 0.0, alpha)
    # Also ensure outer 4px frame is 100% transparent so GPU texture clamping never draws a box border
    alpha[:4, :] = 0.0
    alpha[-4:, :] = 0.0
    alpha[:, :4] = 0.0
    alpha[:, -4:] = 0.0
    arr[:, :, 3] = alpha
    Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA").save(fpath, "PNG")
    print(f"[OK] Cleaned sign alpha border: {fname}")

# 2. Copy Official YouTube Banners & Colored Logos for the 10 Channels
def save_web_jpg(src_path, dst_path, target_w=1600, target_h=900):
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    target_ratio = target_w / target_h
    cur_ratio = w / h
    if cur_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    img.save(dst_path, "JPEG", quality=92)
    print(f"[OK] Saved banner: {os.path.basename(dst_path)}")

# Find accented folders dynamically
all_canal_dirs = {d: os.path.join(CANAIS_DIR, d) for d in os.listdir(CANAIS_DIR) if os.path.isdir(os.path.join(CANAIS_DIR, d))}
aguas_dir = next((v for k, v in all_canal_dirs.items() if "4-" in k), os.path.join(CANAIS_DIR, "4-AGUAS_DE_DESCANSO"))
rock_dir = next((v for k, v in all_canal_dirs.items() if "2-ROCK" in k), os.path.join(CANAIS_DIR, "2-ROCK_INCORRUPTIVEL"))

# Banner 1: Águas de Descanso (Official YouTube Banner with cabin & golden title)
aguas_banner_src = os.path.join(aguas_dir, "2_ASSETS", "WhatsApp Image 2026-09-10 at 22.45.57.jpeg")
if os.path.exists(aguas_banner_src):
    save_web_jpg(aguas_banner_src, os.path.join(BANNERS_OUT, "aguas_youtube_banner.jpg"))
aguas_logo_src = os.path.join(aguas_dir, "2_ASSETS", "WhatsApp Image 2026-09-10 at 22.45.58.jpeg")
if os.path.exists(aguas_logo_src):
    Image.open(aguas_logo_src).convert("RGBA").resize((500, 500), Image.Resampling.LANCZOS).save(os.path.join(LOGOS_COLOR_OUT, "aguas_color.png"))

# Banner 2: Sacronia (Official 3D carved logo on dark background)
sacronia_banner_src = os.path.join(SITE_DIR, "assets", "channels", "sacronia.jpg")
if os.path.exists(sacronia_banner_src):
    save_web_jpg(sacronia_banner_src, os.path.join(BANNERS_OUT, "sacronia_youtube_banner.jpg"))
sacronia_logo_src = os.path.join(CANAIS_DIR, "3-SACRONIA", "2_ASSETS", "IDENTIDADE_VISUAL", "logo_perfil.png")
if os.path.exists(sacronia_logo_src):
    Image.open(sacronia_logo_src).convert("RGBA").resize((500, 500), Image.Resampling.LANCZOS).save(os.path.join(LOGOS_COLOR_OUT, "sacronia_color.png"))

# Banner 3: Trono da Promessa (Official Vovô Nésio + Netos in armchair)
trono_banner_src = os.path.join(CANAIS_DIR, "7-TRONO_DA_PROMESSA", "01_APLICATIVO_TRONO_DA_PROMESSA_EBD", "2_ASSETS_UI_BOTOES", "banner_vovo_e_netos_oficial.jpg")
if os.path.exists(trono_banner_src):
    save_web_jpg(trono_banner_src, os.path.join(BANNERS_OUT, "trono_youtube_banner.jpg"))
trono_logo_src = os.path.join(CANAIS_DIR, "7-TRONO_DA_PROMESSA", "2_ASSETS", "IDENTIDADE_VISUAL", "[Logo_Oficial_SemFundo].png")
if os.path.exists(trono_logo_src):
    Image.open(trono_logo_src).convert("RGBA").save(os.path.join(LOGOS_COLOR_OUT, "trono_color.png"))

# Banner 4: Aliens da Bíblia (Official 4 witnesses + vortex banner)
aliens_banner_src = os.path.join(CANAIS_DIR, "5-ALIENS_DA_BIBLIA", "aliens_youtube_banner_chars.jpg")
if os.path.exists(aliens_banner_src):
    save_web_jpg(aliens_banner_src, os.path.join(BANNERS_OUT, "aliens_youtube_banner.jpg"))
aliens_logo_src = os.path.join(CANAIS_DIR, "5-ALIENS_DA_BIBLIA", "Silver_symbol_with_cosmic_vortex_20261009123644.jpg")
if os.path.exists(aliens_logo_src):
    save_web_jpg(aliens_logo_src, os.path.join(LOGOS_COLOR_OUT, "aliens_color.jpg"), 600, 360)

# Banner 5: Neon Asher (Official Neon Asher rain & lightning banner)
neon_banner_src = os.path.join(CANAIS_DIR, "10-NEON_ASHER", "2_ASSETS", "[Logo Oficial].jpeg")
if os.path.exists(neon_banner_src):
    save_web_jpg(neon_banner_src, os.path.join(BANNERS_OUT, "neon_youtube_banner.jpg"))
neon_logo_src = os.path.join(CANAIS_DIR, "10-NEON_ASHER", "2_ASSETS", "LOGO II.jpeg")
if os.path.exists(neon_logo_src):
    save_web_jpg(neon_logo_src, os.path.join(LOGOS_COLOR_OUT, "neon_color.jpg"), 600, 360)

# Banner 6: Patinhas & Canções (Official YouTube Banner + Official Golden Seal Logo)
patinhas_banner_src = os.path.join(CANAIS_DIR, "8-PATINHAS_E_CANCOES", "2_ASSETS", "IDENTIDADE_VISUAL", "[Banner_YouTube_Patinhas_Maos_Acolhedoras_2560x1440].jpg")
if os.path.exists(patinhas_banner_src):
    save_web_jpg(patinhas_banner_src, os.path.join(BANNERS_OUT, "patinhas_youtube_banner.jpg"))
patinhas_logo_src = os.path.join(CANAIS_DIR, "8-PATINHAS_E_CANCOES", "2_ASSETS", "IDENTIDADE_VISUAL", "[Logo_Selo_Patinhas_E_Cancoes].png")
if os.path.exists(patinhas_logo_src):
    Image.open(patinhas_logo_src).convert("RGBA").save(os.path.join(LOGOS_COLOR_OUT, "patinhas_color.png"))

# Banner 7: Rock Incorruptível (Official Congresso stage lights banner)
rock_banner_src = os.path.join(rock_dir, "2_ASSETS", "AMBIENTES_3D", "ThumbCenario_Ep01B_Incomodar_3D.jpg")
if os.path.exists(rock_banner_src):
    save_web_jpg(rock_banner_src, os.path.join(BANNERS_OUT, "rock_youtube_banner.jpg"))

# Banner 8: Incorruptível (Official Praça dos Três Poderes Crepúsculo 3D)
inc_banner_src = os.path.join(rock_dir, "2_ASSETS", "AMBIENTES_3D", "[PracaDosTresPoderes_Crepusculo_3D].jpg")
if os.path.exists(inc_banner_src):
    save_web_jpg(inc_banner_src, os.path.join(BANNERS_OUT, "incorruptivel_youtube_banner.jpg"))

# Banner 9: Iago Cordeiro (Compose official YouTube banner with warm acoustic worship room + Lion & Guitar crest)
iago_bg_src = os.path.join(SITE_DIR, "assets", "ui", "moment_adoracao.jpg")
iago_pb_logo = os.path.join(SITE_DIR, "assets", "logos", "iago_cordeiro_pb.png")
if os.path.exists(iago_bg_src) and os.path.exists(iago_pb_logo):
    bg = Image.open(iago_bg_src).convert("RGBA").resize((1600, 900), Image.Resampling.LANCZOS)
    # Darken center slightly for crisp golden-amber logo readability
    overlay = Image.new("RGBA", (1600, 900), (14, 9, 4, 115))
    bg = Image.alpha_composite(bg, overlay)
    lg = Image.open(iago_pb_logo).convert("RGBA")
    # Tint white logo into warm golden-amber
    lg_arr = np.array(lg, dtype=np.float32)
    lg_arr[:, :, 0] = 252  # R
    lg_arr[:, :, 1] = 211  # G
    lg_arr[:, :, 2] = 105  # B
    lg_gold = Image.fromarray(lg_arr.astype(np.uint8), "RGBA")
    lg_gold_resized = lg_gold.resize((900, 338), Image.Resampling.LANCZOS)
    # Save colored logo
    lg_gold_resized.save(os.path.join(LOGOS_COLOR_OUT, "iago_color.png"), "PNG")
    bg.paste(lg_gold_resized, ((1600 - 900) // 2, (900 - 338) // 2), lg_gold_resized)
    bg.convert("RGB").save(os.path.join(BANNERS_OUT, "iago_youtube_banner.jpg"), "JPEG", quality=92)
    print("[OK] Saved banner & colored logo: iago_youtube_banner.jpg")

# Banner 10: Aquário dos Felinos (Compose official banner with the 3D cats of Aquário dos Felinos + colored logo)
aquario_bg_src = os.path.join(SITE_DIR, "assets", "ui", "moment_kids.jpg")
aquario_pb_logo = os.path.join(SITE_DIR, "assets", "logos", "aquario_dos_felinos_pb.png")
if os.path.exists(aquario_bg_src) and os.path.exists(aquario_pb_logo):
    bg = Image.open(aquario_bg_src).convert("RGBA").resize((1600, 900), Image.Resampling.LANCZOS)
    lg = Image.open(aquario_pb_logo).convert("RGBA")
    lg_arr = np.array(lg, dtype=np.float32)
    lg_arr[:, :, 0] = 103  # R (cyan-gold glow)
    lg_arr[:, :, 1] = 232  # G
    lg_arr[:, :, 2] = 249  # B
    lg_color = Image.fromarray(lg_arr.astype(np.uint8), "RGBA").resize((860, 322), Image.Resampling.LANCZOS)
    lg_color.save(os.path.join(LOGOS_COLOR_OUT, "aquario_color.png"), "PNG")
    bg.convert("RGB").save(os.path.join(BANNERS_OUT, "aquario_youtube_banner.jpg"), "JPEG", quality=92)
    print("[OK] Saved banner & colored logo: aquario_youtube_banner.jpg")

# 3. Copy extra real MP3 tracks per music channel so clicking "Ouvir Agora" on a channel plays multiple songs of THAT channel!
EXTRA_AUDIO_COPIES = [
    # Rock Incorruptível
    (os.path.join(rock_dir, "3_MUSICAS", "00_ESTOQUE_E_PRODUCAO", "Episodio_01B_Vai_Incomodar", "Vai Incomodar.mp3"), "rock_vai_incomodar.mp3"),
    (os.path.join(rock_dir, "3_MUSICAS", "00_ESTOQUE_E_PRODUCAO", "00_REDES_SOCIAIS", "6_POSTADOS", "Episodio_04_A_Fabrica_de_Promessas", "Episodio_04_A_Fabrica_de_Promessas.mp3"), "rock_fabrica_de_promessas.mp3"),
    # Sacronia
    (os.path.join(CANAIS_DIR, "3-SACRONIA", "3_MUSICAS", "Mais Forte que o Trono.mp3"), "sacronia_mais_forte_que_o_trono.mp3"),
    (os.path.join(CANAIS_DIR, "3-SACRONIA", "3_MUSICAS", "Quando o Mar se Levanta.mp3"), "sacronia_quando_o_mar_se_levanta.mp3"),
    (os.path.join(CANAIS_DIR, "3-SACRONIA", "3_MUSICAS", "O Ultimo Dia de um Rei.mp3"), "sacronia_ultimo_dia_de_um_rei.mp3"),
    # Neon Asher
    (os.path.join(CANAIS_DIR, "10-NEON_ASHER", "3_MUSICAS", "Episodio_13_One_More_Sign", "Episodio_03_Violins_in_the_Rain", "Violins in the Rain.mp3"), "neon_violins_in_the_rain.mp3"),
    (os.path.join(CANAIS_DIR, "10-NEON_ASHER", "3_MUSICAS", "Episodio_11_Ashes_of_Your_Name", "Ashes of Your Name.mp3"), "neon_ashes_of_your_name.mp3"),
    (os.path.join(CANAIS_DIR, "10-NEON_ASHER", "3_MUSICAS", "Episodio_12_Broken_Vow", "Broken Vow.mp3"), "neon_broken_vow.mp3"),
    (os.path.join(CANAIS_DIR, "10-NEON_ASHER", "3_MUSICAS", "Episodio_13_One_More_Sign", "Episodio_05_After_the_Lights_Go_Out", "After the Lights Go Out.mp3"), "neon_after_the_lights.mp3"),
    # Iago Cordeiro
    (os.path.join(CANAIS_DIR, "9-IAGO_CORDEIRO", "3_MUSICAS", "Rei dos Reis", "Rei dos Reis.mp3"), "iago_rei_dos_reis.mp3"),
    (os.path.join(CANAIS_DIR, "9-IAGO_CORDEIRO", "3_MUSICAS", "Paz Que Vem do Alto", "Paz Que Vem do Alto.mp3"), "iago_paz_que_vem_do_alto.mp3"),
    (os.path.join(CANAIS_DIR, "9-IAGO_CORDEIRO", "3_MUSICAS", "A Rocha da Salvaçao.mp3"), "iago_rocha_da_salvacao.mp3"),
    # Patinhas & Canções
    (os.path.join(CANAIS_DIR, "8-PATINHAS_E_CANCOES", "3_MUSICAS", "1_ESTOQUE E PRODUÇAO", "06_POSTADOS", "Episodio_4_Agora Eu Vou Ficar", "diversos", "Agora Eu Vou Ficar.mp3"), "patinhas_agora_eu_vou_ficar.mp3"),
    (os.path.join(CANAIS_DIR, "8-PATINHAS_E_CANCOES", "3_MUSICAS", "1_ESTOQUE E PRODUÇAO", "06_POSTADOS", "Episodio_5_A Ultima Caminhada", "diversos", "A Ultima Caminhada.mp3"), "patinhas_ultima_caminhada.mp3"),
    (os.path.join(CANAIS_DIR, "8-PATINHAS_E_CANCOES", "3_MUSICAS", "1_ESTOQUE E PRODUÇAO", "06_POSTADOS", "Episodio_6_A Gatinha no Telhado", "diversos", "A Gatinha no Telhado.mp3"), "patinhas_gatinha_no_telhado.mp3"),
]

# Also handle encoding variations in folder names for Patinhas & Iago
for src, dst_name in EXTRA_AUDIO_COPIES:
    dst = os.path.join(AUDIO_OUT, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"[OK] Copied audio: {dst_name}")
    else:
        # Try glob search by filename inside channel folder
        fname = os.path.basename(src)
        ch_root = src.split("\\3_MUSICAS")[0]
        found = False
        if os.path.exists(ch_root):
            for root, _, files in os.walk(ch_root):
                for f in files:
                    if f.lower() == fname.lower() or ( dst_name.split("_")[1] in f.lower() and f.endswith(".mp3") ):
                        shutil.copy2(os.path.join(root, f), dst)
                        print(f"[OK] Copied audio (matched): {dst_name} <- {f}")
                        found = True
                        break
                if found:
                    break
        if not found:
            print(f"[WARN] Audio not found: {src}")

print("All real channel assets synchronized successfully!")
