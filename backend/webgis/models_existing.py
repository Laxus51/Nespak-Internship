from django.contrib.gis.db import models


class NycSubwayStation(models.Model):
    id = models.IntegerField(primary_key=True)

    geom = models.PointField(
    srid=26918,
    blank=True,
    null=True
)

    objectid = models.IntegerField(
        db_column="OBJECTID",
        blank=True,
        null=True,
    )

    station_id = models.IntegerField(
        db_column="ID",
        blank=True,
        null=True,
    )

    name = models.CharField(max_length=31, blank=True, null=True)
    alt_name = models.CharField(db_column="ALT_NAME", max_length=38, blank=True, null=True)
    cross_st = models.CharField(db_column="CROSS_ST", max_length=27, blank=True, null=True)
    long_name = models.CharField(db_column="LONG_NAME", max_length=60, blank=True, null=True)
    label = models.CharField(db_column="LABEL", max_length=50, blank=True, null=True)
    borough = models.CharField(max_length=15, blank=True, null=True)
    nghbhd = models.CharField(db_column="NGHBHD", max_length=30, blank=True, null=True)
    routes = models.CharField(max_length=20, blank=True, null=True)
    transfers = models.CharField(db_column="TRANSFERS", max_length=25, blank=True, null=True)
    color = models.CharField(db_column="COLOR", max_length=30, blank=True, null=True)
    express = models.CharField(max_length=10, blank=True, null=True)
    closed = models.CharField(db_column="CLOSED", max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "nyc_subway_stations"