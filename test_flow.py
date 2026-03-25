import urllib.request
import urllib.parse
import json
import http.cookiejar

BASE_URL = 'http://localhost:5000'

def run_tests():
    print("[START] Starting Automated API Flow Test with built-in urllib...\n")
    
    # Setup Cookie Jar for sessions
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    
    def fetch(url, method='GET', data=None):
        headers = {}
        body = None
        if data is not None:
            body = json.dumps(data).encode('utf-8')
            headers['Content-Type'] = 'application/json'
            
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                return response.status, json.loads(response.read().decode('utf-8')) if response.info().get_content_type() == 'application/json' else response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            try:
                msg = json.loads(e.read().decode('utf-8'))
            except:
                msg = str(e)
            return e.code, msg
        except Exception as e:
            return 500, str(e)

    # Test 1: Frontend Accessibility
    print("== 1. Testing Client Frontend ==")
    status, _ = fetch(f"{BASE_URL}/")
    assert status == 200, "Frontend homepage failed"
    print("[SUCCESS] Client homepage loaded (200 OK).")
    
    status, res = fetch(f"{BASE_URL}/api/quotes/random")
    assert status == 200, "Quotes API failed"
    print(f"[SUCCESS] Dynamic Quote API returned: {res.get('quote')}")

    # Test 2: User Registration & Login
    print("\n== 2. Testing User Registration ==")
    reg_data = {"name": "Test Python User", "email": "python@tester.com", "password": "password123"}
    status, res = fetch(f"{BASE_URL}/auth/user/register", method='POST', data=reg_data)
    print(f"[INFO] Register response: {status} - {res}")
    
    log_data = {"email": "python@tester.com", "password": "password123"}
    status, res = fetch(f"{BASE_URL}/auth/user/login", method='POST', data=log_data)
    assert status == 200, "Login failed"
    print("[SUCCESS] Client logged in and received session cookies.")

    # Test 3: Submitting a Contact Lead
    print("\n== 3. Testing Contact Form (Client Flow) ==")
    lead_data = {
        "name": "Test Python User",
        "email": "python@tester.com",
        "phone": "1234567890",
        "company": "Python Test Corp",
        "service": "Web Development",
        "budget": "50k-1lakh",
        "message": "This is an automated test verifying the contact flow."
    }
    status, res = fetch(f"{BASE_URL}/api/contact", method='POST', data=lead_data)
    assert status == 200, f"Contact submission failed: {res}"
    print(f"[SUCCESS] Contact form submitted successfully: {res.get('message')}")

    # Clear session to act as Admin
    cj.clear()
    
    # Test 4: Admin Backend Authentication & Lead Retrieval
    print("\n== 4. Testing Admin Backend Dashboard ==")
    admin_log = {"email": "admin@bhaai.com", "password": "Admin@123"}
    status, res = fetch(f"{BASE_URL}/auth/login", method='POST', data=admin_log)
    assert status == 200, "Admin login failed"
    print("[SUCCESS] Host Admin logged into the backend securely.")
    
    # Get Leads from Admin Dashboard API
    status, res = fetch(f"{BASE_URL}/api/leads")
    assert status == 200, "Failed to retrieve leads"
    leads = res.get('leads', [])
    assert len(leads) > 0, "No leads returned!"
    latest_lead = leads[0]
    
    print(f"[SUCCESS] Host Admin retrieved {len(leads)} leads from the database!")
    print(f"   -> Latest Lead Client: {latest_lead.get('name')} from {latest_lead.get('company')}")
    print(f"   -> Client Request: {latest_lead.get('message')}")

    print("\n[OK] ALL TESTS PASSED SUCCESSFULLY! Both Client and Host portals are fully functional.")

if __name__ == '__main__':
    run_tests()
