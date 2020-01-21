from rest_framework import serializers
from .models import Shed 
from .models import ShedRegister 

class ShedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shed
        fields = ('name','created','updated','type')

class ShedProductionUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','package_total','leftover_eggs','observation')

class ShedProductionDownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','package_total','leftover_eggs','observation')

class ShedRaisedUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','observation')


class ShedRaisedDownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShedRegister
        fields = ('shed','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','observation')
