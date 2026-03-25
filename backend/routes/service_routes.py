"""Service request routes — BhAAi Fans Digital AA"""
from flask import Blueprint, request, jsonify
from models.service_request_model import create_service_request, get_all_requests

service_bp = Blueprint("service", __name__)

@service_bp.route("/service-request", methods=["POST"])
def service_request():
    data = request.get_json(silent=True) or {}
    required = ["name", "email", "service"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"success": False, "errors": {f: "Required" for f in missing}}), 422
    req_id = create_service_request(data)
    return jsonify({"success": True, "id": req_id}), 201

@service_bp.route("/service-requests", methods=["GET"])
def list_requests():
    return jsonify(get_all_requests()), 200
