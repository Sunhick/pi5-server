import os
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from flask import current_app

def resize_image_to_bytes(input_path):
    try:
        with Image.open(input_path) as img:
            # Convert to grayscale for e-paper display
            img = img.convert('L')

            # Enhance contrast for better e-paper visibility
            from PIL import ImageEnhance
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.3)  # Increase contrast by 30%

            # Resize to exact dimensions (this will stretch/distort if aspect ratios don't match)
            canvas = img.resize(
                (current_app.config['MAX_WIDTH'], current_app.config['MAX_HEIGHT']),
                Image.Resampling.LANCZOS
            )

            # Convert back to RGB for JPEG output (but maintain grayscale appearance)
            canvas = canvas.convert('RGB')

            buf = BytesIO()
            canvas.save(buf, format='JPEG', quality=95, optimize=True, progressive=False)
            buf.seek(0)
            return buf
    except UnidentifiedImageError:
        current_app.logger.error(f"Cannot identify image file: {input_path}")
        return None
    except Exception as e:
        current_app.logger.error(f"Error processing image {input_path}: {e}")
        return None
