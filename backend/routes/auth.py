import hashlib, os
from flask import Blueprint, request, session, redirect, jsonify, send_from_directory, render_template
from models.database import get_db

auth_bp = Blueprint('auth', __name__)
ADMIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','admin-dashboard'))

@auth_bp.route('/login', methods=['GET'])
def login_page():
    if 'agent_id' in session: return redirect('/admin/dashboard')
    return render_template('admin-login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    d = request.get_json()
    email = d.get('email','').strip().lower()
    pw_hash = hashlib.sha256(d.get('password','').encode()).hexdigest()
    conn = get_db()
    agent = conn.execute("SELECT * FROM agents WHERE email=? AND password_hash=?", (email, pw_hash)).fetchone()
    conn.close()
    if not agent: return jsonify({'error': 'Invalid credentials'}), 401
    session.permanent = True
    session.update({'agent_id': agent['id'], 'agent_name': agent['name'],
                    'agent_email': agent['email'], 'agent_role': agent['role']})
    return jsonify({'success': True, 'name': agent['name'], 'redirect': '/admin/dashboard'})

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/auth/login')

@auth_bp.route('/me')
def me():
    if 'agent_id' not in session and 'user_id' not in session:
        return jsonify({'authenticated': False}), 401
    
    if 'agent_id' in session:
        return jsonify({'authenticated': True, 'type': 'admin', 'name': session['agent_name'], 'role': session['agent_role']})
    else:
        return jsonify({'authenticated': True, 'type': 'user', 'name': session['user_name'], 'email': session['user_email']})

@auth_bp.route('/user/register', methods=['POST'])
def user_register():
    d = request.get_json()
    name = d.get('name', '').strip()
    email = d.get('email', '').strip().lower()
    pw = d.get('password', '')
    if not name or not email or not pw:
        return jsonify({'error': 'Name, email, and password are required'}), 400
    
    pw_hash = hashlib.sha256(pw.encode()).hexdigest()
    conn = get_db()
    
    existing = conn.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
    if existing:
        conn.close()
        return jsonify({'error': 'Email already registered'}), 400
        
    try:
        cur = conn.execute("INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)", (name, email, pw_hash))
        conn.commit()
        user_id = cur.lastrowid
        conn.close()
        
        # Auto-login upon registration
        session.permanent = True
        session.update({'user_id': user_id, 'user_name': name, 'user_email': email})
        
        return jsonify({'success': True, 'message': 'Registration successful'})
    except Exception as e:
        conn.close()
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/user/login', methods=['POST'])
def user_login():
    d = request.get_json()
    email = d.get('email', '').strip().lower()
    pw_hash = hashlib.sha256(d.get('password', '').encode()).hexdigest()
    
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email=? AND password_hash=?", (email, pw_hash)).fetchone()
    conn.close()
    
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401
        
    session.permanent = True
    session.update({'user_id': user['id'], 'user_name': user['name'], 'user_email': user['email']})
    
    return jsonify({'success': True, 'name': user['name']})

@auth_bp.route('/user/logout')
def user_logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect('/')