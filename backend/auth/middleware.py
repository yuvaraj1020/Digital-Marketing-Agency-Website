import functools
from flask import session, redirect, url_for, jsonify, request

def login_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        if 'agent_id' not in session:
            return redirect('/auth/login')
        return f(*args, **kwargs)
    return decorated

def api_login_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        if 'agent_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated