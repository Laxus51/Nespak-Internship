from django.contrib.gis.db import models

class NycHomicide(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(srid=26918, blank=True, null=True)
    incident_d = models.DateField(blank=True, null=True)
    boroname = models.CharField(max_length=13, blank=True, null=True)
    num_victim = models.CharField(max_length=1, blank=True, null=True)
    primary_mo = models.CharField(max_length=20, blank=True, null=True)
    weapon = models.CharField(max_length=16, blank=True, null=True)
    light_dark = models.CharField(max_length=1, blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nyc_homicides'