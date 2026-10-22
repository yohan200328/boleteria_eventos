from django.contrib import admin
from .models import DetalleCompra

@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('pk', 'compra', 'localidad', 'det_cantidad', 'det_subtotal')
    search_fields = ('compra__pk', 'localidad__loc_nombre')
    list_filter = ('localidad',)