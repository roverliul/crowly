# -*- coding: utf-8 -*-
"""
Crowly Avatar - Cyberpunk Bat using PIL
"""
from PIL import Image, ImageDraw, ImageFilter
import math

size = 512
img = Image.new('RGBA', (size, size), (10, 10, 15, 255))
draw = ImageDraw.Draw(img)

def glow_circle(cx, cy, r, color, opacity=80):
    """Draw a glow circle"""
    for i in range(5):
        alpha = int(opacity * (1 - i/5))
        rr = r + i * 8
        draw.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=(*color[:3], alpha))

def ellipse(draw, cx, cy, rx, ry, fill, outline=None):
    draw.ellipse([cx-rx, cy-ry, cx+rx, cy+ry], fill=fill, outline=outline)

# Glow background
glow_circle(256, 256, 100, (0, 212, 255), 60)
glow_circle(256, 256, 60, (0, 212, 255), 40)

# Wings (dark with cyan outline)
wing_points_left = [
    (80, 200), (50, 150), (80, 100), (120, 140), (140, 180), (120, 220), (90, 240)
]
draw.polygon(wing_points_left, fill=(26, 26, 46, 255), outline=(0, 212, 255, 255))

wing_points_right = [
    (432, 200), (462, 150), (432, 100), (392, 140), (372, 180), (392, 220), (422, 240)
]
draw.polygon(wing_points_right, fill=(26, 26, 46, 255), outline=(0, 212, 255, 255))

# Wing membranes
draw.polygon([(90, 240), (60, 280), (100, 300), (150, 270), (130, 240)], 
             fill=(18, 18, 26, 255), outline=(0, 212, 255, 150))
draw.polygon([(422, 240), (452, 280), (412, 300), (362, 270), (382, 240)], 
             fill=(18, 18, 26, 255), outline=(0, 212, 255, 150))

# Body
ellipse(draw, 256, 300, 65, 80, (26, 26, 46, 255))
ellipse(draw, 256, 300, 55, 70, (18, 18, 26, 255))

# Chest glow
ellipse(draw, 256, 310, 30, 35, (0, 212, 255, 25))

# Head
ellipse(draw, 256, 180, 55, 50, (26, 26, 46, 255))
ellipse(draw, 256, 180, 48, 43, (18, 18, 26, 255))

# Ears (bat pointed ears)
# Left ear
draw.polygon([(200, 155), (180, 90), (230, 140)], fill=(26, 26, 46, 255), outline=(0, 212, 255, 255))
draw.polygon([(205, 152), (190, 105), (225, 138)], fill=(10, 10, 15, 255))
# Right ear
draw.polygon([(312, 155), (332, 90), (282, 140)], fill=(26, 26, 46, 255), outline=(0, 212, 255, 255))
draw.polygon([(307, 152), (322, 105), (287, 138)], fill=(10, 10, 15, 255))

# Eyes (glowing cyan)
ellipse(draw, 225, 180, 20, 17, (0, 212, 255, 255))
ellipse(draw, 287, 180, 20, 17, (0, 212, 255, 255))
ellipse(draw, 225, 180, 13, 11, (10, 10, 15, 255))
ellipse(draw, 287, 180, 13, 11, (10, 10, 15, 255))
# Eye highlights
draw.ellipse([228, 176, 234, 182], fill=(255, 255, 255, 200))
draw.ellipse([290, 176, 296, 182], fill=(255, 255, 255, 200))

# Eye glow rings
draw.ellipse([205, 163, 245, 197], outline=(0, 212, 255, 130), width=2)
draw.ellipse([267, 163, 307, 197], outline=(0, 212, 255, 130), width=2)

# Nose
ellipse(draw, 256, 205, 8, 6, (10, 10, 15, 255))
ellipse(draw, 256, 205, 5, 4, (0, 212, 255, 150))

# Mouth with fangs
draw.arc([240, 218, 272, 235], 0, 180, fill=(0, 212, 255, 150), width=2)
# Fangs
draw.line([245, 230, 243, 245], fill=(255, 255, 255, 255), width=3)
draw.line([267, 230, 269, 245], fill=(255, 255, 255, 255), width=3)

# Cybernetic accents (side dots and lines)
draw.ellipse([160, 240, 166, 246], fill=(0, 212, 255, 200))
draw.ellipse([346, 240, 352, 246], fill=(0, 212, 255, 200))
draw.line([166, 243, 190, 243], fill=(0, 212, 255, 130), width=1)
draw.line([346, 243, 322, 243], fill=(0, 212, 255, 130), width=1)

# Circuit lines on body
draw.line([220, 350, 220, 380], fill=(0, 212, 255, 100), width=1)
draw.line([220, 380, 200, 395], fill=(0, 212, 255, 100), width=1)
draw.line([292, 350, 292, 380], fill=(0, 212, 255, 100), width=1)
draw.line([292, 380, 312, 395], fill=(0, 212, 255, 100), width=1)

# Feet
ellipse(draw, 235, 390, 18, 10, (26, 26, 46, 255))
ellipse(draw, 277, 390, 18, 10, (26, 26, 46, 255))

# Claws
claw_color = (0, 212, 255, 255)
draw.line([225, 398, 220, 418], fill=claw_color, width=2)
draw.line([235, 400, 235, 420], fill=claw_color, width=2)
draw.line([245, 398, 250, 418], fill=claw_color, width=2)
draw.line([267, 398, 262, 418], fill=claw_color, width=2)
draw.line([277, 400, 277, 420], fill=claw_color, width=2)
draw.line([287, 398, 292, 418], fill=claw_color, width=2)

# Text - CROWLY
draw.text((256, 440), "CROWLY", fill=(0, 212, 255, 255), anchor="mm", font=None)
draw.text((256, 465), "AI ASSISTANT", fill=(139, 139, 158, 255), anchor="mm", font=None)

# Save
output_path = 'C:/Users/liulv/.openclaw/workspace/crowly-site/crowly-avatar.png'
img.save(output_path)
print(f"Avatar saved: {output_path}")
