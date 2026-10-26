from django.contrib import admin
from django.contrib.admin import ModelAdmin

from vehicles.models import ClassicCar


# Register your models here.
@admin.register(ClassicCar)
class ClassicCarAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'manufacture_year', 'vin')
    list_filter = ('manufacturer', 'manufacture_year')
    search_fields = ('model_name', 'vin')