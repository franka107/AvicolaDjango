from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from sheds.views import ShedListado, ShedDetalle, ShedCrear, ShedActualizar, ShedEliminar

router = routers.DefaultRouter()
router.register(r'sheds', views.ShedViewSet)
router.register(r'productionup', views.ShedProductionUpViewSet)
router.register(r'productiondown', views.ShedProductionDownViewSet)
router.register(r'raisedup', views.ShedRaisedUpViewSet)
router.register(r'raiseddown', views.ShedRaisedDownViewSet)



urlpatterns = [

    #Esta seccion se pone las rutas de la API
    path('api/', include(router.urls)),

    #Las rutas de la API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('', ShedListado.as_view(template_name = "shed/lista.html"), name='leer_shed'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('detalle/<int:pk>', ShedDetalle.as_view(template_name = "shed/detalles.html"), name='detalles_shed'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('crear', ShedCrear.as_view(template_name = "shed/crear.html"), name='crear_shed'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('editar/<int:pk>', ShedActualizar.as_view(template_name = "shed/actualizar.html"), name='actualizar_shed'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('eliminar/<int:pk>', ShedEliminar.as_view(), name='eliminar_shed'), 
]
