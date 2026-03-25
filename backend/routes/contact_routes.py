"""Contact form routes — BhAAi Fans Digital AA"""
from flask import Blueprint, request, jsonify
from utils.validation import validate_contact_form
from utils.email_service import send_contact_email
from models.client_model import create_client

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}
    errors = validate_contact_form(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 422
    try:
        create_client(data)
        send_contact_email(data)
        return jsonify({"success": True, "message": "Message received. We'll be in touch within 24 hours."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": "Server error. Please try again."}), 500
