from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from parts.models import RestorationPart


# Create your views here.
class PartListView(ListView):
    model = RestorationPart
    template_name = 'vehicles/part_list.html'
    context_object_name = 'restoration_part'

class PartDetailView(DetailView):
    model = RestorationPart
    template_name = 'parts/pppart_detail.html'

class PartCreateView(CreateView):
    model = RestorationPart
    template_name = 'parts/part_form.html'
    fields = ['name', 'part_number', 'price']
    success_url = reverse_lazy('parts-list')

class PartUpdateView(UpdateView):
    model = RestorationPart
    template_name = 'parts/part_form.html'
    fields = ['name', 'part_number', 'price']
    success_url = reverse_lazy('parts-list')

class PartDeleteView(DeleteView):
    model = RestorationPart
    template_name = 'parts/part_confirm_delete.html'
    success_url = reverse_lazy('parts-list')