-- Basic execution plan
EXPLAIN
SELECT *
FROM students
WHERE student_id = 10;

-- Execution plan with timing
EXPLAIN ANALYZE
SELECT *
FROM students
WHERE email = 'student1@example.com';

-- Join execution plan
EXPLAIN ANALYZE
SELECT s.first_name, c.course_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id;

-- Aggregate execution plan
EXPLAIN ANALYZE
SELECT department_id, COUNT(*)
FROM students
GROUP BY department_id;

-- Update planner statistics
ANALYZE students;