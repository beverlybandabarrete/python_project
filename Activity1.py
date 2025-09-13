from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas
img = Image.new("RGB", (900, 700), (0, 0, 0))
draw = ImageDraw.Draw(img)

# -------- Gradient Background (Navy → Black) --------
for y in range(700):
    r = int(15 + (0-15) * (y/700))
    g = int(25 + (0-25) * (y/700))
    b = int(45 + (0-45) * (y/700))
    draw.line([(0, y), (900, y)], fill=(r, g, b))

# -------- Golden Glow Behind Medal --------
glow = Image.new("RGBA", (900, 700), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse((250, 100, 650, 500), fill=(255, 215, 0, 120))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

# -------- Medal --------
draw = ImageDraw.Draw(img)

# Ribbon
draw.polygon([(420, 50), (480, 50), (500, 150), (400, 150)], fill=(200, 30, 30))
draw.polygon([(400, 150), (500, 150), (450, 220)], fill=(150, 20, 20))

# Medal Circle
draw.ellipse((330, 220, 570, 460), fill=(255, 215, 0), outline="black", width=5)
draw.ellipse((360, 250, 540, 430), fill=(255, 239, 150))

# Star inside medal
draw.polygon([(450, 270), (465, 320), (520, 320), (475, 350),
              (490, 400), (450, 370), (410, 400), (425, 350),
              (380, 320), (435, 320)], fill=(218, 165, 32), outline="black")

# -------- Fonts --------
title_font = ImageFont.truetype("arialbd.ttf", 48)
subtitle_font = ImageFont.truetype("ariali.ttf", 32)

# -------- Centered Text --------
def draw_text_center(text, font, y, fill=(255,255,255)):
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((900-w)//2, y), text, font=font, fill=fill)

# -------- Border --------
draw.rectangle((20, 20, 880, 680), outline=(212,175,55), width=6)

# -------- Award Text (Balanced Inside Border) --------
draw_text_center("Intramurals Champion 2025", title_font, 500, fill=(255, 223, 130))
draw_text_center("is awarded to", subtitle_font, 555, fill=(200, 200, 200))
draw_text_center("College of Computing and Information Sciences", subtitle_font, 605, fill=(255, 223, 130))

# Save
img.save("CSELEC3_3B_BarreteBeverly_Activity1.png")
img.show()

