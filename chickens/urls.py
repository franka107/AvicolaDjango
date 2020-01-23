from django.urls import path
from chickens.views import PromotionListado, PromotionDetalle, PromotionCrear, PromotionActualizar, PromotionEliminar
from . import views
 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('', PromotionListado.as_view(template_name = "chicken/lista.html"), name='leer_promotion'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('detalle/<int:pk>', PromotionDetalle.as_view(template_name = "chicken/detalles.html"), name='detalles_promotion'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('crear', PromotionCrear.as_view(template_name = "chicken/crear.html"), name='crear_promotion'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('editar/<int:pk>', PromotionActualizar.as_view(template_name = "chicken/actualizar.html"), name='actualizar_promotion'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('eliminar/<int:pk>', PromotionEliminar.as_view(), name='eliminar_promotion'),    
]