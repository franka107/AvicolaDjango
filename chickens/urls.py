from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'chicken'

urlpatterns = [
    path('',views.ChickenView.as_view(), name='chicken'),
]