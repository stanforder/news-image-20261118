#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news image (1024x1024).

Flat editorial-poster style, drawn with Pillow only at build time.
The submitted program (main.py) does NOT run this file: it copies the
finished entry.png, so the grader (stdlib only, no network) can run it.
News facts, all first reported / happening on Wed 18 Nov 2026:
- Xi Jinping meets Vladimir Putin in Shenzhen (APEC); trilateral with
  Donald Trump set for Thursday 19 Nov.
- US-Iran exchange fire in the Gulf: Iranian drones target US sites in
  Kuwait/Bahrain, US strikes a missile site on Qeshm Island, 5 tankers sunk.
- Ukraine launches a record 1,441-drone assault; Kerch (Crimea) bridge span falls.
- Gaza's 4th winter: WHO puts 950,000 displaced Palestinians in flood-prone ground.
- Nvidia revenue doubles to $115.8bn; board rules out reinstating Jensen Huang.
- Cyclone Akvan hits Odisha (evacuations); COP31 in Antalya deadlocked.
- Footer: Quad meets in Manila; US Senate Democrats 56-44 (Peltola wins Alaska);
  Yemen: 64 children killed since 3 Sep.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

NAVY = (15, 42, 68)
NAVY2 = (22, 58, 90)
INK = (17, 24, 39)
CREAM = (251, 246, 233)
PAPER = (255, 252, 242)
RED = (193, 39, 45)
RED2 = (166, 28, 35)
GOLD = (217, 164, 65)
TEAL = (14, 122, 107)
SKY = (178, 216, 238)
SKY2 = (135, 190, 220)
ORANGE = (232, 116, 28)
DARK = (32, 24, 18)
GREY = (90, 100, 112)

BOLD_PATHS = [
    "/usr/share/fonts/truetype/noto/NotoSans-CondensedBold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
REG_PATHS = [
    "/usr/share/fonts/truetype/noto/NotoSans-Condensed.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def font(size, bold=True):
    for p in (BOLD_PATHS if bold else REG_PATHS):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def fit(text, max_w, start, bold=True, min_size=10):
    size = start
    while size > min_size:
        f = font(size, bold)
        if f.getlength(text) <= max_w:
            return f
        size -= 1
    return font(min_size, bold)


def text_c(d, cx, y, s, f, fill, anchor="ma"):
    d.text((cx, y), s, font=f, fill=fill, anchor=anchor)


def text_l(d, x, y, s, f, fill):
    d.text((x, y), s, font=f, fill=fill, anchor="la")


def wrap(d, x, y, max_w, lines, size, fill, bold=True, leading=None):
    f = font(size, bold)
    lh = leading or int(size * 1.15)
    for i, line in enumerate(lines):
        d.text((x, y + i * lh), line, font=f, fill=fill, anchor="la")
    return y + len(lines) * lh


def flag_china(d, x, y, w=56, h=36):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    d.text((x + 6, y + 4), "*", font=font(20), fill=(255, 222, 0))
    for sx, sy in [(34, 6), (42, 12), (42, 22), (34, 28)]:
        d.text((x + sx, y + sy), "*", font=font(11), fill=(255, 222, 0))


def flag_russia(d, x, y, w=56, h=36):
    d.rectangle([x, y, x + w, y + 12], fill=(255, 255, 255))
    d.rectangle([x, y + 12, x + w, y + 24], fill=(0, 57, 166))
    d.rectangle([x, y + 24, x + w, y + h], fill=(213, 0, 50))


def flag_usa(d, x, y, w=56, h=36):
    for i in range(7):
        d.rectangle([x, y + i * 5, x + w, y + (i + 1) * 5],
                    fill=(178, 34, 52) if i % 2 == 0 else (255, 255, 255))
    d.rectangle([x, y, x + 24, y + 20], fill=(60, 59, 110))
    for sx in (4, 12, 20):
        for sy in (4, 12):
            d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3], fill=(255, 255, 255))


