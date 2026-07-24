
# PostGIS Query Optimization and Execution Plans

## Overview

Today's session focused on understanding how PostgreSQL and PostGIS execute spatial queries efficiently using spatial indexes and query execution plans.

---

# Why Spatial Indexes Are Needed

Without an index, PostgreSQL must compare every geometry.

Example:

```
Street 1
Street 2
Street 3
...
Street 19,000
```

Every feature must be checked.

This is called a Sequential Scan.

---

# GiST Spatial Index

PostGIS stores geometry indexes using GiST (Generalized Search Tree).

Conceptually, this behaves similarly to an R-Tree.

Instead of indexing complete polygons, PostGIS indexes each geometry's Minimum Bounding Rectangle (MBR).

This allows PostgreSQL to quickly identify candidate geometries before performing expensive geometric calculations.

---

# Bounding Box Filtering

The spatial index first checks:

```
Bounding Box A
overlaps
Bounding Box B
```

represented internally as

```sql
geom && other_geometry
```

Only after this fast filtering step does PostGIS execute expensive predicates such as

- ST_Contains()
- ST_Within()
- ST_Intersects()

---

# Execution Plan Analysis

Query used:

```sql
EXPLAIN ANALYZE
SELECT *
FROM nyc_streets
WHERE ST_Intersects(
    geom,
    (
        SELECT geom
        FROM nyc_neighborhoods
        WHERE id = 1
    )
);
```

Important observations:

## Bitmap Index Scan

```
Bitmap Index Scan on sidx_nyc_streets_geom
```

Meaning:

- PostgreSQL successfully used the spatial index.
- Candidate geometries were identified using bounding boxes.

---

## Bitmap Heap Scan

```
Bitmap Heap Scan
```

Meaning:

- Candidate rows were loaded efficiently from disk.
- PostgreSQL grouped page accesses together for improved performance.

---

## Filter

```
ST_Intersects(...)
```

The exact geometry comparison was performed only after the index reduced the candidate set.

Example:

```
200 candidate roads
↓

99 rejected

↓

101 valid intersections
```

---

## Index Scan

```
Index Scan using nyc_neighborhoods_pkey
```

The neighborhood was retrieved using the primary key index.

---

## Execution Time

Execution time was approximately

```
47 ms
```

showing that the spatial index was working correctly.

---

# Sequential Scan

Example:

```
Seq Scan
```

Meaning:

Every row in the table is examined.

Usually indicates either

- no suitable index exists, or
- PostgreSQL estimates that scanning the whole table is cheaper.

---

# Cost-Based Optimizer

PostgreSQL decides automatically whether an index should be used.

Indexes are **not** always beneficial.

Example:

```sql
SELECT *
FROM nyc_streets;
```

Since every row is required, PostgreSQL will normally perform a Sequential Scan instead of using the index.

Reading the table sequentially is faster than traversing the index and then visiting every row.

---

# When Indexes Are Useful

Indexes provide the greatest benefit when filtering data.

Examples:

```sql
WHERE id = 5
```

```sql
WHERE borough = 'Manhattan'
```

```sql
WHERE ST_Contains(...)
```

```sql
WHERE ST_Within(...)
```

```sql
WHERE ST_Intersects(...)
```

---

# Practical Lessons

- GiST indexes dramatically improve spatial query performance.
- Spatial indexes work on bounding boxes before exact geometry comparisons.
- Bitmap Index Scans indicate efficient index usage.
- Bitmap Heap Scans efficiently retrieve candidate rows from disk.
- Execution plans should always be inspected using `EXPLAIN ANALYZE` when optimizing queries.
- A Sequential Scan is not always bad; sometimes it is the optimal execution strategy.

---

# Key Takeaways

- Understand how GiST indexes work.
- Learn to interpret `EXPLAIN ANALYZE`.
- Differentiate between Bitmap Index Scan, Bitmap Heap Scan, Index Scan, and Sequential Scan.
- Recognize that PostgreSQL chooses execution plans using a cost-based optimizer rather than always preferring indexes.
