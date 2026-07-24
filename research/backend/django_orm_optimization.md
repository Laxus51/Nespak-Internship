
# Django ORM Optimization

## Overview

Today focused on understanding how to write efficient Django ORM queries and choosing the correct ORM methods based on the problem being solved. The emphasis was on reducing unnecessary database queries, minimizing transferred data, and understanding the difference between aggregation and annotation.

---

# Aggregate vs Annotate

Although both functions perform calculations, they solve different problems.

## aggregate()

`aggregate()` computes a single summary value for the entire queryset.

Examples:

- Total number of records
- Average salary
- Maximum value
- Minimum value

Example:

```python
Employee.objects.aggregate(
    total=Count("id"),
    average_salary=Avg("salary")
)
```

Returns

```python
{
    "total": 523,
    "average_salary": 78500
}
```

The queryset is collapsed into a single dictionary.

---

## annotate()

`annotate()` keeps every object in the queryset but attaches additional computed values.

Example:

```python
Department.objects.annotate(
    employee_count=Count("employee")
)
```

Each Department object now contains an additional field.

Example:

```
HR          -> 23
Finance     -> 17
IT          -> 51
```

Unlike `aggregate()`, it returns a queryset rather than a single dictionary.

---

# Why Raw SQL Was Used Instead of annotate()

In the WebGIS project, neighborhoods and subway stations are not connected through a ForeignKey relationship.

Instead, they are related spatially.

```
Neighborhood Polygon
        contains
Station Point
```

Since Django ORM cannot automatically infer this spatial relationship, PostGIS functions such as `ST_Contains()` must be used.

Example:

```sql
ST_Contains(neighborhood.geom, station.geom)
```

This is why the dashboard endpoint was implemented using raw SQL instead of ORM annotations.

---

# N+1 Query Problem

Example:

```python
employees = Employee.objects.all()

for employee in employees:
    print(employee.department.name)
```

If there are 100 employees:

- 1 query retrieves employees.
- 100 additional queries retrieve departments.

Total:

```
101 queries
```

This problem is known as the N+1 Query Problem.

---

# select_related()

Used for:

- ForeignKey
- OneToOneField

Example:

```python
Employee.objects.select_related("department")
```

Django performs a SQL JOIN, reducing many queries into a single query.

---

# prefetch_related()

Used for:

- ManyToMany relationships
- Reverse ForeignKeys

Example:

```python
Course.objects.prefetch_related("students")
```

Instead of performing a JOIN, Django executes separate queries and combines the results in Python.

---

# values()

Used when only a few fields are required.

Example:

```python
NycSubwayStation.objects.values(
    "name",
    "borough"
)
```

Returns dictionaries instead of model objects.

Useful for:

- APIs
- Dashboards
- Reports

---

# values_list()

Returns tuples.

Example:

```python
NycSubwayStation.objects.values_list("name")
```

Result:

```
("Times Sq",)
("Union Sq",)
```

Using

```python
flat=True
```

returns

```
[
    "Times Sq",
    "Union Sq"
]
```

Useful when only a single field is required.

---

# exists()

Used when only checking whether matching records exist.

Example:

```python
NycHomicide.objects.filter(
    geom__within=polygon
).exists()
```

Produces a very efficient query that stops after finding the first matching row.

---

# count()

Used when the total number of matching records is required.

Example:

```python
NycSubwayStation.objects.count()
```

Unlike `exists()`, the database must count every matching row.

---

# Choosing the Correct ORM Method

| Situation                   | Recommended Method     |
| --------------------------- | ---------------------- |
| Need all model fields       | all()                  |
| Need a few columns          | values()               |
| Need one column             | values_list(flat=True) |
| Need one summary            | aggregate()            |
| Need one summary per object | annotate()             |
| Need to check existence     | exists()               |
| Need total rows             | count()                |
| ForeignKey optimization     | select_related()       |
| ManyToMany optimization     | prefetch_related()     |

---

# Key Takeaways

- Use `aggregate()` for a single summary.
- Use `annotate()` to enrich queryset objects.
- Avoid the N+1 Query Problem using `select_related()` and `prefetch_related()`.
- Use `values()` and `values_list()` to reduce transferred data.
- Use `exists()` instead of retrieving objects when only checking for existence.
- Choose the ORM method based on the information actually required by the API.
