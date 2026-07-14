-- INNER JOIN

SELECT s.first_name, c.course_name
FROM students s
INNER JOIN enrollments e
ON s.student_id=e.student_id
INNER JOIN courses c
ON c.course_id=e.course_id;


-- LEFT JOIN

SELECT d.department_name, t.first_name
FROM departments d
LEFT JOIN teachers t
ON d.department_id=t.department_id;


-- RIGHT JOIN

SELECT c.course_name, e.semester
FROM enrollments e
RIGHT JOIN courses c
ON c.course_id=e.course_id;


-- FULL OUTER JOIN

SELECT *
FROM students
FULL JOIN enrollments
ON students.student_id=enrollments.student_id;