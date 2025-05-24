-- Lists all tasks with category and priority names
SELECT t.task_id, t.description, t.is_completed, c.category_name, p.priority_name
FROM Tasks t
JOIN Categories c ON t.category_id = c.category_id
JOIN Priority p ON t.priority_id = p.priority_id;

-- Lists completed tasks with categories and priorities
SELECT t.description, c.category_name, p.priority_name
FROM Tasks t
JOIN Categories c ON t.category_id = c.category_id
JOIN Priority p ON t.priority_id = p.priority_id
WHERE t.is_completed = 1;

-- Lists high-priority tasks
SELECT t.description, c.category_name
FROM Tasks t
JOIN Categories c ON t.category_id = c.category_id
JOIN Priority p ON t.priority_id = p.priority_id
WHERE p.priority_name = 'High';