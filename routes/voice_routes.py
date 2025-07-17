from flask import Blueprint, request, jsonify
from services.voice_service import transcribe_audio

voice_bp = Blueprint("voice_bp", __name__)

@voice_bp.route("/api/voice", methods=["POST"])
def handle_voice():
    print("[INFO] /api/voice endpoint received a request")
    if "voice" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    file = request.files["voice"]
    result = transcribe_audio(file)
    return jsonify(result), 200 if result["status"] == "success" else 500
