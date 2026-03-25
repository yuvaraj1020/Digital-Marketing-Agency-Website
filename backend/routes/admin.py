from flask import Blueprint, send_from_directory, session, redirect, render_template, request
import os

ADMIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'admin-dashboard'))
admin_bp = Blueprint('admin', __name__, template_folder=ADMIN_DIR)
ADMIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'admin-dashboard'))

@admin_bp.before_request
def require_admin():
    # Allow login and static assets if they exist but block html pages
    if 'agent_id' not in session and request.endpoint and 'login' not in request.endpoint:
        return redirect('/auth/login')

@admin_bp.route('/')
@admin_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@admin_bp.route('/clients')
def clients():
    return render_template('clients.html')

@admin_bp.route('/requests')
def requests_page():
    return render_template('requests.html')

@admin_bp.route('/<path:filename>')
def serve_admin_assets(filename):
    return send_from_directory(ADMIN_DIR, filename)
