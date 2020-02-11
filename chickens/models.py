from django.db import models
from sheds.models import Shed, ShedRegister
from django.utils import timezone
from datetime import date

# Create your models here.

class Promotion(models.Model):
    TYPE_CHOICES = [
        ('HSX', 'HYSEX'),
        ('HSN', 'H.NEGRA'),
        ('HYN', 'HYN'),
        ('LMN', 'LOHMAN'),
        ('NVG', 'NOVOGEN')
    ]
    name = models.CharField(
        max_length=50,
        unique=True)
    shed = models.OneToOneField(
        Shed,
        on_delete=models.CASCADE
    )
    
    quantity = models.IntegerField()
    
    entry_date = models.DateField()

    chicken_type = models.CharField(
        max_length =3,
        choices= TYPE_CHOICES
    )
    is_active = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
       
    week_age = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Promotion_detail", kwargs={"pk": self.pk})
