from django import forms
from django.core.exceptions import ValidationError

from vehicles.models import ClassicCar


class ClassicCarCreateForm(forms.ModelForm):
    class Meta:
        model = ClassicCar

        exclude = ['required_parts']

        labels = {
            'model_name': 'Car Model',
            'manufacture_year': 'Year of Manufacture',
            'vin': 'Vehicle Identification Number (VIN)',
        }

        widgets = {
            'model_name': forms.TextInput(attrs={'placeholder': 'e.g. Ford Mustang'}),
            'vin': forms.TextInput(attrs={'placeholder': '17-character VIN'}),
        }

    def clean_manufacture_year(self):
        year = self.cleaned_data.get('manufacture_year')
        if year > 1990:
            raise ValidationError('A classic car must have been manufactured in 1990 or earlier')
        return year

    def clean_vin(self):
        vin = self.cleaned_data.get('vin')
        if len(vin) != 17:
            raise ValidationError('The VIN must be exactly 17 characters long')
        return vin

class ClassicCarUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['vin'].disabled = True