
# GeoDjango Spatial Queries

## Introduction

Unlike traditional databases that work with numbers and text, GIS databases also store geometric objects such as points, lines, and polygons. GeoDjango extends Django by providing native support for querying these spatial objects using the Django ORM.

---

## Bounding Box Queries

A Bounding Box (BBox) represents the rectangular area currently visible on a map. Instead of requesting every feature from the database, the frontend sends the coordinates of the visible area to the backend.

Example request:

```
GET /api/stations/bbox?xmin=...&ymin=...&xmax=...&ymax=...
```

The backend returns only the features that fall inside the bounding box.

This approach significantly reduces:

- Database load
- Network traffic
- API response time
- Browser rendering time

Bounding box queries are one of the most common operations in WebGIS applications.

---

## How GeoDjango Works

GeoDjango converts spatial ORM queries into PostGIS SQL functions.

For a bounding box query, GeoDjango generates SQL similar to:

```sql
SELECT *
FROM nyc_subway_stations
WHERE ST_Intersects(
    geom,
    ST_MakeEnvelope(xmin, ymin, xmax, ymax, 26918)
);
```

Where:

- `geom` is the geometry column.
- `ST_MakeEnvelope()` creates the rectangular search area.
- `ST_Intersects()` checks whether a feature lies inside or intersects that area.

---

## Spatial Indexing

Large GIS datasets may contain millions of features. Searching every geometry individually would be computationally expensive.

PostGIS uses a **GiST (Generalized Search Tree)** index for geometry columns.

Unlike a B-Tree index, which is optimized for scalar values, a GiST index understands spatial data by indexing the bounding boxes of geometries.

During a spatial query:

1. The GiST index quickly identifies candidate geometries.
2. PostGIS performs precise spatial calculations only on those candidates.
3. Matching features are returned to the application.

This greatly improves the performance of spatial queries on large datasets.

---

## Key Learnings

- GeoDjango enables spatial queries through Django's ORM.
- Bounding box queries return only features visible on the current map.
- GeoDjango translates ORM operations into PostGIS spatial functions.
- GiST indexes optimize geometry searches and are essential for scalable WebGIS applications.
