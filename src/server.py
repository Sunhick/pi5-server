import os
import random
import logging
from io import BytesIO
from flask import Flask, send_file, abort, current_app
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)

# Configuration
class Config:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", os.path.join(BASE_DIR, "photos"))
    MAX_WIDTH = int(os.getenv("MAX_WIDTH", 1200))
    MAX_HEIGHT = int(os.getenv("MAX_HEIGHT", 825))

app.config.from_object(Config)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def resize_image_to_bytes(input_path):
    try:
        with Image.open(input_path) as img:
            img.thumbnail((app.config['MAX_WIDTH'], app.config['MAX_HEIGHT']), Image.Resampling.LANCZOS)
            img = img.convert('RGB')

            buf = BytesIO()
            img.save(buf, format='JPEG', quality=85, optimize=True, progressive=False)
            buf.seek(0)
            return buf
    except UnidentifiedImageError:
        logger.error(f"Cannot identify image file: {input_path}")
        return None
    except Exception as e:
        logger.error(f"Error processing image {input_path}: {e}")
        return None

@app.route("/image.jpg")
def random_image():
    if not os.path.isdir(app.config['IMAGE_FOLDER']):
        logger.error(f"Image folder does not exist: {app.config['IMAGE_FOLDER']}")
        abort(500, description="Server configuration error")

    images = [f for f in os.listdir(app.config['IMAGE_FOLDER'])
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not images:
        logger.warning("No images found in folder")
        abort(404, description="No images found")

    chosen_image = random.choice(images)
    image_path = os.path.join(app.config['IMAGE_FOLDER'], chosen_image)

    image_bytes = resize_image_to_bytes(image_path)
    if not image_bytes:
        abort(500, description="Failed to process image")

    logger.info(f"Serving image: {chosen_image}")
    return send_file(image_bytes, mimetype='image/jpeg')

if __name__ == "__main__":
    # Only for development/testing. Use Gunicorn in production:
    # gunicorn -b 0.0.0.0:8000 src.server:app
    app.run(host='0.0.0.0', port=8000)
