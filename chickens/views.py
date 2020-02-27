from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Promotion
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class ShedForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = "__all__" 
    def __init__(self, *args, **kwargs):       
        super().__init__(*args, **kwargs)
        self.fields['shed'].queryset = self.fields['shed'].queryset.order_by('type','name')


class PromotionListado(LoginRequiredMixin,ListView): 
    model = Promotion
 
class PromotionDetalle(LoginRequiredMixin,DetailView): 
    model = Promotion
 
class PromotionCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Promotion
    form = Promotion
    form_class = ShedForm
    success_message = 'Promocion Creada Correctamente !' 
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_success_url(self):        
        return reverse('leer_promotion') 
 
class PromotionActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Promotion
    form = Promotion
    fields = "__all__" 
    success_message = 'Promocion Actualizada Correctamente !' 
 
    def get_success_url(self):               
        return reverse('leer_promotion') 
 
class PromotionEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Promotion 
    form = Promotion
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Promocion Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_promotion') 