# Generated by Django 3.2 on 2021-05-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210505_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='operando',
            field=models.CharField(choices=[('No', 'No'), ('Sí', 'Sí')], default='No', max_length=2, verbose_name='Operando'),
        ),
        migrations.AlterField(
            model_name='cultivos',
            name='mesDeSiembra',
            field=models.CharField(choices=[('Febrero', 'Febrero'), ('Enero', 'Enero')], default='Enero', max_length=30, verbose_name='Mes de siembra'),
        ),
        migrations.AlterField(
            model_name='plandecontingencia',
            name='activo',
            field=models.CharField(choices=[('Iniciado', 'Iniciado'), ('En Evaluación', 'En Evaluación'), ('En proceso', 'En proceso'), ('Desconocido', 'Desconocido'), ('Finalizado', 'Finalizado')], default='Desconocido', max_length=13, verbose_name='Estado del plan'),
        ),
    ]
