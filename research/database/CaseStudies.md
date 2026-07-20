# Database Design Case Study – Banking Systems

Today I studied how banking applications influence database design decisions. Unlike many other applications, banking systems prioritize data consistency, integrity, auditability, and reliability over raw performance.

## Core Entities

A typical banking database consists of entities such as:

- Customer
- Account
- Transaction
- Loan
- Card
- Branch
- Employee
- ATM

The Account entity serves as the central component, linking customers with financial transactions and banking services.

## Why Relational Databases?

Banking applications commonly use relational databases such as PostgreSQL, Oracle Database, Microsoft SQL Server, or IBM Db2 because they provide:

- ACID transactions
- Referential integrity
- Strong consistency
- Rollback capabilities
- Support for complex relationships

These features are essential when managing financial data.

## Important Design Principles

### Transaction-Based Design

Financial operations are stored as individual transactions rather than simply updating account balances. This creates a complete financial history and enables accurate auditing.

### Audit Logging

Every important action is recorded, including who performed it, when it occurred, and what changes were made. Audit logs support regulatory compliance and troubleshooting.

### Soft Deletes

Customer records are rarely deleted. Instead, accounts are marked with statuses such as Active, Suspended, or Closed to preserve historical information.

### High Availability

Banking systems must support millions of users while maintaining data integrity. Techniques such as indexing, connection pooling, partitioning, replication, and backup strategies are used to ensure performance and reliability.

## Key Learnings

- Database design should be driven by business requirements.
- Banking systems prioritize consistency and reliability over maximum performance.
- Financial transactions should be stored permanently to maintain a complete audit trail.
- Relational databases are well suited for banking because of their transactional guarantees and strong consistency.

---

# Database Design for Different Applications

Today I studied how database design changes depending on the application's business requirements rather than following a single universal approach.

## Banking Systems

Banking databases prioritize ACID transactions, consistency, audit logs, and data integrity. Financial transactions are stored permanently, and customer records are rarely deleted.

## University Management Systems

University databases focus on managing structured relationships between students, teachers, courses, departments, enrollments, exams, and grades. They are highly normalized to reduce redundancy and support reporting.

## E-Commerce Systems

E-commerce databases manage customers, products, orders, payments, reviews, and inventory. They emphasize transactional consistency for order processing while supporting high read performance for product browsing.

## AI Applications

Modern AI applications typically use multiple database technologies. Relational databases manage users and application data, vector databases store embeddings for semantic search, and Redis is commonly used for caching and session management.

## Social Media Applications

Social media databases must support millions of concurrent interactions, including posts, comments, likes, follows, and messages. Performance and scalability are primary design goals, often requiring a combination of relational databases, caching systems, and NoSQL technologies.

## GIS Applications

GIS databases extend traditional relational databases with spatial data types and spatial indexing. PostgreSQL with PostGIS is widely used because it supports geometry storage, spatial indexing, distance calculations, and advanced spatial analysis.

## Key Learnings

- Database design should always reflect business requirements.
- Different applications prioritize different characteristics such as consistency, scalability, relationships, or spatial analysis.
- PostgreSQL is versatile enough to support many application domains, while specialized technologies such as vector databases and PostGIS extend its capabilities for AI and GIS workloads.
