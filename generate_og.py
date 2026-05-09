from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG = "#f7f8fa"
INK = "#232324"
SOFT = "#6b6b70"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

AVENIR = "/System/Library/Fonts/Avenir Next.ttc"

eyebrow = ImageFont.truetype(AVENIR, 22, index=5)   # Medium
title_f = ImageFont.truetype(AVENIR, 82, index=2)   # Demi Bold
sub_f   = ImageFont.truetype(AVENIR, 26, index=7)   # Regular
mark_f  = ImageFont.truetype(AVENIR, 22, index=7)   # Regular

PAD = 90
d.line([(PAD, PAD), (PAD, H - PAD)], fill=INK, width=2)
inner_x = PAD + 32

eyebrow_text = "THE FIELD GUIDE  ·  NO. 1"
# Letterspacing via spacing trick: draw chars individually
def draw_tracked(draw, xy, text, font, fill, tracking_px):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        bbox = draw.textbbox((0, 0), ch, font=font)
        x += (bbox[2] - bbox[0]) + tracking_px

draw_tracked(d, (inner_x, PAD + 6), eyebrow_text, eyebrow, INK, 3)

title_lines = ["What's actually", "happening to your skin"]
y = PAD + 80
for line in title_lines:
    d.text((inner_x, y), line, font=title_f, fill=INK)
    y += 100

sub = "Nine mechanisms of skin aging — sorted by which ones"
sub2 = "you can do something about, and which ones no product reaches."
d.text((inner_x, H - PAD - 80), sub, font=sub_f, fill=SOFT)
d.text((inner_x, H - PAD - 44), sub2, font=sub_f, fill=SOFT)

mark = "n-strokes.github.io / active-poor-face"
mark_bbox = d.textbbox((0, 0), mark, font=mark_f)
mw = mark_bbox[2] - mark_bbox[0]
d.text((W - PAD - mw, PAD + 8), mark, font=mark_f, fill=SOFT)

out = os.path.join(os.path.dirname(__file__), "og-image.png")
img.save(out, "PNG", optimize=True)
print(f"wrote {out} ({os.path.getsize(out)} bytes)")
