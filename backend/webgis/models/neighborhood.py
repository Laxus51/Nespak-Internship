from django.contrib.gis.db import models

class NycNeighborhood(models.Model):
    geom = models.MultiPolygonField(srid=26918, blank=True, null=True)
    boroname = models.CharField(max_length=43, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nyc_neighborhoods'