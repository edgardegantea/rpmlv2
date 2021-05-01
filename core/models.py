from django.db import models


# Create your models here.
class Informacion(models.Model):
    privacidad = models.TextField(verbose_name='Política de privacidad', max_length=5000)
    nombre = models.CharField(verbose_name='Nombre de la aplicación', max_length=100)
    nombreContro = models.CharField(verbose_name='Nombre corto', max_length=20)
    telefono = models.CharField(verbose_name='Contacto', max_length=100)

    def __str__(self):
        return self.nombreContro

    class Meta:
        verbose_name='Información'
        verbose_name_plural='Datos de la aplicación'


# Temperaturas
class Temperatura(models.Model):
    temperaturaMinima = models.DecimalField(verbose_name='Temperatura mínima', max_digits=2, decimal_places=2,
                                            default=0.00)
    temperaturaMaxima = models.DecimalField(verbose_name='Temperatura máxima', max_digits=2, decimal_places=2, default=0.00)
    temperaturaLeida = models.DecimalField(verbose_name='Temperatura leída', max_digits=2, decimal_places=2, default=0.00)

    def __str__(self):
        return self.temperaturaLeida

    class Meta:
        verbose_name='Temperatuta'
        verbose_name_plural='Temperaturas'


class Area(models.Model):
    clave = models.CharField(verbose_name='Clave', max_length=10)
    nombre = models.CharField(verbose_name='Lugar', max_length=200)
    ubicacion = models.CharField(verbose_name='Ubicación', max_length=255)
    altitud = models.CharField(verbose_name='Altitud', max_length=20)
    latitud = models.CharField(verbose_name='Latitud', max_length=12)
    longitud = models.CharField(verbose_name='Longitud', max_length=12)
    OP = {('Sí', 'Sí'), ('No', 'No')}
    operando = models.CharField(verbose_name='Operando', default='No', choices=OP, max_length=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Ubicación'
        verbose_name_plural='Datos de la ubicación'


class PlanDeContingencia(models.Model):
    area = models.ForeignKey(Area, verbose_name='área', on_delete=models.DO_NOTHING)
    nombre = models.CharField(verbose_name='Nombre del plan', max_length=255)
    OPCIONES = {('Desconocido', 'Desconocido'), ('Iniciado', 'Iniciado'), ('En proceso', 'En proceso'), ('Finalizado', 'Finalizado'), ('En Evaluación', 'En Evaluación')}
    activo = models.CharField(verbose_name='Estado del plan', choices=OPCIONES, max_length=13, default='Desconocido')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Plan de contingencia'
        verbose_name_plural='Planes de contingencia'


class MonitorSequia(models.Model):
    intensidad = models.CharField(verbose_name='Intensidad de la sequía', max_length=50)
    descripcion = models.TextField(verbose_name='Descripción', max_length=5000)

    def __str__(self):
        return self.intensidad

    class Meta:
        verbose_name='Monitor de sequía'
        verbose_name_plural='Datos de la sequía'
