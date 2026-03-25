"""Form validation utilities — BhAAi Fans Digital AA"""
import re

def validate_contact_form(data: dict) -> dict:
    errors = {}
    if not data.get("name", "").strip():
        errors["name"] = "Name is required."
    email = data.get("email", "").strip()
    if not email:
        errors["email"] = "Email is required."
    elif not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email):
        errors["email"] = "Please enter a valid email address."
    phone = data.get("phone", "").strip()
    if phone and not re.match(r"^[\d\s\+\-\(\)]{7,15}$", phone):
        errors["phone"] = "Please enter a valid phone number."
    if not data.get("service", "").strip():
        errors["service"] = "Please select a service."
    if not data.get("message", "").strip():
        errors["message"] = "Message is required."
    elif len(data["message"].strip()) < 10:
        errors["message"] = "Message is too short."
    return errors

def validate_file_upload(filename: str, allowed_extensions: set) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions

def sanitize_string(value: str, max_length: int = 500) -> str:
    return str(value).strip()[:max_length]
