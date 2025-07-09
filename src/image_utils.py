import os
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from flask import current_app

def resize_image_to_bytes(input_path):
    try:
        with Image.open(input_path) as img:
            img.thumbnail(
                (current_app.config['MAX_WIDTH'], current_app.config['MAX_HEIGHT']),
                Image.Resampling.LANCZOS
            )
            img = img.convert('RGB')
            buf = BytesIO()
            img.save(buf, format='JPEG', quality=85, optimize=True, progressive=False)
            buf.seek(0)
            return buf
    except UnidentifiedImageError:
        current_app.logger.error(f"Cannot identify image file: {input_path}")
        return None
    except Exception as e:
        current_app.logger.error(f"Error processing image {input_path}: {e}")
        return None
