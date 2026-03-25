"""Email service — BhAAi Fans Digital AA"""
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
AGENCY_EMAIL = os.getenv("AGENCY_EMAIL", "hello@bhaifansdigital.com")

def send_contact_email(data: dict):
    """Send notification to agency and confirmation to client."""
    if not SMTP_USER or not SMTP_PASS:
        print("[EmailService] SMTP not configured — skipping email.")
        return

    # Notify agency
    _send(
        to=AGENCY_EMAIL,
        subject=f"New enquiry from {data.get('name')} — {data.get('service', 'General')}",
        body=_agency_template(data)
    )

    # Confirm to client
    if data.get("email"):
        _send(
            to=data["email"],
            subject="Thanks for reaching out — BhAAi Fans Digital AA",
            body=_client_template(data)
        )

def _send(to: str, subject: str, body: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to
    msg.attach(MIMEText(body, "html"))
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, to, msg.as_string())

def _agency_template(d: dict) -> str:
    return f"""
    <div style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:2rem;background:#0a0a0a;color:#f5f0e8;">
      <h2 style="color:#c8ff00;font-size:1.5rem;margin-bottom:1.5rem;">New Enquiry</h2>
      <table style="width:100%;border-collapse:collapse;">
        <tr><td style="padding:0.6rem 0;color:#888;width:140px;">Name</td><td style="color:#f5f0e8;">{d.get('name','—')}</td></tr>
        <tr><td style="padding:0.6rem 0;color:#888;">Email</td><td style="color:#f5f0e8;">{d.get('email','—')}</td></tr>
        <tr><td style="padding:0.6rem 0;color:#888;">Phone</td><td style="color:#f5f0e8;">{d.get('phone','—')}</td></tr>
        <tr><td style="padding:0.6rem 0;color:#888;">Company</td><td style="color:#f5f0e8;">{d.get('company','—')}</td></tr>
        <tr><td style="padding:0.6rem 0;color:#888;">Service</td><td style="color:#c8ff00;">{d.get('service','—')}</td></tr>
        <tr><td style="padding:0.6rem 0;color:#888;">Budget</td><td style="color:#f5f0e8;">{d.get('budget','—')}</td></tr>
      </table>
      <div style="margin-top:1.5rem;padding:1rem;background:#1a1a1a;border-left:3px solid #c8ff00;">
        <p style="color:#888;font-size:0.85rem;margin:0 0 0.5rem;">Message</p>
        <p style="color:#f5f0e8;margin:0;">{d.get('message','—')}</p>
      </div>
    </div>"""

def _client_template(d: dict) -> str:
    return f"""
    <div style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:2rem;background:#0a0a0a;color:#f5f0e8;">
      <h2 style="color:#c8ff00;">Thanks, {d.get('name','').split()[0]}.</h2>
      <p style="color:#888;">We've received your enquiry about <strong style="color:#f5f0e8;">{d.get('service','our services')}</strong> and will get back to you within 24 hours.</p>
      <p style="color:#888;">In the meantime, feel free to check out our <a href="https://bhaifansdigital.com/portfolio" style="color:#c8ff00;">portfolio</a>.</p>
      <p style="margin-top:2rem;color:#444;font-size:0.8rem;">— BhAAi Fans Digital AA · hello@bhaifansdigital.com</p>
    </div>"""
