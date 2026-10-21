#!/usr/bin/env python3
# Renderer una-tantum del video di presentazione (60s, 1080x1920, 10fps).
# Motivo dell'uso di Python: PIL e' l'unico renderer di immagini disponibile qui;
# non fa parte del prodotto, e' uno strumento di produzione usa-e-getta.
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 10
BG      = (11, 14, 20)
PANEL   = (20, 24, 34)
TEXT    = (230, 233, 239)
MUTED   = (138, 147, 166)
ACCENT  = (124, 92, 255)
GREEN   = (110, 231, 168)
FONT    = "/system/fonts/DroidSansMono.ttf"

def f(size): return ImageFont.truetype(FONT, size)

def new_frame():
    img = Image.new("RGB", (W, H), BG)
    return img

def center(d, y, text, font, fill=TEXT):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def panel(d, x, y, w, h, r=28):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=PANEL, outline=(44, 50, 66), width=2)

def progress(img_bar, t, total, color=ACCENT):
    bar = Image.new("RGB", (W, 8), (26, 30, 42))
    bd = ImageDraw.Draw(bar)
    bd.rectangle([0, 0, int(W * min(t / total, 1.0)), 8], fill=color)
    img_bar.paste(bar, (0, H - 8))

def scene_title():
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 700, "SigmaTek X", f(96), TEXT)
    d.line([(W/2 - 190, 830), (W/2 + 190, 830)], fill=ACCENT, width=6)
    center(d, 880, "Sistemi AI costruiti", f(46), TEXT)
    center(d, 940, "su un telefono.", f(46), TEXT)
    center(d, 1040, "Nessun cloud. Nessuna emulazione.", f(32), MUTED)
    return img

def scene_pei(n_lines):
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 300, "P.E.I.", f(64), TEXT)
    center(d, 380, "memoria per agenti AI", f(34), MUTED)
    x, y, w, h = 70, 520, W - 140, 520
    panel(d, x, y, w, h)
    fm = f(30)
    lines = ["$ ./bin/peimem stato", "", "db: ~/.local/share/iqvibe/...",
             "embedder: semantico", "          (all-MiniLM-L6-v2)", "integrità: OK"]
    for i, ln in enumerate(lines[:n_lines]):
        col = GREEN if ln.startswith("integrità") else TEXT if ln.startswith("$") else MUTED
        d.text((x + 40, y + 50 + i * 62), ln, font=fm, fill=col)
    center(d, 1180, "La memoria controlla sé stessa:", f(34), TEXT)
    center(d, 1238, "se qualcuno la manomette, lo dice.", f(34), MUTED)
    return img

def scene_rekor():
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 320, "Prova pubblica,", f(56), TEXT)
    center(d, 390, "senza mostrare codice", f(56), ACCENT)
    x, y, w, h = 70, 560, W - 140, 560
    panel(d, x, y, w, h)
    fm = f(30)
    d.text((x + 40, y + 60), "rekor.sigstore.dev", font=fm, fill=MUTED)
    d.text((x + 40, y + 110), "/…/108e9186…aaac6a", font=fm, fill=MUTED)
    d.text((x + 40, y + 220), "HTTP 200", font=f(76), fill=GREEN)
    d.text((x + 40, y + 340), "hash SHA-512", font=fm, fill=TEXT)
    d.text((x + 40, y + 390), "firma Ed25519", font=fm, fill=TEXT)
    d.text((x + 40, y + 440), "16/10/2026", font=fm, fill=TEXT)
    center(d, 1230, "Chiunque può verificarlo.", f(34), TEXT)
    center(d, 1288, "Non contiene una riga di codice.", f(34), MUTED)
    return img

