# Generated by Django 4.0 on 2022-11-30 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercianteExtranjero', '0005_alter_licitacion_closedate_alter_licitacion_initdate'),
        ('productor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oferta',
            old_name='description',
            new_name='offerDescription',
        ),
        migrations.RenameField(
            model_name='oferta',
            old_name='unitPrice',
            new_name='offerValue',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='adminArchives',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='economicArchives',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='productorDescription',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='techArchives',
        ),
        migrations.AddField(
            model_name='oferta',
            name='licitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comercianteExtranjero.licitacion'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='offerFileName',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]