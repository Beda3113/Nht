from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensors-list-create'),
    path('sensors/<pk>/', SensorRetrieveUpdateView.as_view(), name='sensors-retrieve-update'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements-create'),
    path('sensors/<pk>/detail/', SensorDetailView.as_view(), name='sensors-detail'),
]
