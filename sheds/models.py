from django.db import models
from farms.models import Farm 
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
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
        ordering = ('-type','farm')

    def __str__(self):
        return str(self.name)

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
    #Edad de Aves
    age_chicken = models.IntegerField(default=0)

    #Fecha del registro
    date = models.DateField()

    #Ingreso de comida
    food_income = models.IntegerField(default=0)

    #Saldo de comida
    food_deposit = models.IntegerField(default=0)

    #Consumo de comida
    food_consumption = models.IntegerField(default=0)
    
    #Saldo final
    final_deposit = models.IntegerField(default=0)

    #muerte de pollos
    chicken_death = models.IntegerField(default=0)

    #total de pollos
    #chicken_income =  models.IntegerField(default=0,null=True)
    
    #Observacion(opcional)
    observation =  models.TextField(blank=True)
    
    #total de paquetes ( solo en produccion )
    package_total = models.IntegerField(default=0)

    #huevos sobrantes (solo produccion)
    leftover_eggs = models.IntegerField(default=0)

    #tipo de comida
    food_type = models.CharField(max_length=1, choices=FOOD_CHOICES, blank=True)

    #precio del alimento
    food_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    #porcentaje de postura
    posture_percentaje =  models.DecimalField(max_digits=5, decimal_places=2,default=0)

    #conversion
    convertion = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    #peso de gallina
    chicken_weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    #peso huevos
    egg_weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)

#@receiver(post_save, sender=ShedRegister, dispatch_uid="update")
#def update(sender, instance, raw, created,**kwargs):
#    if created:
#       instance.shed.promotion.quantity -= instance.chicken_death
#       instance.shed.promotion.save()

@receiver(post_save, sender=ShedRegister, dispatch_uid="update")
def update(sender, instance, created,**kwargs):
    if created:
       instance.age_chicken = instance.shed.promotion.week_age
       instance.save()



    
  

    
    