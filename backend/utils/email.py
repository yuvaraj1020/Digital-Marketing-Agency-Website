import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_lead_notification(lead_data):
    """
    Sends an email notification to the agency owner when a new lead is submitted.
    """
    owner_email = "yuvarajdevarakonda24@gmail.com"
    
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT', 587)
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')
    
    subject = f"New Lead Alert: {lead_data.get('name')} - {lead_data.get('company', 'No Company')}"
    
    body = f"""
    New Lead Submission Received!
    
    Client Name: {lead_data.get('name')}
    Client Email: {lead_data.get('email')}
    Phone: {lead_data.get('phone', 'N/A')}
    Company: {lead_data.get('company', 'N/A')}
    Requested Service: {lead_data.get('service')}
    Budget: {lead_data.get('budget', 'N/A')}
    
    Message:
    {lead_data.get('message')}
    """
    
    print(f"[EMAIL] Content to {owner_email}:\n{body}")
    
    if not smtp_server or not smtp_user or not smtp_pass:
        print("[WARN] SMTP credentials not configured. Email mock logged above.")
        return False
        
    try:
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = owner_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(smtp_server, int(smtp_port))
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False
