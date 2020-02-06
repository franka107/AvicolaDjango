from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from sheds.views import ShedListado, ShedDetalle, ShedCrear, ShedActualizar, ShedEliminar
from sheds.views import ShedProductionUpListado, ShedProductionUpDetalle, ShedProductionUpCrear, ShedProductionUpActualizar, ShedProductionUpEliminar
from sheds.views import ShedProductionDownListado,ShedProductionDownDetalle,ShedProductionDownCrear,ShedProductionDownActualizar,ShedProductionDownEliminar
from sheds.views import ShedRaisedUpListado,ShedRaisedUpDetalle,ShedRaisedUpCrear,ShedRaisedUpActualizar,ShedRaisedUpEliminar
from sheds.views import ShedRaisedDownListado,ShedRaisedDownDetalle,ShedRaisedDownCrear,ShedRaisedDownActualizar,ShedRaisedDownEliminar
router = routers.DefaultRouter()
router.register(r'sheds', views.ShedViewSet)
router.register(r'productionup', views.ShedProductionUpViewSet)
router.register(r'productiondown', views.ShedProductionDownViewSet)
router.register(r'raisedup', views.ShedRaisedUpViewSet)
router.register(r'raiseddown', views.ShedRaisedDownViewSet)



urlpatterns = [


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\

    
    path('', ShedListado.as_view(template_name = "shed/lista.html"), name='leer_shed'),
 
    path('detalle/<int:pk>', ShedDetalle.as_view(template_name = "shed/detalles.html"), name='detalles_shed'),
 
    path('crear', ShedCrear.as_view(template_name = "shed/crear.html"), name='crear_shed'),
 
    path('editar/<int:pk>', ShedActualizar.as_view(template_name = "shed/actualizar.html"), name='actualizar_shed'), 
 
    path('eliminar/<int:pk>', ShedEliminar.as_view(), name='eliminar_shed'),


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


    path('productionup/', ShedProductionUpListado.as_view(template_name = "shed/productionup/lista.html"), name='leer_shedproductionup'),
 
    path('productionup/detalle/<int:pk>', ShedProductionUpDetalle.as_view(template_name = "shed/productionup/detalles.html"), name='detalles_shedproductionup'),
 
    path('productionup/crear', ShedProductionUpCrear.as_view(template_name = "shed/productionup/crear.html"), name='crear_shedproductionup'),
 
    path('productionup/editar/<int:pk>', ShedProductionUpActualizar.as_view(template_name = "shed/productionup/actualizar.html"), name='actualizar_shedproductionup'), 
 
    path('productionup/eliminar/<int:pk>', ShedProductionUpEliminar.as_view(), name='eliminar_shedproductionup'), 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


    path('productiondown/', ShedProductionDownListado.as_view(template_name = "shed/productiondown/lista.html"), name='leer_shedproductiondown'),
 
    path('productiondown/detalle/<int:pk>', ShedProductionDownDetalle.as_view(template_name = "shed/productiondown/detalles.html"), name='detalles_shedproductiondown'),
 
    path('productiondown/crear', ShedProductionDownCrear.as_view(template_name = "shed/productiondown/crear.html"), name='crear_shedproductiondown'),
 
    path('productiondown/editar/<int:pk>', ShedProductionDownActualizar.as_view(template_name = "shed/productiondown/actualizar.html"), name='actualizar_shedproductiondown'), 
 
    path('productiondown/eliminar/<int:pk>', ShedProductionDownEliminar.as_view(), name='eliminar_shedproductiondown'), 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


    path('raisedup/', ShedRaisedUpListado.as_view(template_name = "shed/raisedup/lista.html"), name='leer_shedraisedup'),
 
    path('raisedup/detalle/<int:pk>', ShedRaisedUpDetalle.as_view(template_name = "shed/raisedup/detalles.html"), name='detalles_shedraisedup'),
 
    path('raisedup/crear', ShedRaisedUpCrear.as_view(template_name = "shed/raisedup/crear.html"), name='crear_shedraisedup'),
 
    path('raisedup/editar/<int:pk>', ShedRaisedUpActualizar.as_view(template_name = "shed/raisedup/actualizar.html"), name='actualizar_shedraisedup'), 
 
    path('raisedup/eliminar/<int:pk>', ShedRaisedUpEliminar.as_view(), name='eliminar_shedraisedup'), 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


    path('raiseddown/', ShedRaisedDownListado.as_view(template_name = "shed/raiseddown/lista.html"), name='leer_shedraiseddown'),
 
    path('raiseddown/detalle/<int:pk>', ShedRaisedDownDetalle.as_view(template_name = "shed/raiseddown/detalles.html"), name='detalles_shedraiseddown'),
 
    path('raiseddown/crear', ShedRaisedDownCrear.as_view(template_name = "shed/raiseddown/crear.html"), name='crear_shedraiseddown'),
 
    path('raiseddown/editar/<int:pk>', ShedRaisedDownActualizar.as_view(template_name = "shed/raiseddown/actualizar.html"), name='actualizar_shedraiseddown'), 
 
    path('raiseddown/eliminar/<int:pk>', ShedRaisedDownEliminar.as_view(), name='eliminar_shedraiseddown'), 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


    path('report/production/',views.ReportsProductions, name='production'),
    path('report/shedp/',views.ReportsShedProduction, name='shedP'),
    path('report/shedr/',views.ReportsShedRaised, name='shedR'),

]
