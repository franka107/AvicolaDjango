from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
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
from datetime import datetime, date, time, timedelta
from django.utils.dateparse import parse_date

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
        self.fields['shed'].queryset = self.fields['shed'].queryset.filter(type=type).filter(farm__name=farm)
        #self.fields['age_chicken'].disabled = True


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
# CRUD Galpones

class ShedListado(LoginRequiredMixin,ListView): 
    model = Shed
 
class ShedDetalle(LoginRequiredMixin,DetailView): 
    model = Shed
 
class ShedCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Shed
    form = Shed
    fields = "__all__" 
    success_message = 'Galpon Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_shed') # Redireccionamos a la vista principal 'leer' 
 
class ShedActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Shed
    form = Shed
    fields = "__all__"  
    success_message = 'Galpon Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
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
    def get_queryset(self):
        if self.request.GET.get('date') == None:
            return ShedRegister.objects.filter(date=date.today()).filter(shed__type="P").filter(shed__farm__name="Arriba").order_by('date','shed')
        else:
            return ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Arriba").order_by('date','shed')

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filter'] = ShedRegisterFilter(self.request.GET, queryset = self.get_queryset())
            context['hoy'] = date.today() 
            return context 

class ShedProductionUpDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedProductionUpCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Arriba")
    form_class = ProductionForm
    success_message = 'Registro Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     

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
    success_message = 'Registro Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
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
    def get_queryset(self):
        if self.request.GET.get('date') == None:
            return ShedRegister.objects.filter(date=date.today()).filter(shed__type="P").filter(shed__farm__name="Abajo").order_by('date','shed')
        else:
            return  ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").order_by('date','shed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
        context['hoy'] = date.today() 
        return context 

class ShedProductionDownDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedProductionDownCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = ProductionForm
    success_message = 'Registro Creado Correctamente !'
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
    success_message = 'Registro Actualizado Correctamente !' 
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "P"
                kwargs['farm'] = "Abajo"            
                return kwargs
    def get_success_url(self):               
        return reverse('leer_shedproductiondown') 
     
 
class ShedProductionDownEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Registro Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedproductiondown') # Redireccionamos a la vista principal 'leer'

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Levante Granja Arriba

class ShedRaisedUpListado(LoginRequiredMixin,ListView): 
    model = ShedRegister
    def get_queryset(self):
        if self.request.GET.get('date') == None:
            return ShedRegister.objects.filter(date=date.today()).filter(shed__type="L").filter(shed__farm__name="Arriba").order_by('date','shed')
        else:
            return  ShedRegister.objects.filter(shed__type="L").filter(shed__farm__name="Arriba").order_by('date','shed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
        context['hoy'] = date.today() 
        return context 

class ShedRaisedUpDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedRaisedUpCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Registro Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
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
    success_message = 'Registro Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
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
        success_message = 'Registro Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraisedup') # Redireccionamos a la vista principal 'leer'        

#-----------------------------------------------------------------------------------------------------------------------#
# CRUD Levante Granja Abajo

class ShedRaisedDownListado(LoginRequiredMixin,ListView): 
    model = ShedRegister
    def get_queryset(self):
        if self.request.GET.get('date') == None:
            return ShedRegister.objects.filter(date=date.today()).filter(shed__type="L").filter(shed__farm__name="Abajo").order_by('date','shed')
        else:
            return  ShedRegister.objects.filter(shed__type="L").filter(shed__farm__name="Abajo").order_by('date','shed')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ShedRegisterFilter(self.request.GET, queryset=self.get_queryset())
        context['hoy'] = date.today() 
        return context 

class ShedRaisedDownDetalle(LoginRequiredMixin,DetailView): 
    model = ShedRegister
 
class ShedRaisedDownCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Registro Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
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
    success_message = 'Registro Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
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
        success_message = 'Registro Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraiseddown') # Redireccionamos a la vista principal 'leer' 

#-----------------------------------------------------------------------------------------------------------------------#
# Funciones

def is_valid_queryparam(param):
    return param != '' and param is not None

# Reportes

def ReportsProductions(request):
    min_date = request.GET.get('min_date')
    max_date = request.GET.get('max_date')
    hoy = date.today()  # Asigna fecha actual
    qs = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").order_by('shed')
    dia1 = None  
    dia2 = None
    dia3 = None
    dia4 = None
    dia5 = None
    dia6 = None
    dia7 = None
    
    if min_date == None:
        qs = None
    elif min_date == "":
        qs = None

    if is_valid_queryparam(min_date):
        dia1 = parse_date(min_date) 
        dia2 = dia1 + timedelta(days=1)
        dia3 = dia2 + timedelta(days=1)
        dia4 = dia3 + timedelta(days=1)
        dia5 = dia4 + timedelta(days=1)
        dia6 = dia5 + timedelta(days=1)
        dia7 = dia6 + timedelta(days=1)
        qs = qs.filter(date__gte=min_date).filter(date__lte=dia7)

    context = {
        'queryset' : qs,
        'd1' : dia1,
        'd2' : dia2,
        'd3' : dia3,
        'd4' : dia4,
        'd5' : dia5,
        'd6' : dia6,
        'd7' : dia7,
        'min_date' : min_date, 
    }    
    return render(request,"shed/reports/productions.html",context)

def ReportsShedProduction(request):
    shed = request.GET.get('shed')
    month = request.GET.get('date')
    mes = timezone.now() - timedelta(days=27)
    qs = ShedRegister.objects.filter(shed__type="P").order_by('date')
    qss = Shed.objects.filter(type="P").order_by('name')
    #if date == None:
    #    qs = ShedRegister.objects.filter(shed__type="P").filter(date__gte=mes).order_by('date')
    #elif date == "":
    #    qs = ShedRegister.objects.filter(shed__type="P").filter(date__gte=mes).order_by('date')
    if shed == None:
        qs = None
    elif shed == "":
        qs = None    
    if is_valid_queryparam(shed):
        qs = qs.filter(shed=shed).order_by('date')

    if is_valid_queryparam(month):
        if qs != None:
            mes = parse_date(month) - timedelta(days=27)
            qs = qs.filter(date__gte=mes).filter(date__lte=month)
    else:
        if qs != None:
            qs = qs.filter(date__gte=mes)

    context = {
        'queryset' : qs,
        'querysets' : qss,
    }    
    return render(request,"shed/reports/shed_production.html",context)

def ReportsShedRaised(request):
    shed = request.GET.get('shed')
    month = request.GET.get('date')
    mes = timezone.now() - timedelta(days=27)
    qs = ShedRegister.objects.filter(shed__type="L").order_by('date')
    qss = Shed.objects.filter(type="L").order_by('name')
    #if date == None:
    #    qs = ShedRegister.objects.filter(shed__type="P").filter(date__gte=mes).order_by('date')
    #elif date == "":
    #    qs = ShedRegister.objects.filter(shed__type="P").filter(date__gte=mes).order_by('date')
    if shed == None:
        qs = None
    elif shed == "":
        qs = None    
    if is_valid_queryparam(shed):
        qs = qs.filter(shed=shed).order_by('date')

    if is_valid_queryparam(month):
        if qs != None:
            mes = parse_date(month) - timedelta(days=27)
            qs = qs.filter(date__gte=mes).filter(date__lte=month)
    else:
        if qs != None:
            qs = qs.filter(date__gte=mes)

    context = {
        'queryset' : qs,
        'querysets' : qss,
    }    
    return render(request,"shed/reports/shed_raised.html",context)