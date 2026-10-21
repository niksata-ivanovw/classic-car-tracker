from django.shortcuts import render
from django.views.generic import CreateView, ListView

from brands.models import Manufacturer


# Create your views here.
class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'brands/manufacturer_list.html'
    context_object_name = 'manufacturers'

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    template_name = 'brands/manufacturer_form.html'
    fields = ['name', 'country', 'established_year']