from decimal import Decimal

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

class RestorationPart(models.Model):
    name = models.CharField(
        max_length=100,
    )
    part_number = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            MinLengthValidator(3, message='Part number must be at least 3 characters long.')
        ],
        error_messages={
            'unique': 'A restoration part with that number already exists.'
        }
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.01'), message='Price must be at least $0.01/')
        ],
        help_text='Cost of the part in USD.'
    )

    class Meta:
        ordering = ['name', 'price']
        verbose_name = 'Restoration Part'
        verbose_name_plural = 'Restoration Parts'

    def __str__(self):
        return f"{self.name} ({self.part_number})"