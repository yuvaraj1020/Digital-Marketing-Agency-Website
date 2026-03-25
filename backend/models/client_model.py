"""Client model — BhAAi Fans Digital AA"""
import sqlite3, os, json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/database.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                company TEXT,
                service TEXT,
                budget TEXT,
                message TEXT,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        conn.commit()

def create_client(data: dict) -> int:
    init_db()
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO clients (name, email, phone, company, service, budget, message)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("name"), data.get("email"), data.get("phone"),
            data.get("company"), data.get("service"), data.get("budget"),
            data.get("message")
        ))
        conn.commit()
        return cur.lastrowid

def get_all_clients():
    init_db()
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM clients ORDER BY created_at DESC").fetchall()
        return [dict(r) for r in rows]

def get_client_by_id(client_id: int):
    init_db()
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM clients WHERE id = ?", (client_id,)).fetchone()
        return dict(row) if row else None
