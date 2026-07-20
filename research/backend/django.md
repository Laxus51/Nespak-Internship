## Django Framework Fundamentals

Today I started learning Django as the backend framework for the internship project.

Unlike FastAPI, Django is a full-stack web framework that includes many built-in features such as an ORM, authentication system, migrations, admin panel, and security mechanisms.

### Django Architecture

A Django application is organized into a **Project** containing multiple **Apps**. Each app is responsible for a specific business domain, making the application modular and easier to maintain.

Example apps for a WebGIS system include:

- Users
- Organizations
- Assets
- Inspections
- Maintenance
- Dashboard
- AI Chatbot

### Django ORM

Instead of SQLAlchemy, Django provides its own Object Relational Mapper (ORM), allowing database tables to be represented as Python classes.

### Migrations

Django includes a built-in migration system for managing database schema changes using:

- `python manage.py makemigrations`
- `python manage.py migrate`

### Django Admin

One of Django's strongest features is the built-in Admin Panel, which provides a complete web interface for managing database records without developing a separate frontend.

### Django REST Framework

For building REST APIs, Django is commonly paired with **Django REST Framework (DRF)**. DRF provides serializers, authentication, pagination, permissions, and API tooling, making it the standard choice for modern Django backend development.

### Key Learnings

- Django follows a modular architecture using Projects and Apps.
- Django includes a built-in ORM, migration system, and administrative interface.
- Django REST Framework is the preferred solution for developing RESTful APIs in Django.
- Compared to FastAPI, Django offers more built-in functionality at the cost of being a larger framework.

---

## Setting Up the Django Backend

Today I initialized the backend for the WebGIS internship project using Django and Django REST Framework.

### Project Setup

The backend project was configured with:

- Django
- Django REST Framework (DRF)
- PostgreSQL database connection
- CORS support for future frontend integration

### Django Project Structure

The project follows Django's standard architecture with a central project (`config`) and modular applications (`apps`) that encapsulate different business domains.

### Database-First Development

Unlike many tutorials where Django models create database tables, this project follows a **database-first** approach. The spatial data already exists in PostgreSQL/PostGIS after being imported from QGIS. Django will generate models from the existing database schema using the `inspectdb` command.

### Key Learnings

- Django projects are organized into reusable applications.
- Django REST Framework is the standard choice for building REST APIs.
- Existing PostgreSQL databases can be integrated into Django without recreating tables.
- The backend architecture is now prepared to expose spatial data through REST endpoints.

---

## Building a CRUD API with Django REST Framework

Today I built my first REST API using Django REST Framework (DRF).

### Architecture

The API follows the standard DRF architecture:

Model → Serializer → ViewSet → URL Router

- **Model** defines the database structure.
- **Serializer** converts model instances to and from JSON.
- **ViewSet** implements CRUD operations.
- **Router** automatically generates RESTful endpoints.

### ModelViewSet

DRF's `ModelViewSet` provides built-in CRUD functionality, reducing boilerplate code. A single ViewSet automatically supports:

- GET (List)
- GET (Retrieve)
- POST (Create)
- PUT (Update)
- PATCH (Partial Update)
- DELETE (Delete)

### API Endpoints

The following endpoints were generated automatically:

- `GET /api/stations/`
- `GET /api/stations/{id}/`
- `POST /api/stations/`
- `PUT /api/stations/{id}/`
- `PATCH /api/stations/{id}/`
- `DELETE /api/stations/{id}/`

### Key Learnings

- DRF simplifies API development through serializers, viewsets, and routers.
- Serializers handle conversion between Python objects and JSON.
- ViewSets encapsulate standard CRUD operations.
- Routers generate RESTful URL patterns automatically, reducing manual routing configuration.

---


## Working with Existing Databases in Django

Today I learned that Django supports both **code-first** and **database-first** development approaches.

### Code-First Development

In a code-first workflow, developers define Django models first. Database tables are then created using migrations.

Model → Migration → Database

### Database-First Development

In many enterprise projects, the database already exists. Django can generate model definitions from existing database tables using the `inspectdb` command.

```bash
python manage.py inspectdb
```
