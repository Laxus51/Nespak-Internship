-- check query plan

EXPLAIN
SELECT *
FROM students
WHERE email='ali@gmail.com';

-- Execution timee

EXPLAIN ANALYZE
SELECT *
FROM students
WHERE cgpa>3.5;

-- index scan

EXPLAIN ANALYZE
SELECT *
FROM students
WHERE student_id=15;