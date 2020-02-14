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
from django.db.models import Avg, Max, Min, Sum
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
    success_message = 'Galpon Creado Correctamente !' 
 
    def get_success_url(self):        
        return reverse('leer_shed')
class ShedActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Shed
    form = Shed
    fields = "__all__"  
    success_message = 'Galpon Actualizado Correctamente !' 
 
    def get_success_url(self):               
        return reverse('leer_shed') 
 
class ShedEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Shed 
    form = Shed
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_shed') 

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
    success_message = 'Registro Creado Correctamente !'  

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['farm'] = "Arriba"
        kwargs['type'] = "P"
        return kwargs
    def get_success_url(self):        
        return reverse('leer_shedproductionup')  
 
class ShedProductionUpActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = ProductionForm
    success_message = 'Registro Actualizado Correctamente !' 
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['farm'] = "Arriba"
        kwargs['type'] = "P"
        return kwargs
    def get_success_url(self):               
        return reverse('leer_shedproductionup') 
 
class ShedProductionUpEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedproductionup')
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
    def get_success_url(self):        
        return reverse('leer_shedproductiondown') 
 
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
 
    def get_success_url(self): 
        success_message = 'Registro Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedproductiondown')

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
    success_message = 'Registro Creado Correctamente !'
   
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Arriba"            
                return kwargs
    def get_success_url(self):        
        return reverse('leer_shedraisedup') 
class ShedRaisedUpActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Registro Actualizado Correctamente !' 
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Arriba"            
                return kwargs
    def get_success_url(self):               
        return reverse('leer_shedraisedup') 
 
class ShedRaisedUpEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = ShedRegister 
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
 
    def get_success_url(self): 
        success_message = 'Registro Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraisedup')         

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
    success_message = 'Registro Creado Correctamente !'      
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Abajo"            
                return kwargs
    def get_success_url(self):        
        return reverse('leer_shedraiseddown') 
 
class ShedRaisedDownActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = ShedRegister
    form = ShedRegister
    form_class = RaisedForm
    success_message = 'Registro Actualizado Correctamente !'  
    def get_form_kwargs(self):
                kwargs = super().get_form_kwargs()
                kwargs['type'] = "L"
                kwargs['farm'] = "Abajo"            
                return kwargs
    def get_success_url(self):               
        return reverse('leer_shedraiseddown') 
 
class ShedRaisedDownEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 

    model = ShedRegister 
    form = ShedRegister
    fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','food_type','food_price','chicken_weight')
 
    def get_success_url(self): 
        success_message = 'Registro Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_shedraiseddown')  

#-----------------------------------------------------------------------------------------------------------------------#
# Funciones

def is_valid_queryparam(param):
    return param != '' and param is not None

# Reportes

def ReportsProductions(request):
    min_date = request.GET.get('min_date')
    semana = timezone.now() - timedelta(days=6)
    qs = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").filter(date__gte=semana).filter(date__lte=timezone.now()).order_by('shed')
    data_date = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").filter(date__gte=semana).filter(date__lte=timezone.now()).order_by('date')

    if min_date == "":
        qs = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").filter(date__gte=semana).filter(date__lte=timezone.now()).order_by('shed')
        data_date = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").filter(date__gte=semana).filter(date__lte=timezone.now()).order_by('date')


    if is_valid_queryparam(min_date):
        dia1 = parse_date(min_date) 
        dia7 = dia1 - timedelta(days=6)
        qs = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").filter(date__gte=dia7).filter(date__lte=min_date).order_by('shed')
        data_date = ShedRegister.objects.filter(shed__type="P").filter(shed__farm__name="Abajo").filter(date__gte=dia7).filter(date__lte=min_date).order_by('date')


    context = {
        'queryset' : qs,
        'data_date' : data_date,
        'min_date' : min_date, 
    }    
    return render(request,"shed/reports/productions.html",context)

def ReportsShedProduction(request):
    shed = request.GET.get('shed')
    month = request.GET.get('date')
    mes = timezone.now() - timedelta(days=27)
    qs = ShedRegister.objects.filter(shed__type="P").order_by('name')
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