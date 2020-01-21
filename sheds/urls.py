from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sheds', views.ShedViewSet)
router.register(r'productionup', views.ShedProductionUpViewSet)
router.register(r'productiondown', views.ShedProductionDownViewSet)
router.register(r'raisedup', views.ShedRaisedUpViewSet)
router.register(r'raiseddown', views.ShedRaisedDownViewSet)
app_name = 'shed'

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.ShedView.as_view(), name='shed'),

]
