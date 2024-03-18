import django_filters as filters
from api.models import Education
from django.db.models import Q
import datetime

    
class CandidateEducationFilter(filters.FilterSet):
    candidate_id__id = filters.CharFilter(field_name='candidate_id__id')
   
    class Meta:
        model = Education
        fields = ['candidate_id']



