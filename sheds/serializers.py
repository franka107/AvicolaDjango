from rest_framework import serializers
from .models import Shed 
from .models import ShedRegister 
from farms.models import Farm

class ShedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shed
        fields = ('id','name','farm','created','updated','type')

class ShedProductionUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('id','shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','package_total','leftover_eggs','observation')

class ShedProductionDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('id','shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','package_total','leftover_eggs','observation')

class ShedRaisedUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('id','shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','observation')

class ShedRaisedDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('id','shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','observation')
