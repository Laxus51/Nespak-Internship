-- Create Materialized View
CREATE MATERIALIZED VIEW department_student_count AS
SELECT
    department_id,
    COUNT(*) AS total_students
FROM students
GROUP BY department_id;

-- Read Materialized View
SELECT *
FROM department_student_count;

-- Refresh Materialized View
REFRESH MATERIALIZED VIEW department_student_count;

-- Refresh Concurrently (requires a unique index)
-- REFRESH MATERIALIZED VIEW CONCURRENTLY department_student_count;

-- Drop Materialized View
DROP MATERIALIZED VIEW department_student_count;