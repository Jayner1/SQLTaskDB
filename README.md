 As a software engineer, my goal is to deepen my understanding of relational databases and SQL by building a Task Management Database. This software integrates with a SQLite relational database to store and manage tasks, allowing users to organize their work efficiently. The Python-based console application enables users to add tasks with descriptions, categories (e.g., Work, School, Health, Personal), and priorities (e.g., High, Medium, Low), view tasks with associated details, mark tasks as complete, and delete tasks. The program uses SQL to perform CRUD operations (Create, Read, Update, Delete) and joins three tables to display comprehensive task information.

 To use the program, run `python3 task_db.py` and select options from the menu:
 - Add Task: Enter a description, category ID, and priority ID.
 - View Tasks: Display all tasks with categories and priorities.
 - Mark Complete: Update a task’s completion status.
 - Update Priority: Change a task's priority level. 
 - Delete Task: Remove a task by ID.
 - Exit: Close the program.

 My purpose is to master SQL table design, foreign key relationships, and JOIN operations while enhancing my Python skills for database integration. This project showcases a practical application of relational databases for task management.

 [Software Demo Video](https://youtu.be/abc123)

 # Relational Database

 The project uses **SQLite**, a lightweight, serverless relational database ideal for small-scale applications. SQLite is embedded in Python via the `sqlite3` library, ensuring easy setup and portability.

 The database (`task_manager.db`) has three tables:
 - **Priority**:
   - `priority_id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `priority_name`: TEXT NOT NULL (e.g., High, Medium, Low)
 - **Categories**:
   - `category_id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `category_name`: TEXT NOT NULL (e.g., Work, School, Health, Personal)
 - **Tasks**:
   - `task_id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `description`: TEXT NOT NULL
   - `is_completed`: BOOLEAN DEFAULT 0
   - `category_id`: INTEGER, FOREIGN KEY to Categories
   - `priority_id`: INTEGER, FOREIGN KEY to Priority

 # Development Environment

 Tools used:
 - **Visual Studio Code**: Code editor with Python and SQL support.
 - **DB Browser for SQLite**: Visualize and test database schema and queries.
 - **Git**: Version control, hosted on GitHub.
 - **macOS Terminal**: Run Python scripts and Git commands.

 Programming language and libraries:
 - **Python 3.13.3**: Core language for console interface.
 - **sqlite3**: Built-in Python library for SQLite integration.

 # Useful Websites

 - [SQLite Documentation](https://www.sqlite.org/docs.html)
 - [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
 - [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
 - [TutorialsPoint: SQLite - Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

 # Future Work

 - Add date/time for task deadlines with range-based queries.
 - Implement sorting tasks by priority or category.
 - Add a graphical user interface for better usability.