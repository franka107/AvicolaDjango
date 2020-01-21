from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from django.urls import reverse
from django.views import generic
from .models import Farm

def index(request):
    context = {
    }
    return render(request, 'farm/index.html',context)

class FarmView(generic.ListView):
    template_name = 'farm/farm.html'
    context_object_name = 'list_farms'

    def get_queryset(self):
        return  Farm.objects.order_by('id')[:5]

# Create your views here.
