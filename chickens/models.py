from django.db import models
from sheds.models import Shed, ShedRegister
from django.utils import timezone
from datetime import date


class Promotion(models.Model):
    TYPE_CHOICES = [
        ('HSX', 'HYSEX'),
        ('HSN', 'H.NEGRA'),
        ('HYN', 'HYN'),
        ('LMN', 'LOHMAN'),
        ('NVG', 'NOVOGEN')
    ]

    # nombre de promocion de aves
    name = models.CharField(
        max_length=50,
        unique=True)
    # nombre de galpon al que pertenece
    shed = models.OneToOneField(
        Shed,
        on_delete=models.CASCADE
    )
    
    # comida de aves
    food = models.IntegerField(default=0)

    # cantidad de aves
    quantity = models.IntegerField()

    # edad en semana
    week_age = models.IntegerField(default=1)

    # edad en dias
    age_days = models.IntegerField(default=0)

    # tipo de aves
    chicken_type = models.CharField(
        max_length =3,
        choices= TYPE_CHOICES
    )

    # estado
    is_active = models.BooleanField(
        default=False,
    )

    #fecha de creacion
    created = models.DateTimeField(
        auto_now=True,
    )

    #fecha de actualizacion
    updated = models.DateTimeField(
        auto_now=True,
    )
       
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Promotion_detail", kwargs={"pk": self.pk})
