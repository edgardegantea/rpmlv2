# Generated by Django 3.2 on 2021-05-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210504_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivos',
            name='imagenes',
            field=models.ImageField(upload_to='imgcultivos', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='plandecontingencia',
            name='activo',
            field=models.CharField(choices=[('En proceso', 'En proceso'), ('Iniciado', 'Iniciado'), ('Desconocido', 'Desconocido'), ('Finalizado', 'Finalizado'), ('En Evaluación', 'En Evaluación')], default='Desconocido', max_length=13, verbose_name='Estado del plan'),
        ),
    ]
