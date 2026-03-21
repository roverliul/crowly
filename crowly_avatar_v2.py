# -*- coding: utf-8 -*-
"""
Crowly Avatar - Cyberpunk Bat v2 (improved)
"""
from PIL import Image, ImageDraw, ImageFilter
import math

size = 512
img = Image.new('RGBA', (size, size), (10, 10, 15, 255))
draw = ImageDraw.Draw(img)

def glow(draw, cx, cy, r_inner, r_outer, color):
    """Draw a gradient glow"""
    for i in range(20):
        ratio = i / 20
        alpha = int(60 * (1 - ratio))
        rr = r_inner + (r_outer - r_inner) * ratio
        draw.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=(*color, alpha))

# Background glow
glow(draw, 256, 230, 60, 160, (0, 212, 255))

# Wings - more refined shape
def draw_wing(draw, side):
    """Draw a bat wing with membrane details"""
    if side == 'left':
        # Main wing shape
        points = [(60, 200), (30, 130), (70, 80), (120, 120), (150, 160), (140, 210), (100, 250), (60, 230)]
        draw.polygon(points, fill=(22, 22, 40, 255), outline=(0, 212, 255, 200))
        # Wing bones
        draw.line([(70, 80), (60, 200)], fill=(0, 212, 255, 100), width=2)
        draw.line([(120, 120), (60, 200)], fill=(0, 212, 255, 80), width=1)
        draw.line([(150, 160), (60, 200)], fill=(0, 212, 255, 60), width=1)
        # Membrane lines
        draw.arc([50, 100, 130, 220], 0, 180, fill=(0, 212, 255, 60), width=1)
        draw.arc([70, 120, 110, 180], 0, 180, fill=(0, 212, 255, 40), width=1)
    else:
        points = [(452, 200), (482, 130), (442, 80), (392, 120), (362, 160), (372, 210), (412, 250), (452, 230)]
        draw.polygon(points, fill=(22, 22, 40, 255), outline=(0, 212, 255, 200))
        draw.line([(442, 80), (452, 200)], fill=(0, 212, 255, 100), width=2)
        draw.line([(392, 120), (452, 200)], fill=(0, 212, 255, 80), width=1)
        draw.line([(362, 160), (452, 200)], fill=(0, 212, 255, 60), width=1)
        draw.arc([370, 100, 450, 220], 180, 360, fill=(0, 212, 255, 60), width=1)
        draw.arc([390, 120, 430, 180], 180, 360, fill=(0, 212, 255, 40), width=1)

draw_wing(draw, 'left')
draw_wing(draw, 'right')

# Body - more streamlined
draw.ellipse([191, 220, 321, 360], fill=(22, 22, 40, 255), outline=(0, 212, 255, 150), width=1)
draw.ellipse([201, 230, 311, 350], fill=(16, 16, 30, 255))

# Chest plate
draw.ellipse([216, 260, 296, 330], fill=(0, 212, 255, 15))
draw.ellipse([226, 270, 286, 320], fill=(0, 212, 255, 10))

# Head
draw.ellipse([191, 130, 321, 210], fill=(22, 22, 40, 255), outline=(0, 212, 255, 150), width=1)
draw.ellipse([201, 140, 311, 200], fill=(16, 16, 30, 255))

# Ears - sharper, more bat-like
def draw_ear(draw, side):
    if side == 'left':
        # Outer ear
        draw.polygon([(200, 145), (175, 60), (235, 125)], fill=(22, 22, 40, 255), outline=(0, 212, 255, 200), width=1)
        # Inner ear
        draw.polygon([(203, 140), (185, 80), (228, 122)], fill=(10, 10, 15, 255))
        # Ear glow accent
        draw.line([(190, 100), (210, 130)], fill=(0, 212, 255, 80), width=2)
    else:
        draw.polygon([(312, 145), (337, 60), (277, 125)], fill=(22, 22, 40, 255), outline=(0, 212, 255, 200), width=1)
        draw.polygon([((309), 140), (327, 80), (284, 122)], fill=(10, 10, 15, 255))
        draw.line([(322, 100), (302, 130)], fill=(0, 212, 255, 80), width=2)

