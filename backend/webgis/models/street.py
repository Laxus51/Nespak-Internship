from django.contrib.gis.db import models

class NycStreet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiLineStringField(srid=26918, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    oneway = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nyc_streets'