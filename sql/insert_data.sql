-- Inserts sample categories
INSERT INTO Categories (category_name) VALUES ('Work');
INSERT INTO Categories (category_name) VALUES ('School');
INSERT INTO Categories (category_name) VALUES ('Personal');
INSERT INTO Categories (category_name) VALUES ('Health');


-- Inserts sample tasks
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Team meeting', 0, 1);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Write report', 0, 2);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Code review', 1, 1);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Study SQL', 0, 2);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Plan sprint', 0, 1);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Grocery shopping', 0, 3);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Yoga class', 0, 4);
INSERT INTO Tasks (description, is_completed, category_id) VALUES ('Doctor appointment', 0, 4);