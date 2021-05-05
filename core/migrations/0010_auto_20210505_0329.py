# Generated by Django 3.2 on 2021-05-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210504_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensoTemperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='Temperatura')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora')),
            ],
            options={
                'verbose_name': 'Censo de temperatura',
                'verbose_name_plural': 'Censo de temperatura',
            },
        ),
        migrations.AlterField(
            model_name='cultivos',
            name='mesDeSiembra',
            field=models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero')], default='Enero', max_length=30, verbose_name='Mes de siembra'),
        ),
        migrations.AlterField(
            model_name='plandecontingencia',
            name='activo',
            field=models.CharField(choices=[('En Evaluación', 'En Evaluación'), ('Iniciado', 'Iniciado'), ('Finalizado', 'Finalizado'), ('Desconocido', 'Desconocido'), ('En proceso', 'En proceso')], default='Desconocido', max_length=13, verbose_name='Estado del plan'),
        ),
    ]
