from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    country = models.CharField(
        max_length=100,
    )
    established_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name