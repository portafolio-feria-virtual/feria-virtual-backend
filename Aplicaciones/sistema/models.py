
import uuid
from django.db import models
from django.utils.text import slugify
from Aplicaciones.cuentas.models import usuarios
from dateutil.relativedelta import relativedelta
from django.conf import settings
import datetime

class Contrato(models.Model):
    id_contrato = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    rut_persona = models.CharField(max_length=20)
    telefono_contacto = models.CharField(max_length=25)
    fec_emision_contrato = models.DateField(default=datetime.date.today(),blank= True)
    fec_fin_contrato= models.DateField(default=datetime.date.today()+ relativedelta(years = 1), blank = True) 
    estado = models.BooleanField(default = False)

class Transporte(models.Model):
    id_trans = models.AutoField(primary_key=True)
    tip_transporte = models.CharField(max_length=15)
    tamano_trans = models.IntegerField()
    capacidad_trans = models.IntegerField()
    refrigeracion_trans = models.CharField(max_length=10)
    fecha_trans = models.DateField()
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,models.DO_NOTHING)

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = "Transportes"
        db_table="Transporte"

class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=20)
    precio_prod = models.IntegerField()
    desc_prod = models.CharField(max_length=200)
    stock_prod = models.IntegerField()
    id_usuario = models.ForeignKey(usuarios,models.DO_NOTHING)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = "Productos"
        db_table="Producto"

class Pedido(models.Model):
    id_ped = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)
    fecha = models.DateField()
    descrip = models.CharField(max_length=200)
    id_usuario = models.ForeignKey(usuarios,models.DO_NOTHING)
    productos_id_prod = models.ForeignKey(Productos,models.DO_NOTHING, blank=True, null=True)
    estado_admin = models.BooleanField(default = False)
    estado_productor = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = "Pedidos"
        db_table="Pedido"

class ProcesPedido(models.Model):
    id_proc_pedido = models.AutoField(primary_key=True)
    transporte_id_trans = models.ForeignKey(Transporte,models.DO_NOTHING)
    pedido_id_ped = models.ForeignKey(Pedido,models.DO_NOTHING)
    estado_proceso = models.BooleanField(default = False)
    class Meta:
        verbose_name = 'ProcesPedido'
        verbose_name_plural = "ProcesosPedidos"
        db_table="ProcesPedido"
class ProcesVenta(models.Model):
    id_proc_venta = models.IntegerField(primary_key=True)
    proces_pedido_id_proc_pedido = models.ForeignKey(ProcesPedido,models.DO_NOTHING)

    class Meta:
        verbose_name = 'ProcesVenta'
        verbose_name_plural = "ProcesosVenta"
        db_table="ProcesVenta"

class DetallCompra(models.Model):
    id_detall = models.IntegerField(primary_key=True)
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta,models.DO_NOTHING)
    fecha_detall = models.DateField()
    nom_producto = models.CharField(max_length=15)
    cost_producto = models.IntegerField()
    iva_producto = models.IntegerField()
    total_compra = models.IntegerField()

    class Meta:
        verbose_name = 'DetallCompra'
        verbose_name_plural = "DetallesCompras"
        db_table="DetallCompra"


class VentExtran(models.Model):
    id_vent_ex = models.CharField(primary_key=True, max_length=10)
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta,models.DO_NOTHING)
    nom_cli = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20)
    ape_mat = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'VentExtran'
        verbose_name_plural = "VentasExtranjeras"
        db_table="VentExtran"



class DirecExtran(models.Model):
    vent_extran_id_vent_ex = models.ForeignKey(VentExtran,models.DO_NOTHING)
    id_direc = models.CharField(primary_key=True, max_length=20)
    pais = models.CharField(max_length=20)
    direc_cli = models.CharField(max_length=20)
    num_calle = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=10, blank=True, null=True)
    localidad = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'DirecExtran'
        verbose_name_plural = "DireccionesExtranjeras"
        db_table="DirecExtran"

class VentLocal(models.Model):
    id_vent_loc = models.CharField(primary_key=True, max_length=10)
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta,models.DO_NOTHING)
    nom_cli = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20)
    ape_mat = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'VentLocal'
        verbose_name_plural = "VentasLocales"
        db_table="VentLocal"

class DirecLocal(models.Model):
    id_direc = models.CharField(primary_key=True, max_length=20)
    direc_cli = models.CharField(max_length=20)
    num_calle = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=20)
    comuna = models.CharField(max_length=20)
    vent_local_id_vent_loc = models.ForeignKey(VentLocal,models.DO_NOTHING)

    class Meta:
        verbose_name = 'DirecLocal'
        verbose_name_plural = "DireccionesLocales"
        db_table="DirecLocal"


class ReportMerma(models.Model):
    id_merma = models.IntegerField(primary_key=True)
    fecha_merma = models.DateField()
    descrip_merma = models.CharField(max_length=40)
    id_usuario = models.ForeignKey(usuarios,models.DO_NOTHING)

    class Meta:
        verbose_name = 'ReportMerma'
        verbose_name_plural = "ReportesMermas"
        db_table="ReportMerma"


class ReportVenta(models.Model):
    id_report_vent = models.IntegerField(primary_key=True)
    prod_venta = models.CharField(max_length=20)
    cant_venta = models.IntegerField()
    total_venta = models.IntegerField()
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta,models.DO_NOTHING)

    class Meta:
        verbose_name = 'ReportVenta'
        verbose_name_plural = "ReportesVentas"
        db_table="ReportVenta"


class Reportes(models.Model):
    id_report = models.IntegerField(primary_key=True)
    fecha_report = models.DateField()
    tip_report = models.CharField(max_length=15)
    user_report = models.CharField(max_length=15)
    descrip_report = models.CharField(max_length=30)
    id_user = models.ForeignKey(usuarios,models.DO_NOTHING)

    class Meta:
        verbose_name = 'Reportes'
        verbose_name_plural = "Reportes"
        db_table="Reportes"


class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    estados = (('preparando','preparando productos'),('despacho','productos despachados'),
        ('recepcionados','recepcionados por el transportista'),('viaje','en camino'),('completado','seguimiento finalizado'))
    est_seguimiento = models.CharField(max_length=50,choices=estados,default='preparando')
    pedido_id_ped = models.ForeignKey(Pedido,models.DO_NOTHING)
    proces_pedido_id_proc_pedido = models.ForeignKey(ProcesPedido,models.DO_NOTHING)

    class Meta:
        verbose_name = 'Seguimiento'
        verbose_name_plural = "Seguimiento"
        db_table="Seguimiento"





# class UsuariosUsuarios(models.Model):
#     id_user = models.AutoField(primary_key=True)
#     password = models.CharField(max_length=128, blank=True, null=True)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=50, blank=True, null=True)
#     email = models.CharField(unique=True, max_length=254, blank=True, null=True)
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     direccion = models.CharField(max_length=50, blank=True, null=True)
#     is_active = models.BooleanField()
#     is_staff = models.BooleanField()
#     tipo_usuario = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'usuarios_usuarios'









