from django.db import models
from farms.models import Farm 
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

class Shed(models.Model):
    TYPE_CHOICES =[
        ('P', 'Produccion'),
        ('L', 'Levante')
    ]

    # granja a al que pertence
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE
    ) 

    # tipo de galpon
    type = models.CharField(
        max_length=2,
        choices= TYPE_CHOICES
    )

    # nombre de galpon
    name = models.CharField(
        max_length=50,
        unique=True)
    
    # estado de galpon
    is_active = models.BooleanField(
        default=True,
    )

    # datos adicionales(se autogeneran)
    created = models.DateTimeField(
        auto_now_add=True,
    )

    # datos adicionales(se autogeneran)
    updated = models.DateTimeField(
        auto_now=True,
    )
    
    # clase meta
    class Meta:
        verbose_name = "Shed"
        verbose_name_plural = "Sheds"
        ordering = ('-type','farm')

    # funcion str
    def __str__(self):
        return str(self.name)

    # funcion get absolute url
    def get_absolute_url(self):
        return reverse("Shed_detail", kwargs={"pk": self.pk})

class ShedRegister(models.Model):
    FOOD_CHOICES = [
        ('G', 'Granos'),
        ('M', 'Maiz')
    ]

    # galpon al que pertenece
    shed = models.ForeignKey(
        Shed,
        related_name='shedregister',
        on_delete=models.CASCADE
    )
    # edad de Aves
    age_chicken = models.IntegerField(default=0)

    # fecha del registro
    date = models.DateField()

    # ingreso de comida
    food_income = models.IntegerField(default=0)

    # saldo de comida(Dia Anterior)
    food_deposit = models.IntegerField(default=0)

    # consumo de comida
    food_consumption = models.IntegerField(default=0)
    
    # saldo final(Final Dia)
    final_deposit = models.IntegerField(default=0)
    
    # total de pollos(final del dia)
    chicken_initial =  models.IntegerField(default=0)

    # muerte de pollos
    chicken_death = models.IntegerField(default=0)

    # total de pollos(final del dia)
    chicken_income =  models.IntegerField(default=0,null=True)
    
    # observacion(opcional)
    observation =  models.TextField(blank=True)
    
    # total de paquetes ( solo en produccion )
    package_total = models.IntegerField(default=0)

    # huevos sobrantes (solo produccion)
    leftover_eggs = models.IntegerField(default=0)

    # huevos blancos (x unidades solo produccion)
    egg_white = models.IntegerField(default=0)
    
    # --porcentaje de muertes 
    def get_pck_w(self):    
        return self.egg_white // 180
    egg_white_p = property(get_pck_w)

    # --porcentaje de muertes
    def get_un_w(self):
        return self.egg_white % 180
    egg_white_u = property(get_un_w)

    # huevos rotos (x unidades solo produccion)
    egg_break = models.IntegerField(default=0)
    
    # --porcentaje de muertes 
    def get_pck_b(self):    
        return self.egg_break // 180
    egg_break_p = property(get_pck_b)

    # --porcentaje de muertes
    def get_un_b(self):
        return self.egg_break % 180
    egg_break_u = property(get_un_b)

    # huevos sucios (solo produccion)
    egg_dirty = models.IntegerField(default=0)

    # --porcentaje de muertes 
    def get_pck_d(self):    
        return self.egg_dirty // 180
    egg_dirty_p = property(get_pck_d)

    # --porcentaje de muertes
    def get_un_d(self):
        return self.egg_dirty % 180
    egg_dirty_u = property(get_un_d)

    # tipo de comida
    food_type = models.CharField(max_length=1, choices=FOOD_CHOICES, blank=True)

    # precio del alimento
    food_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    # porcentaje de postura
    posture_percentaje =  models.DecimalField(max_digits=5, decimal_places=2,default=0)

    # conversion
    convertion = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    # peso de gallina
    chicken_weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    # peso huevos
    egg_weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    # consumo de aves por dia    
    def get_consume(self):  
        return round(self.food_consumption / self.chicken_income , 3)
    consume = property(get_consume)  

    # porcentaje de muertes
    def get_death(self):
        if self.chicken_death != 0 and self.chicken_initial !=0 :
            return round(100 - ((self.chicken_income * 100)/self.chicken_initial) , 3)
        else:
            return 0
    pocent_death = property(get_death)

@receiver(post_save, sender=ShedRegister)
def update_data(sender, instance, created,**kwargs):
    if created:
        post_save.disconnect(update_data, sender=ShedRegister)
        instance.chicken_initial = instance.shed.promotion.quantity
        instance.save()
        instance.food_deposit = instance.shed.promotion.food
        instance.save()
        instance.age_chicken = instance.shed.promotion.week_age
        instance.save()
        instance.final_deposit = (instance.food_income + instance.shed.promotion.food) - instance.food_consumption
        instance.save()
        instance.chicken_income = instance.shed.promotion.quantity - instance.chicken_death
        instance.save()
        instance.shed.promotion.food = (instance.food_income + instance.shed.promotion.food) - instance.food_consumption
        instance.shed.promotion.save()
        instance.shed.promotion.quantity = instance.shed.promotion.quantity - instance.chicken_death
        instance.shed.promotion.save()

        post_save.connect(update_data, sender=ShedRegister)        
    if created == False:
        post_save.disconnect(update_data, sender=ShedRegister)
        instance.shed.promotion.quantity = instance.chicken_initial - instance.chicken_death
        instance.shed.promotion.save()
        instance.shed.promotion.food = (instance.food_income + instance.food_deposit) - instance.food_consumption
        instance.shed.promotion.save()
        instance.chicken_income = instance.chicken_initial - instance.chicken_death
        instance.save()
        instance.final_deposit = (instance.food_income + instance.food_deposit) - instance.food_consumption
        instance.save()
        post_save.connect(update_data, sender=ShedRegister)        

    



    
  

    
    