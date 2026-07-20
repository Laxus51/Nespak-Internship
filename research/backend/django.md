
# Django Framework Fundamentals

Today I began learning Django as the backend framework for the internship project.

Unlike FastAPI, Django is a full-stack web framework that includes many built-in features such as an ORM, authentication, migrations, an admin panel, and security mechanisms.

---

## Django Architecture

A Django application is organized into a **Project** containing multiple **Apps**. Each app is responsible for a specific business domain, making the application modular and maintainable.

Example apps for a WebGIS system:

- Users
- Organizations
- Assets
- Inspections
- Maintenance
- Dashboard
- AI Chatbot

---

## Django ORM

Django provides its own Object Relational Mapper (ORM), allowing database tables to be represented as Python classes instead of writing SQL directly.

---

## Migrations

Django manages database schema changes through migrations.

Common commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Django Admin

Django includes a built-in Admin Panel for managing application data through a web interface without developing a separate frontend.

---

## Django REST Framework (DRF)

Django REST Framework extends Django for API development by providing:

- Serializers
- ViewSets
- Routers
- Authentication
- Permissions
- Pagination

It is the standard framework for building REST APIs with Django.

---

# Setting Up the Backend

The backend was configured with:

- Django
- Django REST Framework
- PostgreSQL
- PostGIS
- CORS support

The project follows a **database-first** approach where existing spatial tables are imported into Django using:

```bash
python manage.py inspectdb
```

instead of creating database tables from Django models.

---

# Building a CRUD API

A simple CRUD API was developed using Django REST Framework.

Architecture:

```
Model → Serializer → ViewSet → Router
```

Responsibilities:

- **Model** → Represents database tables.
- **Serializer** → Converts Python objects to/from JSON.
- **ViewSet** → Implements API operations.
- **Router** → Automatically generates REST endpoints.

Generated endpoints:

- GET `/api/stations/`
- GET `/api/stations/{id}/`
- POST `/api/stations/`
- PUT `/api/stations/{id}/`
- PATCH `/api/stations/{id}/`
- DELETE `/api/stations/{id}/`

---

# Working with Existing Databases

Django supports two development workflows.

### Code-First

```
Model → Migration → Database
```

The database schema is generated from Django models.

### Database-First

```
Existing Database → inspectdb → Django Models
```

The database already exists and Django generates model definitions from it.

This approach is common when integrating legacy or enterprise databases.

---

# GeoDjango Fundamentals

GeoDjango extends Django with native GIS support for working with PostGIS databases.

During setup:

- Configured Django to use the PostGIS database backend.
- Configured the required GDAL library from the existing QGIS installation.
- Verified the GeoDjango environment using the Django shell.

The imported geometry field was converted from a generic `TextField` to a native `PointField`.

```python
geom = models.PointField(srid=26918)
```

This allows Django to understand spatial data instead of treating it as plain text.

---

# GeoDjango Capabilities

Using GeoDjango enables spatial operations directly through Django's ORM.

Examples include:

- Distance calculations
- Bounding box queries
- Spatial intersections
- Containment tests
- Nearest-neighbor searches

Instead of writing raw PostGIS SQL, spatial queries can be expressed using Django's ORM.

---

# Key Learnings

- Django organizes applications into modular apps.
- Django REST Framework simplifies API development using serializers, viewsets, and routers.
- Django supports both code-first and database-first workflows.
- Existing PostGIS databases can be integrated using `inspectdb`.
- GeoDjango enables native spatial data support through `PointField` and the PostGIS backend.
- Spatial queries can be performed through Django's ORM without writing raw SQL.
