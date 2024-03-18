from datetime import timedelta
import django_filters as filters
from api.models import QuestionOption


class QuestionOptionFilter(filters.FilterSet):

    question_id = filters.CharFilter(field_name='question_id')
  
    class Meta:
        model = QuestionOption
        fields = [
            'question_id',
        ]
