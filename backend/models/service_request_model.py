"""Service request model — BhAAi Fans Digital AA"""
import sqlite3, os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/database.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS service_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                service TEXT NOT NULL,
                details TEXT,
                status TEXT DEFAULT 'new',
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        conn.commit()

def create_service_request(data: dict) -> int:
    init_db()
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO service_requests (name, email, service, details)
            VALUES (?, ?, ?, ?)
        """, (data.get("name"), data.get("email"), data.get("service"), data.get("details")))
        conn.commit()
        return cur.lastrowid

def get_all_requests():
    init_db()
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM service_requests ORDER BY created_at DESC").fetchall()
        return [dict(r) for r in rows]

def update_request_status(req_id: int, status: str):
    init_db()
    with get_conn() as conn:
        conn.execute("UPDATE service_requests SET status = ? WHERE id = ?", (status, req_id))
        conn.commit()
