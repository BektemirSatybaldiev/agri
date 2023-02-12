from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import Farmer, Plot, Culture, Season


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'email']
    search_fields = ['id', 'name', 'address', 'email']


@admin.register(Plot)
class PlotAdmin(gis_admin.GISModelAdmin):
    list_display = ['farmer', 'culture']
    search_fields = ['__all__']


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    search_fields = ['name']
