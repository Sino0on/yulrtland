import django_filters
from .models import Destination

class DestinationFilter(django_filters.FilterSet):
    class Meta:
        model = Destination
        fields = {
            'oblasti': ['exact'],
            'level': ['exact'],
            'days': ['exact'],
            'nights': ['exact'],
            'price': ['gte', 'lte'],
        }
