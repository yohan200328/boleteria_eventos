from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cli_nombre', 'cli_apellido', 'cli_documento', 'cli_telefono', 'cli_email')
    search_fields = ('cli_nombre', 'cli_apellido', 'cli_documento')  # <--- Añadir esto
    list_filter = ('cli_email',)                                    # <--- Añadir esto