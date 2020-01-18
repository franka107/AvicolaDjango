from django.db import models
from farms.models import Farm 
# Create your models here.

class Shed(models.Model):
    TYPE_CHOICES =[
        ('P', 'Produccion'),
        ('L', 'Levante')
    ]

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=2,
        choices= TYPE_CHOICES
    )
    name = models.CharField(
        max_length=50,
        unique=True)
    is_active = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    

    class Meta:
        verbose_name = "Shed"
        verbose_name_plural = "Sheds"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Shed_detail", kwargs={"pk": self.pk})

class ShedRegister(models.Model):
    FOOD_CHOICES = [
        ('G', 'Granos'),
        ('M', 'Maiz')
    ]
    shed = models.ForeignKey(
        Shed,
        on_delete=models.CASCADE
    )

    #Fecha del registro
    date = models.DateField()
    #Ingreso de comida
    food_income = models.IntegerField(default=0)
    #Saldo de comida
    food_deposit = models.IntegerField()
    #Consumo de comida
    food_consumption = models.IntegerField()
    #Saldo final
    final_deposit = models.IntegerField()
    #ingreso de pollos
    #chicken_income = models.IntegerField(default=0)
    #cantidad de pollo
    chicken_quantity = models.IntegerField()
    #muerte de pollos
    chicken_death = models.IntegerField(default=0)
    #total de pollos
    chicken_total = models.IntegerField()
    #Observacion(opcional)
    observation =  models.TextField(blank=True)


    #total de paquetes ( solo en produccion )
    package_total = models.IntegerField(blank= True)
    #huevos sobrantes (solo produccion)
    leftover_eggs = models.IntegerField(blank= True)
    #tipo de comida
    food_type = models.CharField(max_length=1, choices=FOOD_CHOICES)
    #precio del alimento
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    #porcentaje de postura
    posture_percentaje =  models.DecimalField(max_digits=5, decimal_places=2)
    #conversion
    convertion = models.DecimalField(max_digits=5, decimal_places=2)
    #peso de gallina
    chicken_weight = models.DecimalField(max_digits=5, decimal_places=2)


    

    
    