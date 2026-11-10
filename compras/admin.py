from django.contrib import admin
from .models import Compra
from detalles_compra.models import DetalleCompra

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cliente', 'com_fecha', 'com_total')
    search_fields = ('cliente__cli_nombre', 'cliente__cli_documento')
    list_filter = ('com_fecha',)
    inlines = [DetalleCompraInline]