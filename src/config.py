import os

class Config:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", os.path.join(BASE_DIR, "photos"))
    MAX_WIDTH = int(os.getenv("MAX_WIDTH", 960))
    MAX_HEIGHT = int(os.getenv("MAX_HEIGHT", 825))
