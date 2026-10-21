from django.urls import path, include

from parts.views import PartListView, PartCreateView, PartDetailView, PartUpdateView, PartDeleteView

app_name = 'parts'

urlpatterns = [
    path('', PartListView.as_view(), name='part-list'),
    path('create/', PartCreateView.as_view(), name='part-create'),
    path('<int:pk>/', include([
        path('', PartDetailView.as_view(), name='part-detail'),
        path('edit/', PartUpdateView.as_view(), name='part-edit'),
        path('delete/', PartDeleteView.as_view(), name='part-delete'),
    ])),
]