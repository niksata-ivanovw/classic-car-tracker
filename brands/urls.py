from django.urls import path

from brands.views import ManufacturerListView, ManufacturerCreateView

urlpatterns = [
    path('', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('create/', ManufacturerCreateView.as_view(), name='manufacturer-create'),
]