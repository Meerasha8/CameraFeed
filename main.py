from flask import Flask, request, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    images = os.listdir(UPLOAD_FOLDER)
    images.sort(reverse=True)
    return render_template("index.html", images=images)

@app.route("/upload", methods=["POST"])
def upload():
    if request.data:
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, "wb") as f:
            f.write(request.data)
        return "Image uploaded", 200
    return "No image", 400

@app.route("/uploads/<filename>")
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
