# Generated by Django 3.2 on 2021-05-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210504_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivos',
            name='imagenes',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='area',
            name='operando',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], default='No', max_length=2, verbose_name='Operando'),
        ),
        migrations.AlterField(
            model_name='plandecontingencia',
            name='activo',
            field=models.CharField(choices=[('Iniciado', 'Iniciado'), ('En Evaluación', 'En Evaluación'), ('En proceso', 'En proceso'), ('Finalizado', 'Finalizado'), ('Desconocido', 'Desconocido')], default='Desconocido', max_length=13, verbose_name='Estado del plan'),
        ),
    ]