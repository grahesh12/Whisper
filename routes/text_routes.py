
from flask import Blueprint, request, jsonify
from services.text_service import translate_text

text_bp = Blueprint("text_bp", __name__)

@text_bp.route("/api/text", methods=["POST"])
def handle_text():
    print("[INFO] /api/text endpoint received a request")
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Text field is required"}), 400

    text = data["text"]
    result = translate_text(text)
    return jsonify(result), 200 if result["status"] == "success" else 500
