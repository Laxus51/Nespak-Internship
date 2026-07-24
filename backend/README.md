# WebGIS Backend

This repository contains the backend of the WebGIS internship project built using **Django**, **Django REST Framework**, **GeoDjango**, **PostgreSQL**, and **PostGIS**.

The backend exposes REST APIs for querying and analyzing spatial datasets through GeoDjango and PostGIS while following a modular architecture.

---

# Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* GeoDjango
* PostgreSQL
* PostGIS

---

# Project Structure

```
backend/
│
├── config/                     # Django project configuration
├── webgis/
│   ├── models/                 # Database models (one file per dataset)
│   ├── serializers/            # DRF serializers
│   ├── viewsets/               # API endpoints
│   ├── urls.py                 # API routes
│   └── admin.py
│
├── research/                   # Learning notes & documentation
└── manage.py
```

The project follows a modular architecture where every spatial dataset has its own:

* Model
* Serializer
* ViewSet

Analytics endpoints are organized separately from resource endpoints.

---

# Spatial Datasets

The backend currently provides APIs for the following PostGIS datasets:

* NYC Subway Stations
* NYC Neighborhoods
* NYC Streets
* NYC Census Blocks
* NYC Homicides

All datasets are stored inside PostgreSQL/PostGIS and accessed through GeoDjango.

---

# REST API Endpoints

## Resource Endpoints

```
/api/stations/
/api/neighborhoods/
/api/streets/
/api/homicides/
/api/census-blocks/
```

---

# Spatial Query Endpoints

## Bounding Box Search

Returns only the subway stations visible inside the current map extent.

```
GET /api/stations/bbox/
```

---

## Nearest Subway Station

Returns the closest subway station to a given coordinate.

```
GET /api/stations/nearest/
```

---

## Radius Search

Returns every subway station within a specified search radius.

```
GET /api/stations/within_radius/
```

---

## Neighborhood of a Station

Returns the neighborhood containing a selected subway station.

```
GET /api/stations/{id}/neighborhood/
```

---

## Stations Inside a Neighborhood

Returns every subway station located inside a selected neighborhood.

```
GET /api/neighborhoods/{id}/subway_stations/
```

---

## Neighborhood Details

Returns a complete spatial summary of a neighborhood, including:

* Neighborhood information
* Subway stations
* Streets
* Homicides
* Census blocks

```
GET /api/neighborhoods/{id}/details/
```

---

# Dashboard & Analytics APIs

The backend also includes analytics endpoints that are not tied to a single database model.

## Top Neighborhoods

Returns the neighborhoods containing the highest number of subway stations.

```
GET /api/dashboard/top_neighborhoods/
```

Supports an optional limit parameter:

```
GET /api/dashboard/top_neighborhoods?limit=5
```

This endpoint demonstrates:

* Raw SQL execution
* Spatial joins using PostGIS
* Aggregation (COUNT)
* GROUP BY
* ORDER BY
* Custom DRF serializers
* Analytics ViewSets

---

# Database

Spatial data is stored in PostgreSQL with the PostGIS extension enabled.

GeoDjango is configured to use the PostGIS backend, allowing spatial queries directly through Django's ORM while also supporting raw SQL for advanced analytics and reporting.

The project follows a database-first workflow where existing PostGIS datasets are imported into PostgreSQL and mapped into Django models.

---

# Current Architecture

```
                    PostgreSQL + PostGIS
                            │
                            ▼
                    GeoDjango Models
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
 Resource ViewSets                      Dashboard ViewSets
        │                                       │
        ▼                                       ▼
     Serializers                      Custom Serializers
        │                                       │
        └───────────────────┬───────────────────┘
                            ▼
                         REST API
                            │
                            ▼
                    React Frontend
```

---

# Implemented Features

* Django project setup
* PostgreSQL/PostGIS integration
* GeoDjango configuration
* Database-first development
* Modular project structure
* Read-only REST APIs
* Multiple spatial datasets
* Bounding-box filtering
* Nearest feature search
* Radius search
* Point-in-polygon queries
* Polygon-to-point spatial relationships
* Neighborhood detail endpoint
* Dashboard analytics endpoints
* Raw SQL reporting
* Spatial aggregation using PostGIS
