from django_filters import FilterSet, DateFilter, Filter
from store.models import Product


class ProductFilter(FilterSet):
    from_date = DateFilter(field_name='paid_at', lookup_expr='gte')
    to_date = DateFilter(field_name='paid_at', lookup_expr='lte')

    class Meta:
        model = Product
        fields = {
            'id': ['exact'],
            'collection': ['exact'],
            'title': ['exact'],
            'unit_price': ['exact']
        }
