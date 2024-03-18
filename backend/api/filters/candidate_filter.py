import django_filters as filters
from api.models import Candidate
from django.db.models import Q
import datetime

class DateOnlyFilter(filters.DateFilter):
    def filter(self, qs, value):
        if not value:
            return qs
        # Filter for the entire day (from 00:00:00 to 23:59:59)
        start_date = datetime.datetime.combine(value, datetime.time.min)
        end_date = datetime.datetime.combine(value, datetime.time.max)
        return qs.filter(**{f"{self.field_name}__range": (start_date, end_date)})
    
class StatusFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value == 'null':
            return qs.filter(**{f"{self.field_name}__isnull": True})
        elif value == 'true':
            return qs.filter(**{f"{self.field_name}__exact": True})
        elif value == 'false':
            return qs.filter(**{f"{self.field_name}__exact": False})
        else:
            return qs
        
class RepeatStatusFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value == 'repeater':
            return qs.filter(prev_candidature__isnull=False).distinct()
        elif value == 'fresh':
            return qs.filter(prev_candidature__isnull=True).distinct()
        else:
            return qs
    

class CandidateFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id')
    nic = filters.CharFilter(field_name='nic')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    roll_number = filters.CharFilter(field_name='roll_number')
    gender = filters.CharFilter(field_name='gender')
    status = StatusFilter(field_name='status')
    repeat_status = RepeatStatusFilter(field_name='candidate_id')


    created_at = DateOnlyFilter(field_name='created_at')

    center__id = filters.CharFilter(field_name='center__id')
    course__id = filters.CharFilter(field_name='course__id')

    def filter_repeat_status(self, queryset, name, value):
        # This method is defined separately to handle the repeat_status filter logic
        return queryset
    
    
    class Meta:
        model = Candidate
        fields = ['id', 'nic', 'name', 'center', 'course', 'roll_number', 'gender', 'status', 'created_at', 'repeat_status']



