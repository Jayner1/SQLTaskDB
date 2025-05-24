-- Lists all tasks with category names
SELECT t.task_id, t.description, t.is_completed, c.category_name
FROM Tasks t
JOIN Categories c ON t.category_id = c.category_id;

-- Lists completed tasks
SELECT t.description, c.category_name
FROM Tasks t
JOIN Categories c ON t.category_id = c.category_id
WHERE t.is_completed = 1;

-- Lists tasks in School category
SELECT t.description
FROM Tasks t
JOIN Categories c ON t.category_id = c.category_id
WHERE c.category_name = 'School';