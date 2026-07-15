-- CREATE
INSERT INTO students
(first_name,last_name,email,department_id)
VALUES
('Ali','Khan','ali@example.com',2);

-- READ
SELECT student_id,
       first_name,
       email
FROM students
WHERE department_id = 2;

-- UPDATE
UPDATE students
SET email='alikhan@example.com'
WHERE student_id=1;

-- HARD DELETE
DELETE FROM students
WHERE student_id=100;

-- SOFT DELETE 
UPDATE students
SET is_deleted = TRUE,
    deleted_at = CURRENT_TIMESTAMP
WHERE student_id=2;