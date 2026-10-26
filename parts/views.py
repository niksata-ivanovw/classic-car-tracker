from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from parts.forms import PartForm
from parts.models import RestorationPart


# Create your views here.
class PartListView(ListView):
    model = RestorationPart
    template_name = 'parts/parts_list.html'
    context_object_name = 'parts'

class PartDetailView(DetailView):
    model = RestorationPart
    template_name = 'parts/part_detail.html'
    context_object_name = 'part'

class PartCreateView(CreateView):
    model = RestorationPart
    template_name = 'parts/part_form.html'
    form_class = PartForm
    success_url = reverse_lazy('parts:part-list')

class PartUpdateView(UpdateView):
    model = RestorationPart
    template_name = 'parts/part_form.html'
    form_class = PartForm
    success_url = reverse_lazy('parts:part-list')

class PartDeleteView(DeleteView):
    model = RestorationPart
    context_object_name = 'part'
    template_name = 'parts/part_confirm_delete.html'
    success_url = reverse_lazy('parts:part-list')