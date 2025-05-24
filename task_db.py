# task_db.py: Console interface for Task Management Database
# Author: Jason
import sqlite3

def connect_db():
    """Connects to SQLite database."""
    conn = sqlite3.connect("task_manager.db")
    return conn

def execute_sql_file(conn, filename):
    """Executes SQL script from file."""
    with open(filename, 'r') as f:
        conn.executescript(f.read())
    conn.commit()

def table_exists(conn, table_name):
    """Checks if a table exists in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

def initialize_db(conn):
    """Initializes database with tables and sample data if needed."""
    if not table_exists(conn, "Categories"):
        execute_sql_file(conn, "sql/create_tables.sql")
        execute_sql_file(conn, "sql/insert_data.sql")
        print("Created tables and inserted sample data")
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Categories")
        if cursor.fetchone()[0] == 0:
            execute_sql_file(conn, "sql/insert_data.sql")
            print("Inserted sample data")
        else:
            print("Tables and data already exist")

def main():
    """Sets up database and tests connection."""
    conn = connect_db()
    print("SQLite version:", sqlite3.sqlite_version)
    print("Connected to task_manager.db")
    initialize_db(conn)
    conn.close()

if __name__ == "__main__":
    main()