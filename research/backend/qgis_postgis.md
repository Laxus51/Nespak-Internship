
# QGIS to PostGIS Workflow

Today I learned the standard workflow for importing GIS data into a spatial database.

## WebGIS Data Flow

In a typical WebGIS application, spatial data follows this pipeline:

Shapefile → QGIS → PostgreSQL + PostGIS → Backend API → Frontend Map

QGIS acts as a GIS client used to visualize, edit, and prepare spatial datasets before storing them in the database. The actual application communicates directly with PostgreSQL/PostGIS rather than with QGIS.

## Creating a PostGIS Database

A standard PostgreSQL database becomes a spatial database by enabling the PostGIS extension:

```sql
CREATE EXTENSION postgis;
```

The installation can be verified using:

```sql
SELECT PostGIS_Version();
```

## Connecting QGIS to PostgreSQL

QGIS connects directly to PostgreSQL using the database connection settings (host, port, database name, username, and password). Once connected, QGIS can read from and write to PostGIS tables.

## Importing Spatial Data

Shapefiles can be imported into PostGIS by using **Export → Save Features As...** and selecting PostgreSQL as the output format. During import, the geometry column and primary key are created in the target table.

## Verifying the Import

After importing, the spatial table can be inspected in PostgreSQL using SQL queries such as:

```sql
SELECT * FROM table_name LIMIT 10;
```

To visualize the geometry in a human-readable format:

```sql
SELECT id, ST_AsText(geom)
FROM table_name
LIMIT 5;
```

## Key Learnings

* QGIS is a GIS client and visualization tool, not a database.
* PostGIS is responsible for permanently storing spatial data.
* Spatial layers imported from QGIS become standard PostgreSQL tables with additional geometry columns.
* Backend frameworks such as Django or FastAPI access spatial data directly from PostGIS to build WebGIS applications.

---



## Importing Spatial Data into PostGIS

Today I imported a Shapefile into PostgreSQL using QGIS's Database Manager.

### Import Process

The import process converts each GIS feature into a row within a PostgreSQL table. During the import, QGIS automatically creates the database table, defines the geometry column, and inserts all spatial features.

A typical imported table contains:

- A primary key (`id`)
- Attribute columns (e.g., road name, district, category)
- A geometry column (`geom`)

### Spatial Metadata Verification

After importing the layer, I verified the data using SQL queries to inspect:

- Number of imported records (`COUNT(*)`)
- Geometry type (`GeometryType()`)
- Coordinate Reference System (`ST_SRID()`)
- Human-readable geometry (`ST_AsText()`)

### Key Learnings

- A GIS layer is stored as a standard PostgreSQL table with an additional geometry column.
- The geometry column stores spatial objects such as points, lines, or polygons.
- QGIS acts as a client for importing and managing spatial data, while PostGIS serves as the permanent storage layer for WebGIS applications.
- Backend frameworks like Django access these PostGIS tables directly to expose spatial data through REST APIs.

---



## Working with a Real Spatial Dataset

Today I imported the **NYC Subway Stations** dataset into PostGIS and explored its structure.

### Dataset Information

- Table Name: `nyc_subway_stations`
- Number of Features: **491**
- Geometry Type: **POINT**
- Coordinate Reference System (SRID): **26918 (NAD83 / UTM Zone 18N)**

### Dataset Structure

The imported layer contains both spatial and non-spatial attributes. Besides the geometry column (`geom`), the table includes descriptive fields such as station name, borough, subway routes, transfer information, and express service status.

### Key Learnings

- Each GIS feature is stored as a row in a PostgreSQL table.
- The geometry column stores the spatial location, while other columns store descriptive information.
- Projected coordinate systems such as SRID 26918 are commonly used because they provide more accurate distance and area calculations than geographic coordinate systems.
- Spatial data can be queried using standard SQL together with PostGIS spatial functions.
