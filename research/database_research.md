# Day 02 – Database Design, SQL Fundamentals & Backend Database Architecture

**Date:** 15 July 2026

---

# Objective

Today's objective was to strengthen my understanding of relational databases, database design, SQL, query optimization, and how databases are designed to support backend APIs for modern web applications.

---

# Topics Covered

## 1. Database Fundamentals

Revised the core concepts of relational databases and how they are used within modern web applications.

Topics covered:

- Database vs DBMS
- Why relational databases are used
- SQL as a database query language
- PostgreSQL architecture
- Client → Backend → Database workflow
- Data flow inside a web application

Typical request flow:

```

Frontend (React)

↓

FastAPI Backend

↓

PostgreSQL Database

↓

JSON Response

↓

Frontend

```

This reinforced the understanding that the frontend should never communicate directly with the database. The backend is responsible for authentication, authorization, validation, business logic, and database interaction.

---

## 2. Relational Database Mapping

Revised how data is modeled using entities and relationships.

Relationship types studied:

- One-to-One
- One-to-Many
- Many-to-Many

Important concepts:

- Primary Keys
- Foreign Keys
- Junction Tables
- Entity Relationship (ER) Design

The emphasis was on identifying real-world entities first and then defining relationships between them before creating tables.

---

## 3. Database Normalization

Reviewed normalization principles for reducing redundancy and improving maintainability.

Normal Forms Covered:

- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

Also revised common database anomalies:

- Insert Anomaly
- Update Anomaly
- Delete Anomaly

Normalization ensures data consistency while reducing unnecessary duplication.

---

## 4. SQL Revision

Revised SQL command categories.

### DDL (Data Definition Language)

- CREATE
- ALTER
- DROP
- TRUNCATE

### DML (Data Manipulation Language)

- INSERT
- UPDATE
- DELETE

### DQL (Data Query Language)

- SELECT

### DCL (Data Control Language)

- GRANT
- REVOKE

### TCL (Transaction Control Language)

- COMMIT
- ROLLBACK
- SAVEPOINT

---

## 5. SQL Practice

Created a complete relational database for a University Management System.

Tables designed:

- Departments
- Teachers
- Students
- Courses
- Enrollments

Relationships implemented using foreign keys.

Practical SQL topics practiced:

- Table creation
- Primary Keys
- Foreign Keys
- Data Types
- Constraints
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- Aggregate Functions
- GROUP BY
- HAVING
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- Views
- Indexes
- EXPLAIN
- EXPLAIN ANALYZE
- PostgreSQL built-in functions

SQL practice files were organized separately to maintain a structured learning repository.

---

## 6. Database Design for Backend APIs

Studied how modern backend systems are designed around application features and API requirements rather than simply creating database tables.

Key idea:

Features → APIs → Database Design

Instead of beginning with tables, the recommended workflow is:

1. Identify application requirements.
2. Identify entities.
3. Define relationships.
4. Design REST APIs.
5. Design database schema.
6. Implement backend logic.

This approach keeps the database aligned with business requirements.

---

## 7. CRUD Mapping

Reviewed how REST APIs map directly to SQL operations.

| REST API    | SQL                  |
| ----------- | -------------------- |
| POST        | INSERT               |
| GET         | SELECT               |
| PUT / PATCH | UPDATE               |
| DELETE      | DELETE / Soft Delete |

This mapping is fundamental when developing FastAPI applications.

---

## 8. Database Design Best Practices

Studied several practices commonly used in production systems.

Topics included:

- Naming conventions
- Audit columns
- created_at
- updated_at
- deleted_at
- Soft Deletes vs Hard Deletes
- UUID vs SERIAL Primary Keys
- Designing databases around API requirements
- Thinking in terms of business entities instead of tables

---

## 9. Query Optimization

Studied different methods of improving database performance.

Topics researched:

- Indexes
- Composite Indexes
- Query Planning
- EXPLAIN
- EXPLAIN ANALYZE
- Efficient JOIN usage
- Selecting only required columns
- Avoiding unnecessary table scans

Also introduced to PostgreSQL indexing strategies including B-Tree and GiST indexes (commonly used with PostGIS).

---

## 10. Learning Resources

### Video

Database Design Course – freeCodeCamp

Completed the database design course to reinforce concepts related to relational database modeling and schema design.

Additional references:

- PostgreSQL Documentation
- ByteByteGo
- Lucidchart ER Diagram Tutorials

---

--
