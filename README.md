# 🖼️ Flask Image Server

A lightweight Flask-based image server that serves a **random photo** from a local folder, resizes it on the fly, and returns it as a JPEG — ideal for digital photo frames or background feeds.

## 🚀 Features

- Serves a random image from a folder on each request to `/image.jpg`
- Resizes images dynamically (max width and height configurable)
- No disk writes — images are processed in-memory
- Lightweight, easy to deploy
- Production-ready with error handling and logging

## 📁 Project Structure

```
project-root/
├── photos/              # Folder containing your source images (.jpg, .jpeg, .png)
├── src/
│   └── server.py        # Main Flask server
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone git@github.com:Sunhick/pi5-server.git
cd pi5-server
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add images

Place your `.jpg`, `.jpeg`, or `.png` files inside the `photos/` folder.

### 5. Run the server (development)

```bash
python src/server.py
```

This will start the server on:

```
http://0.0.0.0:8000/image.jpg
```

Each request will return a different resized image.

---

## ⚙️ Configuration (Optional)

You can override the defaults using environment variables:

| Variable       | Default     | Description                            |
|----------------|-------------|----------------------------------------|
| `IMAGE_FOLDER` | `photos/`   | Path to folder with source images      |
| `MAX_WIDTH`    | `1200`      | Maximum image width                    |
| `MAX_HEIGHT`   | `825`       | Maximum image height                   |

Example:

```bash
export IMAGE_FOLDER=/path/to/your/images
export MAX_WIDTH=1920
export MAX_HEIGHT=1080
```

---

## 🏗️ Run in Production (with Gunicorn)

```bash
gunicorn -b 0.0.0.0:8000 src.server:app
```

Optionally put it behind Nginx or run it in a container. If you'd like a `Dockerfile`, just ask!

---

## 📄 License

MIT License. See `LICENSE` for details.
