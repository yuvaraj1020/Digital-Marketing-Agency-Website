"""Video edit upload routes — BhAAi Fans Digital AA"""
import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename

video_bp = Blueprint("video", __name__)
ALLOWED = {"mp4", "mov", "avi", "mkv", "webm"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED

@video_bp.route("/video-upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"success": False, "message": "No file provided"}), 400
    file = request.files["file"]
    if not file.filename or not allowed_file(file.filename):
        return jsonify({"success": False, "message": "Invalid file type"}), 400
    filename = secure_filename(file.filename)
    dest = os.path.join(current_app.config["UPLOAD_FOLDER"], "videos", filename)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    file.save(dest)
    return jsonify({"success": True, "filename": filename}), 200
