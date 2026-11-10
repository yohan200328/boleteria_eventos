from django.contrib import admin
from .models import Evento
from localidades.models import Localidad

class LocalidadInline(admin.TabularInline):
    model = Localidad
    extra = 1

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'eve_nombre', 'lugar', 'eve_fecha_hora')
    search_fields = ('eve_nombre', 'eve_descripcion')
    list_filter = ('eve_fecha_hora', 'lugar')
    inlines = [LocalidadInline]