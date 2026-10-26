from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from parts.models import RestorationPart
from vehicles.forms import ClassicCarCreateForm, ClassicCarUpdateForm
from vehicles.models import ClassicCar
from brands.models import Manufacturer


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cars = ClassicCar.objects.select_related('manufacturer').prefetch_related('required_parts')

        context['total_cars'] = cars.count()
        context['total_parts'] = RestorationPart.objects.count()
        context['total_manufacturers'] = Manufacturer.objects.count()

        context['total_restoration_budget'] = sum(car.total_parts_cost for car in cars)

        context['recent_cars'] = cars.order_by('-id')[:3]
        return context

class ClassicCarListView(ListView):
    model = ClassicCar
    template_name = 'vehicles/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('manufacturer').prefetch_related('required_parts')

        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(model_name__icontains=query) | Q(vin__icontains=query)
            )

        manufacturer_id = self.request.GET.get('manufacturer', '').strip()
        if manufacturer_id:
            queryset = queryset.filter(manufacturer_id=manufacturer_id)

        sort = self.request.GET.get('sort', '').strip()
        if sort == 'oldest':
            queryset = queryset.order_by('manufacture_year', 'model_name')
        elif sort == 'newest':
            queryset = queryset.order_by('-manufacture_year', 'model_name')
        elif sort == 'model_asc':
            queryset = queryset.order_by('model_name')
        elif sort == 'model_desc':
            queryset = queryset.order_by('-model_name')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturers'] = Manufacturer.objects.all()
        context['selected_manufacturer'] = self.request.GET.get('manufacturer', '')
        context['selected_sort'] = self.request.GET.get('sort', '')
        context['search_query'] = self.request.GET.get('q', '')

        return context

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
    context_object_name = 'car'
    template_name = 'vehicles/car_confirm_delete.html'
    success_url = reverse_lazy('vehicles:car-list')