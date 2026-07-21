from django.contrib.gis.db import models

class NycCensusBlock(models.Model):
    geom = models.MultiPolygonField(srid=26918, blank=True, null=True)
    blkid = models.CharField(max_length=15, blank=True, null=True)
    popn_total = models.BigIntegerField(blank=True, null=True)
    popn_white = models.BigIntegerField(blank=True, null=True)
    popn_black = models.BigIntegerField(blank=True, null=True)
    popn_nativ = models.BigIntegerField(blank=True, null=True)
    popn_asian = models.BigIntegerField(blank=True, null=True)
    popn_other = models.BigIntegerField(blank=True, null=True)
    boroname = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nyc_census_blocks'