# Generated by Django 4.0 on 2022-12-14 03:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productor', '0005_localsale_editable_offer_editable'),
    ]

    operations = [
        migrations.AddField(
            model_name='localsale',
            name='published',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]