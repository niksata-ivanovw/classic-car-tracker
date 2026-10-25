from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from brands.models import Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country', 'established_year']
        labels = {
            'name': 'Brand Name',
            'established_year': 'Year Established',
        }

    def clean_established_year(self):
        year = self.cleaned_data.get('established_year')
        current_year = date.today().year

        if year is not None and year > current_year:
            raise ValidationError(f"The established year cannot be in the future (greater than {current_year})")
        return year