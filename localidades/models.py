from django.db import models
from eventos.models import Evento

class Localidad(models.Model):
    evento = models.ForeignKey(
        Evento, 
        on_delete=models.CASCADE, 
        db_column='fk_eve_id', 
        related_name='localidades'
    )
    loc_zona = models.CharField(max_length=50)
    loc_precio = models.DecimalField(max_digits=10, decimal_places=2)
    loc_cupo_total = models.IntegerField()

    def __str__(self):
        return f"{self.loc_zona} - {self.evento.eve_nombre}"