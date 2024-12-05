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
    cursor = conn.cursor()
    try:
        # Create the Requests table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester_name TEXT NOT NULL,
                department TEXT NOT NULL,
                project TEXT NOT NULL,
                purpose TEXT NOT NULL,
                amount_requested REAL NOT NULL,
                status TEXT NOT NULL,
                funds_issued INTEGER DEFAULT 0,
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
        print("Tables created successfully")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    db_file = "requests.db"
    connection = create_connection(db_file)
    if connection:
        create_tables(connection)
        connection.close()
