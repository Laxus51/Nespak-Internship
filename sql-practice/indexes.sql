-- Normal Index

CREATE INDEX idx_student_email
ON students(email);


-- Composite Index

CREATE INDEX idx_course_department
ON courses
(department_id,teacher_id);

-- Unique index

CREATE UNIQUE INDEX idx_teacher_email

ON teachers(email);