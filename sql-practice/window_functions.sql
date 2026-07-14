-- Rank

SELECT
student_id,
first_name,
cgpa,
RANK()
OVER
(ORDER BY cgpa DESC)
FROM students;

-- Dense Rank

SELECT
first_name,
cgpa,
DENSE_RANK()
OVER
(ORDER BY cgpa DESC)
FROM students;

-- Row Number

SELECT
first_name,
ROW_NUMBER()
OVER
(ORDER BY first_name)
FROM students;


-- Running average

SELECT
marks,
AVG(marks)
OVER()
FROM enrollments;

