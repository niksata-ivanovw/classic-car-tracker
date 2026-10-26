from django.contrib import admin

from brands.models import Manufacturer


# Register your models here.
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'established_year')
    search_fields = ('name', 'country')