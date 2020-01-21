from django.http import HttpResponse
from rest_framework import viewsets
from .models import Promotion
from django.utils import timezone

from django.urls import reverse
from django.views import generic

class ChickenView(generic.ListView):
    template_name = 'chicken/chicken.html'
    context_object_name = 'list_chicken'

    def get_queryset(self):
        return  Promotion.objects.order_by('id')[:5]   