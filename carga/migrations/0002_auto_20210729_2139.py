# Generated by Django 3.2.4 on 2021-07-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remito',
            name='fecharem1',
            field=models.DateField(blank=True, default='2021-01-01', null=True, verbose_name='Fecha remito 1'),
        ),
        migrations.AlterField(
            model_name='remito',
            name='fecharem2',
            field=models.DateField(blank=True, default='2021-01-01', null=True, verbose_name='Fecha remito 1'),
        ),
    ]
