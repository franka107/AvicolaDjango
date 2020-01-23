from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ShedSerializer, ShedProductionUpSerializer, ShedProductionDownSerializer, ShedRaisedUpSerializer, ShedRaisedDownSerializer
from .models import Shed, ShedRegister
from farms.models import Farm
from django.utils import timezone

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

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
     
class ShedListado(ListView): 
    model = Shed
 
class ShedDetalle(DetailView): 
    model = Shed
 
class ShedCrear(SuccessMessageMixin, CreateView): 
    model = Shed
    form = Shed
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer' 
 
class ShedActualizar(SuccessMessageMixin, UpdateView): 
    model = Shed
    form = Shed
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer' 
 
class ShedEliminar(SuccessMessageMixin, DeleteView): 
    model = Shed 
    form = Shed
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer'

class ShedProductionUpListado(ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="P").filter(shed__farm__name="Arriba")

class ShedProductionUpDetalle(DetailView): 
    model = ShedRegister
 
class ShedProductionUpCrear(SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedprodcutionup') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionUpActualizar(SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedprodcutionup') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionUpEliminar(SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedprodcutionup') # Redireccionamos a la vista principal 'leer'

class ShedProductionDownListado(ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="P").filter(shed__farm__name="Abajo")

class ShedProductionDownDetalle(DetailView): 
    model = ShedRegister
 
class ShedProductionDownCrear(SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedprodcutiondown') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionDownActualizar(SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedprodcutiondown') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionDownEliminar(SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedprodcutiondown') # Redireccionamos a la vista principal 'leer'


class ShedRaisedUpListado(ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(date = timezone.now()).filter(shed__type="L").filter(shed__farm__name="Arriba")

class ShedRaisedUpDetalle(DetailView): 
    model = ShedRegister
 
class ShedRaisedUpCrear(SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer' 
 
class ShedRaisedUpActualizar(SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer' 
 
class ShedRaisedUpEliminar(SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer'        