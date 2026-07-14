SELECT COUNT(*) FROM students;

SELECT AVG(cgpa) FROM students;

SELECT MAX(salary) FROM teachers;

SELECT MIN(marks) FROM enrollments;

SELECT SUM(salary) FROM teachers;


SELECT department_id, COUNT(*)
FROM students
GROUP BY department_id;


SELECT department_id, COUNT(*)
FROM students
GROUP BY department_id
HAVING COUNT(*)>5;