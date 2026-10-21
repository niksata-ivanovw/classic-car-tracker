from django.urls import path, include

from vehicles.views import ClassicCarListView, ClassicCarDetailView, ClassicCarCreateView, ClassicCarDeleteView, \
    ClassicCarUpdateView

app_name = 'vehicles'

urlpatterns = [
    path('', ClassicCarListView.as_view(), name='car-list'),
    path('create/', ClassicCarCreateView.as_view(), name='car-create'),
    path('<int:pk>/', include([
        path('', ClassicCarDetailView.as_view(), name='car-detail'),
        path('edit/', ClassicCarUpdateView.as_view(), name='car-update'),
        path('delete/', ClassicCarDeleteView.as_view(), name='car-delete'),
    ])),
]