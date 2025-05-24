-- Marks task as complete by task_id
UPDATE Tasks SET is_completed = 1 WHERE task_id = 1;

-- Updates task priority by task_id
UPDATE Tasks SET priority_id = 3 WHERE task_id = 2;

-- Deletes task by task_id
DELETE FROM Tasks WHERE task_id = 2;