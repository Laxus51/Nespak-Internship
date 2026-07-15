-- B-Tree Index
CREATE INDEX idx_students_email
ON students(email);

-- Foreign Key Index
CREATE INDEX idx_students_department
ON students(department_id);

-- Composite Index
CREATE INDEX idx_courses_department_teacher
ON courses(department_id, teacher_id);

-- Partial Index
CREATE INDEX idx_active_students
ON students(student_id)
WHERE cgpa >= 3.5;

-- GiST Index 

-- CREATE INDEX idx_assets_geom
-- ON assets
-- USING GIST (geom);

-- GIN Index 

-- CREATE INDEX idx_metadata
-- ON projects
-- USING GIN (metadata);