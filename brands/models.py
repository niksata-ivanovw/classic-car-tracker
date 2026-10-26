from datetime import date
from django.core.validators import MinValueValidator
from django.db import models

def current_year():
    return date.today().year

class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique': 'A manufacturer with this brand name already exists.'
        }
    )
    country = models.CharField(
        max_length=100,
    )
    established_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1700, message='Established year must be 1700 or later.')
        ],
        help_text='Year the brand was established'
    )

    class Meta:
        ordering = ['name',]
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    @property
    def cars_count(self):
        return self.cars.count()

    def __str__(self):
        return self.name