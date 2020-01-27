from django.db import models
from sheds.models import Shed
from django.utils import timezone

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
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    def _get_final(self):
        return round((timezone.now()-self.created).days/7,0)
       
    week_age = property(_get_final)


    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Promotion_detail", kwargs={"pk": self.pk})
