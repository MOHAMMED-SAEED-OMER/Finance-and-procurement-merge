import sqlite3

# Initialize database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection successful")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create tables
def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Table for requests
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester_name TEXT NOT NULL,
                department TEXT,
                date_submitted TEXT,
                project TEXT,
                purpose TEXT,
                status TEXT DEFAULT 'pending',
                amount_requested REAL
            )
        """)

        # Table for approvals
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

        # Table for finance
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
        print("Tables created successfully")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    db_file = "requests.db"
    connection = create_connection(db_file)
    if connection:
        create_tables(connection)
        connection.close()
