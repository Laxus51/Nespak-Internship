# Database Design, SQL Fundamentals & Backend Database Architecture

**Date:** 14 July 2026

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

# PostgreSQL Internals & Storage Architecture

**Date:** 15 July 2026

## Query Execution Pipeline

Every SQL query passes through multiple stages before returning the result:

```
Client Application
        │
        ▼
SQL Query
        │
        ▼
Parser
        │
        ▼
Planner / Optimizer
        │
        ▼
Executor
        │
        ▼
Storage Engine
        │
        ▼
Disk Pages
```

### Parser

The parser validates the SQL syntax and checks whether the referenced tables and columns exist. If an error is found, execution stops before the query reaches the database engine.

### Planner / Optimizer

The PostgreSQL query planner estimates the cost of different execution strategies and selects the most efficient one. It decides whether to perform operations such as sequential scans, index scans, or different join algorithms based on available statistics and indexes.

### Executor

The executor follows the execution plan generated by the planner and retrieves or modifies the required data.

## PostgreSQL Storage

Unlike spreadsheets, PostgreSQL does not store data row-by-row in a single file. Data is organized into fixed-size **8 KB pages**, with each table consisting of many pages containing rows (tuples).

This page-based storage improves disk I/O efficiency and enables PostgreSQL to process large datasets effectively.

---

## Heap Tables

By default, PostgreSQL stores tables as **heap tables**, meaning rows are not physically stored in sorted order. Data retrieval order is determined using indexes when necessary rather than relying on physical row placement.

---

## Multi-Version Concurrency Control (MVCC)

PostgreSQL uses MVCC (Multi-Version Concurrency Control) to allow multiple users to read and modify data simultaneously without blocking each other.

Instead of modifying rows directly, PostgreSQL creates a new version of the row while keeping the previous version available for active transactions. This significantly improves concurrency in multi-user applications.

Benefits include:

- Reduced locking
- Higher concurrency
- Better read performance
- Improved scalability for web applications

---

## Write-Ahead Logging (WAL)

Before modifying actual table data, PostgreSQL records every change in the **Write-Ahead Log (WAL)**.

This mechanism ensures that if the database crashes unexpectedly, PostgreSQL can recover committed transactions by replaying the WAL logs, maintaining database consistency and durability.

---

## VACUUM and AUTOVACUUM

Because MVCC creates multiple row versions, outdated tuples remain in storage after updates and deletes.

The **VACUUM** process removes obsolete row versions and reclaims storage space. PostgreSQL automatically performs this maintenance through **AUTOVACUUM**, which helps maintain database performance without manual intervention.

---

## Transactions

Transactions group multiple SQL operations into a single unit of work.

Using **BEGIN**, **COMMIT**, and **ROLLBACK**, PostgreSQL guarantees that either all operations succeed together or none are applied if an error occurs.

This ensures data consistency and is especially important in financial systems, inventory management, and other applications where partial updates cannot be allowed.

---

## Key Takeaways

- PostgreSQL processes every query through the Parser, Planner, Executor, and Storage Engine.
- Data is stored internally using fixed-size pages rather than simple tables.
- Heap tables store rows without maintaining physical order.
- MVCC enables concurrent read and write operations without excessive locking.
- WAL provides crash recovery and ensures data durability.
- VACUUM removes obsolete row versions created by MVCC.
- Transactions maintain consistency by ensuring atomic execution of related operations.

---

# Query Execution Plans using EXPLAIN

Studied how PostgreSQL generates execution plans using the `EXPLAIN` and `EXPLAIN ANALYZE` commands.

## Topics Covered

- Difference between EXPLAIN and EXPLAIN ANALYZE
- Sequential Scan
- Index Scan
- Bitmap Index Scan
- Nested Loop Join
- Hash Join
- Merge Join
- Query Cost Estimation
- Planner Statistics
- ANALYZE command

## Key Learnings

- EXPLAIN displays PostgreSQL's estimated execution strategy.
- EXPLAIN ANALYZE executes the query and reports actual performance metrics.
- Sequential Scans are efficient for small tables but expensive on large datasets.
- Index Scans significantly improve lookup performance when suitable indexes exist.
- PostgreSQL automatically chooses the lowest-cost execution plan based on table statistics.
- ANALYZE updates planner statistics to improve execution plan accuracy.

Understanding execution plans is an essential skill for diagnosing slow queries and optimizing backend API performance.

---

Backend Database Performance Best Practices

Studied practical techniques used to improve database performance in modern backend applications.

## Topics Covered

- Avoiding `SELECT *`
- Pagination using LIMIT/OFFSET
- Keyset (Cursor) Pagination
- Avoiding the N+1 Query Problem
- Batch Inserts
- Connection Pooling
- Caching Frequently Accessed Data
- Proper Indexing Strategies
- Minimizing Unnecessary JOINs
- Database Transactions
- Monitoring Slow Queries using EXPLAIN ANALYZE
- FastAPI and PostgreSQL Performance Best Practices

## Key Learnings

- Retrieve only the data required by an API.
- Use pagination to efficiently handle large datasets.
- Reduce database round trips by avoiding N+1 queries.
- Reuse database connections through connection pooling.
- Index only frequently queried columns.
- Use transactions to ensure data consistency.
- Optimize queries based on execution plans rather than assumptions.
- Efficient database interaction is as important as efficient SQL.

Understanding these practices helps build scalable, maintainable, and high-performance backend systems.
