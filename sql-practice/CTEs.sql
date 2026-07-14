WITH AvgCGPA AS
(
SELECT AVG(cgpa) avg_cgpa
FROM students
)

SELECT *
FROM students,AvgCGPA
WHERE students.cgpa>AvgCGPA.avg_cgpa;


-- Department statistics

WITH DeptStats AS
(
SELECT
department_id,
COUNT(*) total_students
FROM students
GROUP BY department_id
)

SELECT *
FROM DeptStats;