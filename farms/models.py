from django.db import models

# Create your models here.

class Farm(models.Model):
    
    # nombre de granja
    name = models.CharField(
        max_length=50,
        unique=True)
    
    # estado
    is_active = models.BooleanField(
        default=True,
    )

    # fecha de creacion
    created = models.DateTimeField(
        auto_now_add=True,
    )

    # fecha de actualizacion
    updated = models.DateTimeField(
        auto_now=True,
    )
    
    class Meta:
        verbose_name = "Farm"
        verbose_name_plural = "Farms"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Farm_detail", kwargs={"pk": self.pk})



