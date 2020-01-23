from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Promotion
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

class PromotionListado(ListView): 
    model = Promotion
 
class PromotionDetalle(DetailView): 
    model = Promotion
 
class PromotionCrear(SuccessMessageMixin, CreateView): 
    model = Promotion
    form = Promotion
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_promotion') # Redireccionamos a la vista principal 'leer' 
 
class PromotionActualizar(SuccessMessageMixin, UpdateView): 
    model = Promotion
    form = Promotion
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_promotion') # Redireccionamos a la vista principal 'leer' 
 
class PromotionEliminar(SuccessMessageMixin, DeleteView): 
    model = Promotion 
    form = Promotion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_promotion') # Redireccionamos a la vista principal 'leer'