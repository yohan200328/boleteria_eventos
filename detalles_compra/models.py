from django.db import models
from compras.models import Compra
from localidades.models import Localidad

class DetalleCompra(models.Model):
    compra = models.ForeignKey(
        Compra, 
        on_delete=models.CASCADE, 
        db_column='fk_com_id', 
        related_name='detalles'
    )
    localidad = models.ForeignKey(
        Localidad, 
        on_delete=models.CASCADE, 
        db_column='fk_loc_id', 
        related_name='detalles'
    )
    det_cantidad = models.IntegerField()
    det_subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle Compra #{self.compra.pk} - Zona: {self.localidad.loc_zona}"