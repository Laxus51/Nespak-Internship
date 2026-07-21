
# WebGIS Backend

This repository contains the backend of the WebGIS internship project built using Django, Django REST Framework, GeoDjango, PostgreSQL, and PostGIS.

---

# Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- GeoDjango
- PostgreSQL
- PostGIS

---

# Project Structure

```
backend/
│
├── config/                 # Django project configuration
├── webgis/                 # Main application
│   ├── models/
│   ├── serializers/
│   ├── viewsets/
│   └── urls.py
│
├── research/               # Learning notes and documentation
└── manage.py
```

The project follows a modular architecture where each spatial layer has its own:

- Model
- Serializer
- ViewSet

---

# Current Spatial Layers

The backend currently exposes REST APIs for:

- NYC Subway Stations
- NYC Neighborhoods
- NYC Streets
- NYC Census Blocks
- NYC Homicides

These datasets are stored inside PostgreSQL/PostGIS and accessed using GeoDjango.

---

# Implemented Features

## REST APIs

CRUD-style endpoints have been created using Django REST Framework ViewSets.

Example endpoints:

```
/api/stations/
/api/neighborhoods/
/api/streets/
/api/homicides/
/api/census-blocks/
```

---

## Spatial Queries

The backend currently supports:

### Bounding Box Search

Returns only the stations currently visible inside the user's map extent.

```
GET /api/stations/bbox/
```

---

### Nearest Station

Returns the closest subway station to a given coordinate.

```
GET /api/stations/nearest/
```

---

### Radius Search

Returns all subway stations within a specified radius.

```
GET /api/stations/within_radius/
```

---

# Database

Spatial data is stored in PostgreSQL with the PostGIS extension enabled.

GeoDjango is configured to use the PostGIS backend, allowing spatial operations directly through Django's ORM.

Spatial datasets are imported from GIS sources and integrated using a database-first workflow.

---

# Current Architecture

```
PostGIS
      │
      ▼
GeoDjango Models
      │
      ▼
Serializers
      │
      ▼
ViewSets
      │
      ▼
REST API
      │
      ▼
Frontend (React)
```

---

# Current Status

Implemented:

- Django project setup
- PostgreSQL integration
- GeoDjango configuration
- Database-first development
- Existing PostGIS model integration
- DRF serializers
- Read-only ViewSets
- Multiple spatial datasets
- Bounding-box filtering
- Nearest feature search
- Radius search

Future work will focus on additional spatial analysis, performance optimization, authentication, and frontend integration.