def scene_code():
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 230, "Estratto reale", f(52), TEXT)
    center(d, 296, "dettagli oscurati", f(34), ACCENT)
    x, y, w, h = 60, 400, W - 120, 900
    panel(d, x, y, w, h)
    code = [
        "pub fn hash_leaf(item: &[u8]) -> [u8; 32] {",
        "    let mut h = Sha256::new();",
        "    h.update(b\"....anchor.leaf.v1\");",
        "    h.update((item.len() as u64).to_le_bytes());",
        "    h.update(item);",
        "    h.finalize().into()",
        "}",
        "",
        "fn hash_node(l: &[u8; 32], r: &[u8; 32]) -> [u8; 32] {",
        "    let mut h = Sha256::new();",
        "    h.update(b\"....anchor.node.v1\");",
        "    h.update(l);",
        "    h.update(r);",
        "    h.finalize().into()",
        "}",
    ]
    fm = f(27)
    layer = Image.new("RGB", (w - 80, len(code) * 52 + 20), PANEL)
    ld = ImageDraw.Draw(layer)
    for i, ln in enumerate(code):
        ld.text((0, 10 + i * 52), ln, font=fm, fill=(214, 219, 230))
    sharp_from, sharp_to = 1, 5          # righe leggibili
    top, bot = 10 + sharp_from * 52, 10 + sharp_to * 52
    blurred = layer.filter(ImageFilter.GaussianBlur(7))
    out = blurred.copy()
    out.paste(layer.crop((0, top, w - 80, bot)), (0, top))
    img.paste(out, (x + 40, y + 40))
    d.rectangle([x + 12, y + top + 40, x + 18, y + bot + 40], fill=ACCENT)
    center(d, 1380, "Il resto è privato.", f(36), TEXT)
    center(d, 1438, "Si vede il metodo, non il progetto.", f(32), MUTED)
    return img

def scene_numbers():
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 300, "Numeri, non aggettivi", f(52), TEXT)
    rows = [("465", "test automatici in 89 suite"),
            ("196/235", "task chiusi con verifica eseguita"),
            ("9", "crate Rust nel workspace")]
    y = 520
    for big, small in rows:
        panel(d, 70, y, W - 140, 250)
        d.text((120, y + 45), big, font=f(92), fill=ACCENT)
        d.text((120, y + 160), small, font=f(30), fill=MUTED)
        y += 300
    center(d, 1470, "Ogni numero viene da un'esecuzione.", f(32), MUTED)
    return img

def scene_nexqx():
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 340, "NexQX", f(72), TEXT)
    center(d, 430, "linguaggio proprio", f(34), MUTED)
    chain = "lessico → sintassi → tipi → MIR"
    center(d, 620, chain, f(34), TEXT)
    x, y, w, h = 90, 760, W - 180, 380
    panel(d, x, y, w, h)
    d.text((x + 40, y + 50), "$ suite pipeline completa", font=f(28), fill=MUTED)
    d.text((x + 40, y + 140), "TUTTI I CONTROLLI", font=f(46), fill=GREEN)
    d.text((x + 40, y + 205), "CORRETTI", font=f(46), fill=GREEN)
    d.text((x + 40, y + 300), "da sorgente a esecuzione, non a pezzi", font=f(26), fill=MUTED)
    center(d, 1290, "Un errore di sintassi non passa.", f(32), TEXT)
    return img

def scene_end():
    img = new_frame(); d = ImageDraw.Draw(img)
    center(d, 760, "Demo su richiesta.", f(64), TEXT)
    center(d, 880, "Nessun sorgente inviato.", f(40), ACCENT)
    d.line([(W/2 - 160, 990), (W/2 + 160, 990)], fill=(44, 50, 66), width=4)
    center(d, 1050, "github.com/ANGEL-HoG", f(34), MUTED)
    return img

# --- montaggio -------------------------------------------------------------
scenes = [
    (scene_title(),            5.0),
    (scene_pei(2),             3.4), (scene_pei(4), 3.4), (scene_pei(6), 3.4),
    (scene_rekor(),            9.0),
    (scene_code(),            12.0),
    (scene_numbers(),         10.0),
    (scene_nexqx(),            8.0),
    (scene_end(),              6.0),
]
FADE = 0.4

def frames():
    total = sum(d for _, d in scenes)
    t = 0.0
    for idx, (img, dur) in enumerate(scenes):
        n = max(1, int(round(dur * FPS)))
        nxt = scenes[idx + 1][0] if idx + 1 < len(scenes) else None
        for i in range(n):
            t += 1.0 / FPS
            base = img.copy()
            progress(base, t, total)
            if nxt is not None and i >= n - int(FADE * FPS):
                a = (i - (n - int(FADE * FPS)) + 1) / float(int(FADE * FPS))
                nf = nxt.copy(); progress(nf, t, total)
                base = Image.blend(base, nf, min(a, 1.0))
            yield base.tobytes()

out = sys.argv[1]
cmd = ["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
       "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
       "-pix_fmt", "yuv420p", "-movflags", "+faststart", out]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for buf in frames():
    p.stdin.write(buf)
p.stdin.close()
p.wait()
print("ok" if p.returncode == 0 else f"errore {p.returncode}")
