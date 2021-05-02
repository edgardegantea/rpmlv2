from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Informacion)
class InformacionAdmin(admin.ModelAdmin):
    list_display = ('privacidad', 'nombre', 'nombreContro', 'telefono')
    # list_filter = ('nombre', 'nombreContro', 'telefono')
    ordering = ('privacidad', 'nombre', 'nombreContro', 'telefono')
    search_fields = ['nombre', 'nombreContro', 'telefono']


@admin.register(Temperatura)
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ('temperaturaMinima', 'temperaturaMaxima', 'temperaturaLeida')
    # list_filter = ('temperaturaMaxima', 'temperaturaLeida')
    ordering = ('temperaturaMinima', 'temperaturaMaxima', 'temperaturaLeida')
    search_fields = ['temperaturaMinima', 'temperaturaMaxima', 'temperaturaLeida']


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    # list_display_links = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    # list_filter = ('clave', 'nombre', 'ubicacion', 'operando')
    ordering = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    search_fields = ['clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando']


@admin.register(PlanDeContingencia)
class PlanDeContingenciaAdmin(admin.ModelAdmin):
    list_display = ('area', 'nombre', 'activo')
    # list_filter = ('area', 'nombre', 'activo')
    ordering = ('area', 'nombre', 'activo')
    search_fields = ['area', 'nombre', 'activo']



@admin.register(MonitorSequia)
class MonitorSequiaAdmin(admin.ModelAdmin):
    list_display = ('intensidad', 'descripcion')
    list_filter = ('intensidad', 'descripcion')
    ordering = ('intensidad', 'descripcion')
    search_fields = ['intensidad', 'descripcion']
