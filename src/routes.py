import os
import random
from flask import send_file, abort, current_app
from .image_utils import resize_image_to_bytes

def register_routes(app):
    @app.route("/image.jpg")
    def random_image():
        folder = current_app.config['IMAGE_FOLDER']
        if not os.path.isdir(folder):
            current_app.logger.error(f"Image folder does not exist: {folder}")
            abort(500, description="Server configuration error")

        images = [f for f in os.listdir(folder)
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not images:
            current_app.logger.warning("No images found in folder")
            abort(404, description="No images found")

        chosen_image = random.choice(images)
        image_path = os.path.join(folder, chosen_image)

        image_bytes = resize_image_to_bytes(image_path)
        if not image_bytes:
            abort(500, description="Failed to process image")

        current_app.logger.info(f"Serving image: {chosen_image}")
        return send_file(image_bytes, mimetype='image/jpeg')
