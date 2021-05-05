from django.contrib import admin
from django.utils.html import format_html

from .models import *


# Register your models here.
@admin.register(Informacion)
class InformacionAdmin(admin.ModelAdmin):
    list_display = ('privacidad', 'nombre', 'nombreContro', 'telefono')
    # list_filter = ('nombre', 'nombreContro', 'telefono')
    ordering = ('privacidad', 'nombre', 'nombreContro', 'telefono')
    search_fields = ['nombre', 'nombreContro', 'telefono']
    list_per_page = 10
    empty_value_display = '-empty-'


@admin.register(Temperatura)
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ('temperaturaMinima', 'temperaturaMaxima', 'temperaturaLeida')
    # list_filter = ('temperaturaMaxima', 'temperaturaLeida')
    ordering = ('temperaturaMinima', 'temperaturaMaxima', 'temperaturaLeida')
    search_fields = ['temperaturaMinima', 'temperaturaMaxima', 'temperaturaLeida']
    list_per_page = 10
    empty_value_display = '-empty-'


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    # fields = ['clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'longitud', 'operando']  # Organización de campos
    list_display = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    # list_display_links = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    # list_filter = ('clave', 'nombre', 'ubicacion', 'operando')
    ordering = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    search_fields = ['clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando']
    list_per_page = 10
    empty_value_display = '-empty-'


@admin.register(PlanDeContingencia)
class PlanDeContingenciaAdmin(admin.ModelAdmin):
    list_display = ('area', 'nombre', 'activo')
    # list_filter = ('area', 'nombre', 'activo')
    ordering = ('area', 'nombre', 'activo')
    search_fields = ['area', 'nombre', 'activo']
    list_per_page = 10
    empty_value_display = '-empty-'


@admin.register(MonitorSequia)
class MonitorSequiaAdmin(admin.ModelAdmin):
    list_display = ('intensidad', 'descripcion')
    list_filter = ('intensidad', 'descripcion')
    ordering = ('intensidad', 'descripcion')
    search_fields = ['intensidad', 'descripcion']
    list_per_page = 10
    empty_value_display = '-empty-'


@admin.register(Cultivos)
class CultivosAdmin(admin.ModelAdmin):
    list_filter = ('nombre', 'nombreCientifico', 'descripcion', 'mesDeSiembra')
    list_display = ('imagenes', 'nombre', 'nombreCientifico', 'descripcion', 'mesDeSiembra')
    list_per_page = 3
    ordering = ('nombre',)
    search_fields = ['nombre', 'nombreCientifico', 'descripcion', 'mesDeSiembra']

    def imagenes(self, obj):
        # return format_html('<img src={} />', obj.imagenes.url)
        return format_html('<img src={} />', obj.imagenes.url)


@admin.register(CensoTemperatura)
class CensoTemperaturaAdmin(admin.ModelAdmin):
    list_display = ('Area', 'Cultivo', 'temperatura1', 'temperatura2', 'fecha', 'hora')
    ordering = ('Area', 'Cultivo', 'temperatura1', 'temperatura2', 'fecha', 'hora')
    search_fields = ['Area', 'Cultivo', 'temperatura1', 'temperatura2', 'fecha', 'hora']
    list_per_page = 10
    empty_value_display = '-empty-'



