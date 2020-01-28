import django_filters
from .models import ShedRegister

class ShedRegisterFilter(django_filters.FilterSet):

    class Meta:
        model = ShedRegister
        fields = ('date',) 
