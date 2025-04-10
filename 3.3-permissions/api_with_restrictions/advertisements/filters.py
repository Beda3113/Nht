from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget
from django.contrib.auth.models import User

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    
    created_at = filters.DateFromToRangeFilter(
        field_name='created_at',
        label='Дата создания (диапазон)',
        widget=RangeWidget(attrs={'type': 'date'})
    )
    
    creator = filters.ModelChoiceFilter(
        field_name='creator',
        queryset=User.objects.all(),
        label='Создатель'
    )
    
    status = filters.ChoiceFilter(
        choices=Advertisement.STATUS_CHOICES,
        label='Статус'
    )

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
