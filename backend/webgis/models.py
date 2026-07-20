from django.db import models

# Create your models here.
class SubwayStation(models.Model):
    name = models.CharField(max_length = 150)
    borough = models.CharField(max_length = 50)
    routes = models.CharField(max_length = 100)
    transfers = models.CharField(max_length = 100, blank = True)
    express = models.BooleanField(default = False)

    def __str__(self):
        return self.name