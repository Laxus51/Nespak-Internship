CREATE TABLE departments
(
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE NOT NULL,
    building VARCHAR(100)
);

CREATE TABLE teachers
(
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    salary NUMERIC(10,2),
    department_id INT REFERENCES departments(department_id)
);

CREATE TABLE students
(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    cgpa NUMERIC(3,2),
    department_id INT REFERENCES departments(department_id)
);

CREATE TABLE courses
(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    credit_hours INT,
    teacher_id INT REFERENCES teachers(teacher_id),
    department_id INT REFERENCES departments(department_id)
);

CREATE TABLE enrollments
(
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    semester VARCHAR(20),
    marks INT
);