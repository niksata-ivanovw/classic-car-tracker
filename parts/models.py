from django.db import models

# Create your models here.
class RestorationPart(models.Model):
    name = models.CharField(
        max_length=100,
    )
    part_number = models.CharField(
        max_length=50,
        unique=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.name} ({self.part_number})"