# Generated by Django 4.0 on 2022-12-09 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_administrador_remove_mercancia_productor_and_more'),
        ('comercianteExtranjero', '0002_initial'),
        ('transportista', '0004_remove_postulacionlicitaciontransporte_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PREPARATION', 'preparation'), ('AWAITING CARRIER', 'awaiting carrier'), ('RECEIVED BY CARRIER', 'received by carrier'), ('ON TRACK', 'on track'), ('RECEPTIONED', 'receptioned')], default='PREPARATION', max_length=30)),
                ('licitacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comercianteExtranjero.licitacion')),
                ('productor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.productor')),
                ('transportista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.transportista')),
            ],
        ),
    ]