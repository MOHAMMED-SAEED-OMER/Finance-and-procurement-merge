import sqlite3

# Database file name
DB_FILE = "requests.db"

def create_connection():
    """Create and return a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_database():
    """Create necessary tables in the database if they do not already exist."""
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database. Initialization aborted.")
        return

    try:
        cursor = conn.cursor()
        
        # Create the Requests table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester_name TEXT NOT NULL,
                department TEXT NOT NULL,
                project TEXT NOT NULL,
                purpose TEXT NOT NULL,
                amount_requested REAL NOT NULL,
                status TEXT DEFAULT 'Pending',
                funds_issued REAL DEFAULT 0,
                actual_expenses REAL,
                liquidation_date TEXT
            )
        """)

        # Create the Approvals table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Approvals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_id INTEGER NOT NULL,
                manager_name TEXT,
                approval_date TEXT,
                status TEXT,
                FOREIGN KEY (request_id) REFERENCES Requests (id)
            )
        """)

        # Create the Finance table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Finance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_id INTEGER NOT NULL,
                amount_issued REAL,
                issue_date TEXT,
                liquidation_date TEXT,
                actual_expenses REAL,
                attachments TEXT,
                FOREIGN KEY (request_id) REFERENCES Requests (id)
            )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()
