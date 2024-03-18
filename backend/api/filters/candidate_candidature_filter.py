import django_filters as filters
from api.models import PreviousCandidature
from django.db.models import Q
import datetime

    
class CandidateCandidatureFilter(filters.FilterSet):
    candidate_id__id = filters.CharFilter(field_name='candidate_id__id')
   
    class Meta:
        model = PreviousCandidature
        fields = ['candidate_id']



