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
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ShedRegisterFilter

#-----------------------------------------------------------------------------------------------------------------------#
# Filtro de Opciones Views

class ProductionForm(forms.ModelForm):
    class Meta:
        model = ShedRegister
        fields = "__all__" 
    def __init__(self, *args, **kwargs):
        farm = kwargs.pop('farm', None)
        type = kwargs.pop('type', None)        
        super().__init__(*args, **kwargs)
        self.fields['shed'].queryset = self.fields['shed'].queryset.filter(
            type=type).filter(farm__name=farm)

class RaisedForm(forms.ModelForm):
    class Meta:
        model = ShedRegister
        fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
    def __init__(self, *args, **kwargs):
        farm = kwargs.pop('farm', None)
        type = kwargs.pop('type', None)        
        super().__init__(*args, **kwargs)
        self.fields['shed'].queryset = self.fields['shed'].queryset.filter(
            type=type).filter(farm__name=farm)

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

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Galpones

class ShedListado(LoginRequiredMixin,ListView): 
    model = Shed
 
class ShedDetalle(LoginRequiredMixin,DetailView): 
    model = Shed
 
class ShedCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Shed
    form = Shed
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer' 
 
class ShedActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Shed
    form = Shed
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer' 
 
class ShedEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Shed 
    form = Shed
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer'

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Produccion Granja Arriba

class ShedProductionUpListado(LoginRequiredMixin,ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Arriba")

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
            return context 

class ShedProductionUpDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedProductionUpCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Arriba")
    form_class = ProductionForm
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['farm'] = "Arriba"
        kwargs['type'] = "P"
        return kwargs
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedproductionup') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionUpActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = ProductionForm
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['farm'] = "Arriba"
        kwargs['type'] = "P"
        return kwargs
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedproductionup') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionUpEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedproductionup') # Redireccionamos a la vista principal 'leer'

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Produccion Granja Abajo

class ShedProductionDownListado(LoginRequiredMixin,ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
        return context 

class ShedProductionDownDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedProductionDownCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = ProductionForm
    success_message = 'Creado Correctamente !'
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['type'] = "P"
            kwargs['farm'] = "Abajo"            
            return kwargs
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedproductiondown') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionDownActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = ProductionForm
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "P"
                kwargs['farm'] = "Abajo"            
                return kwargs
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedproductiondown') # Redireccionamos a la vista principal 'leer' 
 
class ShedProductionDownEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedproductiondown') # Redireccionamos a la vista principal 'leer'

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Levante Granja Arriba

class ShedRaisedUpListado(LoginRequiredMixin,ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(shed__type="L").filter(shed__farm__name="Arriba")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
        return context 

class ShedRaisedUpDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedRaisedUpCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Arriba"            
                return kwargs
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer' 
 
class ShedRaisedUpActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Arriba"            
                return kwargs
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer' 
 
class ShedRaisedUpEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer'        

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Levante Granja Abajo

class ShedRaisedDownListado(LoginRequiredMixin,ListView): 
    model = ShedRegister
    queryset = ShedRegister.objects.filter(shed__type="L").filter(shed__farm__name="Abajo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
        return context 

class ShedRaisedDownDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedRaisedDownCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Abajo"            
                return kwargs
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shedraiseddown') # Redireccionamos a la vista principal 'leer' 
 
class ShedRaisedDownActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Abajo"            
                return kwargs
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_shedraiseddown') # Redireccionamos a la vista principal 'leer' 
 
class ShedRaisedDownEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraiseddown') # Redireccionamos a la vista principal 'leer' 