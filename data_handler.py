import sqlite3
import pandas as pd

DB_FILE = "expenses.db"

def initialize_db():
    """Create the expenses table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_expense(category, amount, date):
    """Insert a new expense into the database."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
              (category, amount, str(date)))
    conn.commit()
    conn.close()

def load_expenses():
    """Load all expenses as a DataFrame."""
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    # Parse date column properly
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
    return df
