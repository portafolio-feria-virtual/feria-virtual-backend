# Generated by Django 4.0 on 2022-11-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercianteExtranjero', '0004_alter_licitacion_extranjero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacion',
            name='closeDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='licitacion',
            name='initDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]