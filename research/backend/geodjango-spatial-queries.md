
# GeoDjango Spatial Queries

## Why Spatial Queries?

Returning every feature from the database is inefficient, especially when dealing with large GIS datasets. Even if the frontend only displays a small portion of the map, querying millions of records wastes database resources and increases response times.

Instead, the backend should return only the features relevant to the user's current map view or query.

---

## Spatial Indexing

Traditional B-Tree indexes are designed for exact comparisons and sorting, but they cannot efficiently answer questions such as:

- Which points lie inside this area?
- Which feature is closest?
- Which polygons intersect another polygon?

GeoDjango and PostGIS solve this using **GiST (Generalized Search Tree)** indexes.

GiST indexes understand spatial relationships, allowing PostGIS to eliminate large portions of the dataset before performing exact geometry calculations.

---

## Bounding Box Queries

The first spatial endpoint implemented returns only subway stations inside the current map extent.

Workflow:

1. Receive xmin, ymin, xmax and ymax.
2. Validate the input.
3. Construct a polygon representing the map extent.
4. Filter stations whose geometry intersects the bounding box.
5. Return only visible stations.

This significantly reduces the amount of data transferred between the database and the client.

---

## Nearest Feature Search

A nearest-station endpoint was implemented using GeoDjango's spatial functions.

Workflow:

1. Receive map coordinates.
2. Create a Point geometry.
3. Use PostGIS distance calculations.
4. Order stations by distance.
5. Return the closest station.

This demonstrates nearest-neighbor searching without manually computing distances for every record.

---

## Radius Search

Another endpoint returns all stations within a user-specified radius.

Workflow:

1. Receive coordinates and search radius.
2. Create a Point geometry.
3. Compute spatial distance.
4. Filter stations whose distance is less than the specified radius.
5. Sort results by distance.

This allows users to discover nearby stations efficiently.

---

## Additional Spatial Layers

The project was expanded by importing additional GIS datasets into PostGIS and exposing them through Django REST Framework.

Current layers include:

- Subway Stations
- Neighborhoods
- Streets
- Census Blocks
- Homicides

Each layer is represented by its own model, serializer, and ViewSet.

---

## Key Learnings

- Spatial databases should return only the data required by the client.
- GiST indexes enable efficient spatial searching.
- Bounding-box filtering greatly reduces unnecessary database load.
- GeoDjango integrates spatial operations directly into Django's ORM.
- Common GIS queries such as nearest-neighbor and radius searches can be implemented without writing raw SQL.
