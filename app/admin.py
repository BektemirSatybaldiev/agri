from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import Farmer, Plot, Culture, Season


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'address', 'email']


admin.site.register(Plot, gis_admin.GISModelAdmin)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    search_fields = ['name']
