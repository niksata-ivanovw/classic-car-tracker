from django import forms
from django.core.exceptions import ValidationError

from parts.models import RestorationPart


class PartForm(forms.ModelForm):
    class Meta:
        model = RestorationPart
        fields = ['name', 'part_number', 'price']
        labels = {
            'name': 'Part Description',
            'part_number': 'Official Part Number',
            'price': 'Price ($)',
        }
        widgets = {
            'part_number': forms.TextInput(attrs={'placeholder': 'e.g. ALT-9921'})
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('The price of a restoration part cannot be negative.')
        return price