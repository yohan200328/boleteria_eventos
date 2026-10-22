from django.contrib import admin
from .models import Lugar

@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'lug_nombre', 'lug_direccion', 'lug_ciudad')
    search_fields = ('lug_nombre', 'lug_ciudad')
    list_filter = ('lug_ciudad',)