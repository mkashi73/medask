import django_filters as filters
from api.models import Discipline

class DisciplineFilter(filters.FilterSet):
    course__id = filters.CharFilter(field_name='course__id')
    
    class Meta:
        model = Discipline
        fields = ['course']



