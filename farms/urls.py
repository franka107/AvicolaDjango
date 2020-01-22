from django.urls import path
#from django.views.generic import TemplateView
from farms.views import FarmListado, FarmDetalle, FarmCrear, FarmActualizar, FarmEliminar
from . import views
 
#from postres.views import PostresList
 
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [

    path('',views.index, name='index'),
    
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('farm/', FarmListado.as_view(template_name = "farm/lista.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('farm/detalle/<int:pk>', FarmDetalle.as_view(template_name = "farm/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('farm/crear', FarmCrear.as_view(template_name = "farm/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('farm/editar/<int:pk>', FarmActualizar.as_view(template_name = "farm/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('farm/eliminar/<int:pk>', FarmEliminar.as_view(), name='eliminar'),    
]