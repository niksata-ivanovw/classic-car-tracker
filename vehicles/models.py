from django.db import models
from brands.models import Manufacturer
from parts.models import RestorationPart

# Create your models here.
class ClassicCar(models.Model):
    model_name = models.CharField(
        max_length=100,
    )
    manufacture_year = models.PositiveIntegerField()
    vin = models.CharField(
        max_length=17,
        unique=True,
    )

    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars',
    )

    required_parts = models.ManyToManyField(
        to=RestorationPart,
        related_name='cars',
        blank=True,
    )

    def __str__(self):
        return f"{self.manufacture_year} {self.manufacturer.name} {self.model_name}"