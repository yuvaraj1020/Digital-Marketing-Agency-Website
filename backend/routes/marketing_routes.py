"""Marketing enquiry routes — BhAAi Fans Digital AA"""
from flask import Blueprint, request, jsonify

marketing_bp = Blueprint("marketing", __name__)

@marketing_bp.route("/marketing-enquiry", methods=["POST"])
def marketing_enquiry():
    data = request.get_json(silent=True) or {}
    required = ["name", "email", "goal"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"success": False, "errors": {f: "Required" for f in missing}}), 422
    return jsonify({"success": True, "message": "Enquiry received."}), 200
