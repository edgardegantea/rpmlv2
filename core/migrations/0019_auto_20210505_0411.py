# Generated by Django 3.2 on 2021-05-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210505_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='censotemperatura',
            name='temperatura',
        ),
        migrations.AddField(
            model_name='censotemperatura',
            name='temperatura1',
            field=models.DecimalField(decimal_places=1, default=26.0, max_digits=5, max_length=6, verbose_name='Temperatura del suelo'),
        ),
        migrations.AddField(
            model_name='censotemperatura',
            name='temperatura2',
            field=models.DecimalField(decimal_places=1, default=27.0, max_digits=5, max_length=6, verbose_name='Temperatura ambiental'),
        ),
        migrations.AlterField(
            model_name='cultivos',
            name='mesDeSiembra',
            field=models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero')], default='Enero', max_length=30, verbose_name='Mes de siembra'),
        ),
        migrations.AlterField(
            model_name='plandecontingencia',
            name='activo',
            field=models.CharField(choices=[('Finalizado', 'Finalizado'), ('En proceso', 'En proceso'), ('Iniciado', 'Iniciado'), ('En Evaluación', 'En Evaluación'), ('Desconocido', 'Desconocido')], default='Desconocido', max_length=13, verbose_name='Estado del plan'),
        ),
    ]
