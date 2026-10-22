from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        db_column='user_id', 
        related_name='cliente_perfil'
    )
    cli_nombre = models.CharField(max_length=100)
    cli_apellido = models.CharField(max_length=100)
    cli_documento = models.CharField(max_length=20, unique=True)
    cli_telefono = models.CharField(max_length=20)
    cli_email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.cli_nombre} {self.cli_apellido} ({self.cli_documento})"