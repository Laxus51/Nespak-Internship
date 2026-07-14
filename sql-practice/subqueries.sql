SELECT *
FROM students
WHERE cgpa >
(
SELECT AVG(cgpa) FROM students
);


SELECT *
FROM teachers
WHERE salary=
(
SELECT MAX(salary)
FROM teachers
);