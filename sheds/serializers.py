from rest_framework import serializers
from .models import Shed 
from .models import ShedRegister 
from farms.models import Farm

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ('id','name')

class ShedSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(read_only=True)
    class Meta:
        model = Shed
        fields = ('id','farm','name')

class ShedProductionUpSerializer(serializers.ModelSerializer):
    shed = ShedSerializer(many = False, read_only= True)
    
    shed_id = serializers.PrimaryKeyRelatedField(
        write_only = True,
        queryset =  Shed.objects.all(),
        source= 'shed'
    )

    class Meta:
        model = ShedRegister
        fields = ('id','shed','shed_id','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','package_total','leftover_eggs','observation')

    def create(self, validated_data):
        shed_register = ShedRegister.objects.create(**validated_data)
        return shed_register       

class ShedProductionDownSerializer(serializers.ModelSerializer):
    shed = ShedSerializer(many = False, read_only= True)
    
    shed_id = serializers.PrimaryKeyRelatedField(
        write_only = True,
        queryset =  Shed.objects.all(),
        source= 'shed'
    )

    class Meta:
        model = ShedRegister
        fields = ('id','shed','shed_id','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','package_total','leftover_eggs','observation')

    def create(self, validated_data):
        shed_register = ShedRegister.objects.create(**validated_data)
        return shed_register

class ShedRaisedUpSerializer(serializers.ModelSerializer):
    shed = ShedSerializer(many = False, read_only= True)
    
    shed_id = serializers.PrimaryKeyRelatedField(
        write_only = True,
        queryset =  Shed.objects.all(),
        source= 'shed'
    )

    class Meta:
        model = ShedRegister
        fields = ('id','shed','shed_id','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','observation')

    def create(self, validated_data):
        shed_register = ShedRegister.objects.create(**validated_data)
        return shed_register


class ShedRaisedDownSerializer(serializers.ModelSerializer):
    shed = ShedSerializer(many = False, read_only= True)
    
    shed_id = serializers.PrimaryKeyRelatedField(
        write_only = True,
        queryset =  Shed.objects.all(),
        source= 'shed'
    )

    class Meta:
        model = ShedRegister
        fields = ('id','shed','shed_id','date','food_income','food_deposit','food_consumption','final_deposit','chicken_death','observation')

    def create(self, validated_data):
        shed_register = ShedRegister.objects.create(**validated_data)
        return shed_register