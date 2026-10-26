from django.contrib import admin

from parts.models import RestorationPart


# Register your models here.
@admin.register(RestorationPart)
class RestorationPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'part_number', 'price')
    search_fields = ('name', 'part_number')