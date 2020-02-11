from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from sheds.models import Shed, ShedRegister
from farms.models import Farm
from django.utils import timezone
from datetime import datetime, date, time, timedelta

#-----------------------------------------------------------------------------------------------------------------------#
# Datos API

class ShedViewSet(viewsets.ModelViewSet):
    queryset = Shed.objects.all().order_by('name')
    serializer_class = ShedSerializer
    http_method_names = ['get']

class ShedProductionUpViewSet(viewsets.ModelViewSet):
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="P").filter(shed__farm__name="Arriba")
    serializer_class = ShedProductionUpSerializer

class ShedProductionDownViewSet(viewsets.ModelViewSet):
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="P").filter(shed__farm__name="Abajo")
    serializer_class = ShedProductionDownSerializer

class ShedRaisedUpViewSet(viewsets.ModelViewSet):
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="L").filter(shed__farm__name="Arriba")
    serializer_class = ShedRaisedUpSerializer   

class ShedRaisedDownViewSet(viewsets.ModelViewSet):
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="L").filter(shed__farm__name="Abajo")
    serializer_class = ShedRaisedDownSerializer

class ProductionUpViewSet(viewsets.ModelViewSet):
    queryset = ShedRegister.objects.filter(date__gte = timezone.now()- timedelta(days=7) ).filter(date__lte = timezone.now()).filter(shed__type="P").filter(shed__farm__name="Arriba")
    serializer_class = ShedRaisedDownSerializer
    http_method_names = ['get']


class ProductionDownViewSet(viewsets.ModelViewSet):
    queryset = ShedRegister.objects.filter(date__gte = timezone.now()- timedelta(days=7) ).filter(date__lte = timezone.now()).filter(shed__type="P").filter(shed__farm__name="Abajo")
    serializer_class = ShedRaisedDownSerializer
    http_method_names = ['get']