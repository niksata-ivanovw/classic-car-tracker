from django import forms
from django.core.exceptions import ValidationError

from vehicles.models import ClassicCar


class ClassicCarCreateForm(forms.ModelForm):
    class Meta:
        model = ClassicCar
        fields = ['model_name', 'manufacture_year', 'vin', 'manufacturer']
        labels = {
            'model_name': 'Car Model',
            'manufacture_year': 'Year of Manufacture',
            'vin': 'Vehicle Identification Number (VIN)',
            'manufacturer': 'Manufacturer',
        }

        widgets = {
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Ford Mustang'}),
            'vin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '17-character VIN'}),
            'manufacture_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(attrs={'class': 'form-select'}),
            'required_parts': forms.CheckboxSelectMultiple(),
        }

    def clean_manufacture_year(self):
        year = self.cleaned_data.get('manufacture_year')
        if year is not None and year > 1990:
            raise ValidationError('A classic car must have been manufactured in 1990 or earlier')
        return year

    def clean_vin(self):
        vin = self.cleaned_data.get('vin')
        if vin and len(vin) != 17:
            raise ValidationError('The VIN must be exactly 17 characters long')
        return vin

class ClassicCarUpdateForm(ClassicCarCreateForm):
    class Meta(ClassicCarCreateForm.Meta):
        fields = ['model_name', 'manufacture_year', 'vin', 'manufacturer', 'required_parts']
        widgets = {
            **ClassicCarCreateForm.Meta.widgets,
            'required_parts': forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vin'].disabled = True