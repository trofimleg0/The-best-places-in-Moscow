from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short description")
    long_description = models.TextField(verbose_name="Long description")
    lon = models.FloatField(verbose_name="Longitude")
    lat = models.FloatField(verbose_name="Latitude")

    def __str__(self):
        return self.title
