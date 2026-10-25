from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from vehicles.forms import ClassicCarCreateForm, ClassicCarUpdateForm
from vehicles.models import ClassicCar


# Create your views here.
class ClassicCarListView(ListView):
    model = ClassicCar
    template_name = 'vehicles/car_list.html'
    context_object_name = 'cars'

class ClassicCarDetailView(DetailView):
    model = ClassicCar
    template_name = 'vehicles/car_detail.html'
    context_object_name = 'car'

class ClassicCarCreateView(CreateView):
    model = ClassicCar
    template_name = 'vehicles/car_form.html'
    form_class = ClassicCarCreateForm
    success_url = reverse_lazy('vehicles:car-list')

class ClassicCarUpdateView(UpdateView):
    model = ClassicCar
    template_name = 'vehicles/car_form.html'
    form_class = ClassicCarUpdateForm
    success_url = reverse_lazy('vehicles:car-list')

class ClassicCarDeleteView(DeleteView):
    model = ClassicCar
    template_name = 'vehicles/car_confirm_delete.html'
    context_object_name = 'car'
    success_url = reverse_lazy('vehicles:car-list')