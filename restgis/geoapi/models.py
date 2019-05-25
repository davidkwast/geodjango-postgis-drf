from django.contrib.gis.db import models

class Point(models.Model):
    name = models.CharField(max_length=100, unique=True)
    geometry = models.PointField()

class Polygon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    geometry = models.PolygonField()
