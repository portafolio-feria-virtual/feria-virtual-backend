# Generated by Django 4.0 on 2022-12-09 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fileName',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]