def person(d, cx, base_y, suit, skin=(232, 190, 150), hair=(40, 30, 25)):
    # head, shoulders, simple flat figure (no face detail: clean at small size)
    d.ellipse([cx - 26, base_y - 118, cx + 26, base_y - 66], fill=skin)
    d.pieslice([cx - 26, base_y - 118, cx + 26, base_y - 82], 180, 360, fill=hair)
    d.polygon([(cx - 52, base_y), (cx - 38, base_y - 68), (cx + 38, base_y - 68),
               (cx + 52, base_y)], fill=suit)
    d.polygon([(cx - 10, base_y - 68), (cx, base_y - 44), (cx + 10, base_y - 68)],
              fill=(255, 255, 255))
    d.polygon([(cx - 5, base_y - 66), (cx + 5, base_y - 66), (cx, base_y - 46)],
              fill=RED)


def drone(d, cx, cy, s=1.0, fill=INK):
    d.line([cx - 22 * s, cy - 12 * s, cx + 22 * s, cy + 12 * s], fill=fill, width=3)
    d.line([cx - 22 * s, cy + 12 * s, cx + 22 * s, cy - 12 * s], fill=fill, width=3)
    d.ellipse([cx - 9 * s, cy - 7 * s, cx + 9 * s, cy + 7 * s], fill=fill)
    for dx, dy in [(-22, -12), (22, -12), (-22, 12), (22, 12)]:
        d.ellipse([cx + dx * s - 6, cy + dy * s - 3, cx + dx * s + 6, cy + dy * s + 3],
                  outline=fill, width=2)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=NAVY, width=10)

    # ---- Masthead ----
    d.rectangle([10, 10, 1013, 118], fill=NAVY)
    text_c(d, 512, 22, "THE WORLD IN ONE DAY", font(24), GOLD)
    text_c(d, 512, 48, "WEDNESDAY 18 NOVEMBER 2026",
           fit("WEDNESDAY 18 NOVEMBER 2026", 960, 46), (255, 255, 255))

    # ---- Headline ----
    text_c(d, 512, 122, "SUMMITS AND STRIKES",
           fit("SUMMITS AND STRIKES", 980, 60), INK)
    text_c(d, 512, 190, "Xi meets Putin in Shenzhen  —  Trump joins them Thursday",
           fit("Xi meets Putin in Shenzhen  —  Trump joins them Thursday", 960, 24, bold=False),
           (70, 70, 70))

    # ================= HERO: SUMMIT (left) =================
    hx, hy, hw, hh = 24, 222, 608, 306
    d.rectangle([hx, hy, hx + hw, hy + hh], fill=SKY)
    # Shenzhen skyline
    for bx, bw, bh in [(0, 70, 90), (70, 46, 140), (116, 80, 70), (196, 52, 160),
                       (248, 70, 100), (318, 44, 150), (362, 80, 80), (442, 54, 170),
                       (496, 60, 110), (556, 52, 130)]:
        d.rectangle([hx + bx, hy + hh - 118 - bh, hx + bx + bw, hy + hh - 118],
                    fill=NAVY2)
        for wy in range(hy + hh - 118 - bh + 10, hy + hh - 128, 22):
            for wx in range(hx + bx + 8, hx + bx + bw - 6, 16):
                d.rectangle([wx, wy, wx + 6, wy + 8], fill=GOLD)
    d.rectangle([hx, hy + hh - 118, hx + hw, hy + hh], fill=(214, 232, 240))
    # flags on poles
    for fx, flag in [(hx + 52, flag_china), (hx + 276, flag_russia), (hx + 500, flag_usa)]:
        d.line([fx + 28, hy + 22, fx + 28, hy + 78], fill=INK, width=4)
        flag(d, fx, hy + 22)
    # two leaders at the summit: full torsos visible above the caption band
    person(d, hx + 210, hy + hh - 62, NAVY, hair=(30, 30, 30))
    person(d, hx + 400, hy + hh - 62, (90, 30, 30), skin=(240, 205, 170), hair=(210, 210, 210))
    d.rectangle([hx, hy + hh - 62, hx + hw, hy + hh], fill=NAVY)
    text_c(d, hx + hw // 2, hy + hh - 56, "XI MEETS PUTIN IN SHENZHEN",
           fit("XI MEETS PUTIN IN SHENZHEN", hw - 24, 34), (255, 255, 255))
    text_c(d, hx + hw // 2, hy + hh - 24, "APEC  •  TRILATERAL WITH TRUMP SET FOR THURSDAY",
           fit("APEC  •  TRILATERAL WITH TRUMP SET FOR THURSDAY", hw - 24, 20, bold=False),
           GOLD)

    # ================= HERO: GULF (right) =================
    gx, gy, gw, gh = 640, 222, 360, 306
    d.rectangle([gx, gy, gx + gw, gy + gh], fill=(43, 26, 18))
    # explosion
    for r, col in [(86, ORANGE), (62, (245, 158, 40)), (38, (255, 214, 90))]:
        d.ellipse([gx + 180 - r, gy + 96 - r, gx + 180 + r, gy + 96 + r], fill=col)
    d.polygon([(gx + 180, gy + 6), (gx + 200, gy + 60), (gx + 246, gy + 40),
               (gx + 214, gy + 92), (gx + 262, gy + 110), (gx + 206, gy + 128),
               (gx + 220, gy + 178), (gx + 180, gy + 140), (gx + 140, gy + 178),
               (gx + 154, gy + 128), (gx + 98, gy + 110), (gx + 146, gy + 92),
               (gx + 114, gy + 40), (gx + 160, gy + 60)], fill=(255, 230, 140))
    drone(d, gx + 62, gy + 52, 0.9, fill=(255, 255, 255))
    drone(d, gx + 302, gy + 44, 0.7, fill=(220, 220, 220))
    # tanker + sea
    d.rectangle([gx, gy + 218, gx + gw, gy + gh], fill=(18, 60, 90))
    d.polygon([(gx + 30, gy + 218), (gx + 330, gy + 218), (gx + 300, gy + 252),
               (gx + 60, gy + 252)], fill=(20, 20, 20))
    d.rectangle([gx + 150, gy + 188, gx + 210, gy + 218], fill=(200, 60, 40))
    for wx in range(gx + 12, gx + gw - 12, 34):
        d.arc([wx, gy + 262, wx + 26, gy + 282], 0, 180, fill=(255, 255, 255), width=3)
    d.rectangle([gx, gy, gx + gw, gy + 44], fill=RED)
    text_c(d, gx + gw // 2, gy + 6, "GULF IN FLAMES",
           fit("GULF IN FLAMES", gw - 20, 32), (255, 255, 255))
    d.rectangle([gx, gy + gh - 62, gx + gw, gy + gh], fill=(0, 0, 0))
    text_c(d, gx + gw // 2, gy + gh - 56, "U.S.–IRAN EXCHANGE FIRE",
           fit("U.S.–IRAN EXCHANGE FIRE", gw - 16, 24), (255, 255, 255))
    text_c(d, gx + gw // 2, gy + gh - 28, "Drones at Gulf bases  •  U.S. hits Qeshm",
           fit("Drones at Gulf bases  •  U.S. hits Qeshm", gw - 16, 18, bold=False),
           (255, 200, 150))

    # ================= GRID: 4 panels =================
    panels = [
        # (x, y, label, label_bg, title_lines, sub, small, kind)
        (24, 534, "UKRAINE", RED, ["1,441 DRONES"], "KERCH BRIDGE HIT",
         "Record drone assault; a bridge span falls", "bridge"),
        (512, 534, "GAZA", TEAL, ["950,000 IN", "FLOOD ZONE"], "A 4TH WINTER IN GAZA",
         "Cold deaths feared as rain floods tents", "gaza"),
        (24, 738, "TECH  •  MARKETS", (30, 90, 50), ["$115.8 BN"], "NVIDIA REVENUE DOUBLES",
         "Board rules out bringing Huang back", "chip"),
        (512, 738, "CLIMATE", (40, 90, 160), ["CYCLONE AKVAN"], "ODISHA EVACUATES",
         "COP31 deadlocked over fossil fuels", "storm"),
    ]
    pw, ph = 488, 196
    for (x, y, label, lbg, titles, sub, small, kind) in panels:
        d.rectangle([x, y, x + pw, y + ph], fill=PAPER, outline=INK, width=3)
        d.rectangle([x, y, x + pw, y + 34], fill=lbg)
        text_l(d, x + 12, y + 5, label, fit(label, pw - 24, 24), (255, 255, 255))
        ix, iy, iw, ih = x + 12, y + 46, 150, 138
        tx = x + 176
        if kind == "bridge":
            d.rectangle([ix, iy, ix + iw, iy + ih], fill=SKY2)
            d.rectangle([ix, iy + 96, ix + iw, iy + ih], fill=(30, 90, 140))
            d.rectangle([ix + 8, iy + 58, ix + 58, iy + 70], fill=INK)
            d.rectangle([ix + 94, iy + 58, ix + 142, iy + 70], fill=INK)
            d.polygon([(ix + 58, iy + 58), (ix + 76, iy + 96), (ix + 94, iy + 58)],
                      fill=INK)
            d.line([ix + 20, iy + 58, ix + 20, iy + 30], fill=INK, width=3)
            d.line([ix + 130, iy + 58, ix + 130, iy + 30], fill=INK, width=3)
            drone(d, ix + 40, iy + 26, 0.55)
            drone(d, ix + 112, iy + 18, 0.45)
        elif kind == "gaza":
            d.rectangle([ix, iy, ix + iw, iy + ih], fill=(120, 140, 160))
            for rx in range(ix + 8, ix + iw, 26):
                d.line([rx, iy + 6, rx - 8, iy + 30], fill=(200, 220, 240), width=3)
            d.rectangle([ix, iy + 96, ix + iw, iy + ih], fill=(60, 110, 150))
            for tx0 in (ix + 14, ix + 78):
                d.polygon([(tx0, iy + 96), (tx0 + 26, iy + 58), (tx0 + 52, iy + 96)],
                          fill=(240, 230, 200), outline=INK)
            d.ellipse([ix + 108, iy + 18, ix + 138, iy + 48], fill=(255, 220, 120))
        elif kind == "chip":
            d.rectangle([ix, iy, ix + iw, iy + ih], fill=(16, 40, 26))
            d.rectangle([ix + 38, iy + 34, ix + 112, iy + 104], fill=(22, 110, 70),
                        outline=GOLD, width=3)
            d.text((ix + 58, iy + 52), "AI", font=font(34), fill=(255, 255, 255))
            for px in range(ix + 48, ix + 108, 16):
                d.line([px, iy + 22, px, iy + 34], fill=GOLD, width=3)
                d.line([px, iy + 104, px, iy + 116], fill=GOLD, width=3)
            d.line([ix + 16, iy + 118, ix + 60, iy + 118, ix + 86, iy + 96, ix + 134, iy + 96],
                   fill=(120, 255, 160), width=4)
            d.polygon([(ix + 122, iy + 88), (ix + 138, iy + 96), (ix + 122, iy + 104)],
                      fill=(120, 255, 160))
        else:  # storm
            d.rectangle([ix, iy, ix + iw, iy + ih], fill=(28, 70, 90))
            for r in (58, 42, 26):
                d.arc([ix + 75 - r, iy + 62 - r, ix + 75 + r, iy + 62 + r],
                      200, 140, fill=(255, 255, 255), width=5)
            d.line([ix + 20, iy + 122, ix + 34, iy + 96], fill=(90, 60, 30), width=6)
            for lx, ly in [(34, 84), (52, 78), (18, 92), (48, 92)]:
                d.line([ix + lx, iy + ly, ix + lx - 14, iy + ly + 10],
                       fill=(40, 160, 90), width=5)
            for rx in range(ix + 90, ix + iw, 22):
                d.line([rx, iy + 100, rx - 6, iy + 122], fill=(180, 220, 240), width=3)
        ty = y + 46
        for t in titles:
            f = fit(t, pw - 188, 38)
            d.text((tx, ty), t, font=f, fill=INK, anchor="la")
            ty += 42
        d.text((tx, ty + 2), sub, font=fit(sub, pw - 188, 23), fill=RED, anchor="la")
        d.text((tx, ty + 32), small, font=fit(small, pw - 188, 18, bold=False),
               fill=(70, 70, 70), anchor="la")

    # ---- Footer ticker ----
    d.rectangle([10, 942, 1013, 1013], fill=NAVY)
    text_c(d, 512, 960, "QUAD MEETS IN MANILA  •  U.S. SENATE: DEMOCRATS 56–44  •  YEMEN: 64 CHILDREN KILLED",
           fit("QUAD MEETS IN MANILA  •  U.S. SENATE: DEMOCRATS 56–44  •  YEMEN: 64 CHILDREN KILLED",
               980, 24), (255, 255, 255))
    text_c(d, 512, 988, "Sources: AP / AFP / Reuters / UN News  •  18 November 2026",
           font(16, bold=False), (190, 200, 210))

    img.save(OUT, "PNG", optimize=True)
    print(OUT, os.path.getsize(OUT), "bytes", img.size)


if __name__ == "__main__":
    main()
