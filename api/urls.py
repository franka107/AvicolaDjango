from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'sheds', views.ShedViewSet)
router.register(r'productionup', views.ShedProductionUpViewSet)
router.register(r'productiondown', views.ShedProductionDownViewSet)
router.register(r'raisedup', views.ShedRaisedUpViewSet)
router.register(r'raiseddown', views.ShedRaisedDownViewSet)
router.register(r'reportpu', views.ProductionUpViewSet)
router.register(r'reportpd', views.ProductionDownViewSet)


urlpatterns = [
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\

    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]