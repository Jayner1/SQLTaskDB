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

def add_task(conn, description, category_id):
    """Adds a task to Tasks table."""
    if not description.strip():
        print("Description cannot be empty!")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT category_id FROM Categories WHERE category_id = ?", (category_id,))
    if not cursor.fetchone():
        print("Invalid category ID!")
        return
    cursor.execute("INSERT INTO Tasks (description, category_id) VALUES (?, ?)",
                   (description, category_id))
    conn.commit()
    print("Task added!")

def view_tasks(conn):
    """Displays all tasks with categories."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.task_id, t.description, t.is_completed, c.category_name
        FROM Tasks t JOIN Categories c ON t.category_id = c.category_id
    """)
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for task in tasks:
        status = "Yes" if task[2] else "No"
        print(f"ID: {task[0]}, Description: {task[1]}, Category: {task[3]}, Completed: {status}")

def mark_complete(conn, task_id):
    """Marks a task as completed."""
    cursor = conn.cursor()
    cursor.execute("UPDATE Tasks SET is_completed = 1 WHERE task_id = ?", (task_id,))
    if cursor.rowcount == 0:
        print("Invalid task ID!")
    else:
        conn.commit()
        print("Task marked complete!")

def delete_task(conn, task_id):
    """Deletes a task."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tasks WHERE task_id = ?", (task_id,))
    if cursor.rowcount == 0:
        print("Invalid task ID!")
    else:
        conn.commit()
        print("Task deleted!")

def main():
    """Runs the menu-driven interface."""
    conn = connect_db()
    initialize_db(conn)

    while True:
        print("\nTask Management Database")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            desc = input("Description: ")
            cat_id = input("Category ID (1=Work, 2=School): ")
            try:
                add_task(conn, desc, int(cat_id))
            except ValueError:
                print("Invalid category ID!")
        elif choice == "2":
            view_tasks(conn)
        elif choice == "3":
            task_id = input("Task ID: ")
            try:
                mark_complete(conn, int(task_id))
            except ValueError:
                print("Invalid task ID!")
        elif choice == "4":
            task_id = input("Task ID: ")
            try:
                delete_task(conn, int(task_id))
            except ValueError:
                print("Invalid task ID!")
        elif choice == "5":
            print("Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()