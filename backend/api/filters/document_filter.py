import django_filters as filters
from api.models import Document


class DocumentFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    created_by = filters.NumberFilter(field_name='created_by__id')

    class Meta:
        model = Document
        fields = ['name', 'created_by']