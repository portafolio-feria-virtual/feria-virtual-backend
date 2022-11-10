from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Contrato)
admin.site.register(Productos)
admin.site.register(Transporte)
admin.site.register(Pedido)
admin.site.register(ProcesPedido)
admin.site.register(ProcesVenta)
admin.site.register(DetallCompra)
admin.site.register(VentExtran)
admin.site.register(DirecExtran)
admin.site.register(VentLocal)
admin.site.register(DirecLocal)
admin.site.register(ReportMerma)
admin.site.register(ReportVenta)
admin.site.register(Reportes)
admin.site.register(Seguimiento)


