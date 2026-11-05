from django.db import models
from clientes.models import Cliente

class Compra(models.Model):
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        db_column='fk_cli_id', 
        related_name='compras'
    )
    com_fecha = models.DateTimeField(auto_now_add=True)
    com_total = models.DecimalField(max_digits=10, decimal_places=2)
    com_estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Compra #{self.pk} - {self.cliente.cli_documento}"