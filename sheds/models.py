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
    shed = models.ForeignKey(
        Shed,
        on_delete=models.CASCADE
    )
    #Fecha del registro
    date = models.DateField()
    #Ingreso de comida
    food_income = models.IntegerField()
    #Saldo de comida
    food_deposit = models.IntegerField()
    #Consumo de comida
    food_consumption = models.IntegerField()
    #Saldo final
    final_deposit = models.IntegerField()
    #ingreso de pollos
    chicken_income = models.IntegerField()
    #cantidad de pollo
    chicken_quantity = models.IntegerField()
    #muerte de pollos
    chicken_death = models.IntegerField()
    #total de pollos
    chicken_total = models.IntegerField()
    #Observacion(opcional)
    observation =  models.TextField(null=True)


    #total de paquetes
    package_total = models.IntegerField(null= True)
    #huevos sobrantes
    leftover_eggs = models.IntegerField(null= True)



    
    