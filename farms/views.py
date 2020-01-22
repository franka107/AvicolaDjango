from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Farm
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

def index(request):
    context = {
    }
    return render(request, 'farm/index.html',context)

class FarmListado(ListView): 
    model = Farm
 
class FarmDetalle(DetailView): 
    model = Farm
 
class FarmCrear(SuccessMessageMixin, CreateView): 
    model = Farm
    form = Farm
    fields = "__all__" 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class FarmActualizar(SuccessMessageMixin, UpdateView): 
    model = Farm
    form = Farm
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class FarmEliminar(SuccessMessageMixin, DeleteView): 
    model = Farm 
    form = Farm
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'