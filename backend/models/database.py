import sqlite3, os, hashlib

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'agency.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db()
    conn.execute("""CREATE TABLE IF NOT EXISTS agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'admin', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.execute("""CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL,
        phone TEXT, company TEXT, service_interested TEXT, budget TEXT, message TEXT,
        status TEXT DEFAULT 'New', notes TEXT, source TEXT DEFAULT 'contact_form',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.execute("""CREATE TABLE IF NOT EXISTS service_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL,
        phone TEXT, company TEXT, service TEXT, budget TEXT, timeline TEXT, description TEXT,
        status TEXT DEFAULT 'Pending', notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    # Seed admin
    if not conn.execute("SELECT id FROM agents WHERE email='admin@bhaai.com'").fetchone():
        conn.execute("INSERT INTO agents (name,email,password_hash,role) VALUES (?,?,?,?)",
            ('Super Admin','admin@bhaai.com', hashlib.sha256(b'Admin@123').hexdigest(),'admin'))
    conn.commit()
    conn.close()
    print("[OK] Database ready")