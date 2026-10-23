from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from brands.forms import ManufacturerForm
from brands.models import Manufacturer


# Create your views here.
class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'brands/manufacturer_list.html'
    context_object_name = 'manufacturers'

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    template_name = 'brands/manufacturer_form.html'
    form_class = ManufacturerForm
    success_url = reverse_lazy('brands:manufacturer_list')