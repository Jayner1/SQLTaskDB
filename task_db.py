import sqlite3
def view_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT t.task_id, t.description, t.is_completed, c.category_name FROM Tasks t JOIN Categories c ON t.category_id = c.category_id")
    for task in cursor.fetchall():
        status = "Yes" if task[2] else "No"
        print(f"ID: {task[0]}, Description: {task[1]}, Category: {task[3]}, Completed: {status}")