"""Portfolio model — BhAAi Fans Digital AA"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/database.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS portfolio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                tags TEXT,
                image_path TEXT,
                featured INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        conn.commit()

def get_all_portfolio(category=None):
    init_db()
    with get_conn() as conn:
        if category:
            rows = conn.execute(
                "SELECT * FROM portfolio WHERE category = ? ORDER BY featured DESC, created_at DESC",
                (category,)
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM portfolio ORDER BY featured DESC, created_at DESC"
            ).fetchall()
        return [dict(r) for r in rows]

def add_portfolio_item(data: dict) -> int:
    init_db()
    import json
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO portfolio (title, category, description, tags, image_path, featured)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.get("title"), data.get("category"), data.get("description"),
            json.dumps(data.get("tags", [])), data.get("image_path"), int(data.get("featured", 0))
        ))
        conn.commit()
        return cur.lastrowid
