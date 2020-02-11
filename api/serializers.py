from rest_framework import serializers
from sheds.models import Shed 
from sheds.models import ShedRegister 
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

    def update(self, instance, validated_data):
        instance.shed = validated_data.get(
            'shed',
            instance.shed
        )
        instance.date = validated_data.get(
            'date',
            instance.date
        )
        instance.food_income = validated_data.get(
            'food_income',
            instance.food_income
        )
        instance.food_deposit = validated_data.get(
            'food_deposit',
            instance.food_deposit
        )
        instance.food_consumption = validated_data.get(
            'food_consumption',
            instance.food_consumption
        )
        instance.final_deposit = validated_data.get(
            'final_deposit',
            instance.final_deposit
        )
        instance.chicken_death = validated_data.get(
            'chicken_death',
            instance.chicken_death
        )
        instance.observation = validated_data.get(
            'observation',
            instance.observation
        )
        instance.save()
        return instance

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



class ProductionShedSerializer(serializers.ModelSerializer):
    shed = ShedSerializer(many = False, read_only= True)
    class Meta:
        model = ShedRegister
        fields = ('id','shed','date','package_total','leftover_eggs')

