from flask import Blueprint, request, jsonify, session
from models.database import get_db
from utils.email import send_lead_notification

leads_bp = Blueprint('leads', __name__)

@leads_bp.route('/contact', methods=['POST'])
def submit_contact():
    if 'user_id' not in session and 'agent_id' not in session:
        return jsonify({'error': 'Unauthorized. Please login first.'}), 401
        
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
        
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone', '')
    company = data.get('company', '')
    service = data.get('service')
    budget = data.get('budget', '')
    message = data.get('message')
    
    if not name or not email or not service or not message:
        return jsonify({'error': 'Missing required fields'}), 400
        
    user_id = session.get('user_id') # Will be None if agent is submitting, but that's fine
        
    try:
        conn = get_db()
        conn.execute(
            """INSERT INTO leads (name, email, phone, company, service_interested, budget, message) 
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (name, email, phone, company, service, budget, message)
        )
        conn.commit()
        conn.close()
        
        # Send Notification
        send_lead_notification(data)
        
        return jsonify({'success': True, 'message': 'Lead submitted successfully'})
    except Exception as e:
        print(f"Error saving lead: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

@leads_bp.route('/leads', methods=['GET'])
def get_leads():
    if 'agent_id' not in session:
        return jsonify({'error': 'Unauthorized admin access'}), 401
    
    conn = get_db()
    leads = conn.execute("SELECT * FROM leads ORDER BY created_at DESC").fetchall()
    conn.close()
    
    # Convert rows to dict
    leads_list = [dict(lead) for lead in leads]
    return jsonify({'success': True, 'leads': leads_list})

@leads_bp.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    if 'agent_id' not in session:
        return jsonify({'error': 'Unauthorized admin access'}), 401
        
    try:
        conn = get_db()
        conn.execute("DELETE FROM leads WHERE id = ?", (lead_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Lead deleted successfully'})
    except Exception as e:
        print(f"Error deleting lead: {e}")
        return jsonify({'error': 'Database error occurred'}), 500
