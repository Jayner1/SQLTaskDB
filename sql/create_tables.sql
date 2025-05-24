-- Creates Categories table for task categories
CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL
);

-- Creates Tasks table with foreign key to Categories
CREATE TABLE Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    is_completed BOOLEAN DEFAULT 0,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);