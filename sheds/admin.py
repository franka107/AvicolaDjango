from django.contrib import admin

# Register your models here.
from .models import Shed, ShedRegister

class ShedAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm', 'type')



admin.site.register(Shed, ShedAdmin)
admin.site.register(ShedRegister)