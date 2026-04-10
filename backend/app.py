import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret')

from datetime import timedelta
app.permanent_session_lifetime = timedelta(hours=8)

CORS(app, origins=os.getenv('ALLOWED_ORIGINS','http://localhost:5000').split(','), supports_credentials=True)

from models.database import init_db
init_db()

from routes.public import public_bp
from routes.leads import leads_bp
from routes.auth import auth_bp
from routes.admin import admin_bp

app.register_blueprint(public_bp)
app.register_blueprint(leads_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"[START] Running on http://localhost:{port}")
    print(f"[INFO] Admin -> http://localhost:{port}/auth/login  (admin@bhaai.com / Admin@123)")
    app.run(host='0.0.0.0', port=port, debug=True)