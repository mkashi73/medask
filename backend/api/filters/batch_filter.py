import django_filters as filters
from api.models import Batches

class BatchFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id')
    course_id__id = filters.CharFilter(field_name='course_id__id')
    center_id__id = filters.CharFilter(field_name='center_id__id')
    
    class Meta:
        model = Batches
        fields = ['id', 'course_id', 'center_id']



