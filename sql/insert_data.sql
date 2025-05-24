-- Inserts sample categories
INSERT INTO Categories (category_name) VALUES ('Work');
INSERT INTO Categories (category_name) VALUES ('School');

-- Inserts sample tasks
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Team meeting', 0, 1);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Write report', 0, 2);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Code review', 1, 1);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Study SQL', 0, 2);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Plan sprint', 0, 1);