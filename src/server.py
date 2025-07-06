from flask import Flask, send_file
import random
import os
from PIL import Image

app = Flask(__name__)

# Folder with your images (jpg/png)
IMAGE_FOLDER = "/Users/sunny/prv/github/Image-Server/photos"

PROCESSED_IMAGE = '/Users/sunny/prv/github/Image-Server/processed/image.jpg'
MAX_WIDTH = 1200
MAX_HEIGHT = 825

def resize_image(input_path, output_path):
    with Image.open(input_path) as img:
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
        # DO NOT convert to grayscale
        img = img.convert('RGB')  # Ensure compatible 3-channel JPEG

        # Save as baseline JPEG
        img.save(output_path, format='JPEG', quality=85, optimize=True, progressive=False)
    print(f"Processed image saved to {output_path}")

@app.route("/image.jpg")
def random_image():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not images:
        return "No images found", 404

    chosen_image = random.choice(images)
    image_path = os.path.join(IMAGE_FOLDER, chosen_image)
    resize_image(image_path, PROCESSED_IMAGE)

    return send_file(PROCESSED_IMAGE, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(host='192.168.1.179', port=8000)
