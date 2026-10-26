from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from brands.models import Manufacturer
from parts.models import RestorationPart

class ClassicCar(models.Model):
    model_name = models.CharField(
        max_length=100,
    )
    manufacture_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1886, message='Manufacture year must be 1886 or later (invention of the automobile)'),
            MaxValueValidator(1990, message='A classic car must have been manufactured in 1990 or earlier.')
        ],
        help_text='Year must be between 1886 and 1990.'
    )
    vin = models.CharField(
        max_length=17,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-HJ-NPR-Z0-9]{17}$',
                message='VIN must be exactly 17 alphanumerical characters (standard VIN excludes letters I, O and Q).'
            )
        ],
        error_messages={
            'unique': 'A vehicle with that VIN already exists.'
        },
        help_text='17-character unique Vehicle Identification Number (VIN).'
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

    class Meta:
        ordering = ['-manufacture_year', 'model_name']
        verbose_name = 'Classic Car'
        verbose_name_plural = 'Classic Cars'

    @property
    def total_parts_cost(self):
        return sum(part.price for part in self.required_parts.all())

    @property
    def parts_count(self):
        return self.required_parts.count()

    def __str__(self):
        return f"{self.manufacture_year} {self.manufacturer.name} {self.model_name}"