CREATE VIEW student_course_view AS

SELECT s.first_name, c.course_name, e.marks
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
JOIN courses c
ON c.course_id=e.course_id;



SELECT * FROM student_course_view;