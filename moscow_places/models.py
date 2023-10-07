from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short description")
    long_description = HTMLField(verbose_name="Long description")
    lon = models.FloatField(verbose_name="Longitude")
    lat = models.FloatField(verbose_name="Latitude")

    def __str__(self):
        return f"{self.pk}. {self.title}"

    class Meta:
        db_table = "Place"


class Photo(models.Model):
    image = models.ImageField(verbose_name="Image")
    place = models.ForeignKey(
        Place, related_name="photo", on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}. {self.place.title}"

    class Meta:
        db_table = "Photo"
        ordering = ["order"]
