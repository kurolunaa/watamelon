from PIL import Image

def overlayImage(base, overlay, scale):
    base = Image.open(base).convert("RGBA")
    overlay = Image.open(overlay).convert("RGBA")

    base_width, base_height = base.size

    scale_factor = 0.3
    new_width = int(base_width * scale_factor)

    aspect_ratio = overlay.width / overlay.height
    new_height = int(new_width / aspect_ratio)

    overlay = overlay.resize((new_width, new_height), Image.LANCZOS)

    x = base_width - new_width
    y = base_height - new_height

    base.paste(overlay, (x, y), overlay)

    base.save("bin/extra/withfwmc/temp/result.png", format="PNG")

    return "bin/extra/withfwmc/temp/result.png"