draw_ear(draw, 'left')
draw_ear(draw, 'right')

# Eyes - more intense glow
# Outer glow
draw.ellipse([195, 158, 265, 198], fill=(0, 212, 255, 30))
draw.ellipse([257, 158, 327, 198], fill=(0, 212, 255, 30))
# Eye rings
draw.ellipse([202, 162, 258, 194], outline=(0, 212, 255, 200), width=2)
draw.ellipse([264, 162, 320, 194], outline=(0, 212, 255, 200), width=2)
# Main eyes
draw.ellipse([210, 168, 250, 188], fill=(0, 212, 255, 255))
draw.ellipse([272, 168, 312, 188], fill=(0, 212, 255, 255))
# Pupils
draw.ellipse([220, 173, 240, 183], fill=(5, 5, 10, 255))
draw.ellipse([282, 173, 302, 183], fill=(5, 5, 10, 255))
# Highlights
draw.ellipse([224, 172, 232, 178], fill=(255, 255, 255, 220))
draw.ellipse([286, 172, 294, 178], fill=(255, 255, 255, 220))

# Nose - small, cute
draw.ellipse([247, 202, 265, 214], fill=(5, 5, 10, 255))
draw.ellipse([250, 204, 262, 212], fill=(0, 212, 255, 150))

# Mouth - subtle smile with fangs
draw.arc([232, 210, 280, 235], 200, 340, fill=(0, 212, 255, 150), width=2)
# Fangs - sharper
draw.polygon([(238, 228), (235, 245), (243, 235)], fill=(255, 255, 255, 255))
draw.polygon([(274, 228), (277, 245), (269, 235)], fill=(255, 255, 255, 255))

# Cybernetic details on face
draw.ellipse([175, 195, 183, 201], fill=(0, 212, 255, 200))  # left cheek dot
draw.ellipse([339, 195, 347, 201], fill=(0, 212, 255, 200))  # right cheek dot
draw.line([183, 198, 200, 198], fill=(0, 212, 255, 100), width=1)  # left line
draw.line([332, 198, 339, 198], fill=(0, 212, 255, 100), width=1)  # right line

# Circuit patterns on body
draw.line([220, 340, 220, 365], fill=(0, 212, 255, 80), width=1)
draw.line([220, 365], fill=(0, 212, 255, 80), width=1)
draw.arc([210, 350, 250, 375], 0, 90, fill=(0, 212, 255, 60), width=1)
draw.line([292, 340, 292, 365], fill=(0, 212, 255, 80), width=1)
draw.arc([262, 350, 302, 375], 90, 180, fill=(0, 212, 255, 60), width=1)

# Feet
draw.ellipse([218, 358, 248, 378], fill=(22, 22, 40, 255))
draw.ellipse([274, 358, 304, 378], fill=(22, 22, 40, 255))

# Claws - sharper
def draw_claws(draw, start_x, end_x, y_start):
    for x in range(start_x, end_x, 12):
        draw.line([x, y_start, x+3, y_start+18], fill=(0, 212, 255, 255), width=2)

draw_claws(draw, 220, 248, 375)
draw_claws(draw, 274, 302, 375)

# Name - just CROWLY, styled
draw.text((256, 430), "CROWLY", fill=(0, 212, 255, 255), anchor="mm", font=None)

# Small decorative dots around name
for angle in range(0, 360, 45):
    rad = math.radians(angle)
    x = 256 + int(40 * math.cos(rad))
    y = 430 + int(15 * math.sin(rad))
    draw.ellipse([x-2, y-2, x+2, y+2], fill=(0, 212, 255, 100))

# Save
output_path = 'C:/Users/liulv/.openclaw/workspace/crowly-site/crowly-avatar-v2.png'
img.save(output_path)
print(f"Avatar v2 saved: {output_path}")
