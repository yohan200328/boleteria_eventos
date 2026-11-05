from django.db import models
from lugares.models import Lugar

class Evento(models.Model):
    lugar = models.ForeignKey(
        Lugar, 
        on_delete=models.CASCADE, 
        db_column='fk_lug_id', 
        related_name='eventos'
    )
    eve_nombre = models.CharField(max_length=200)
    eve_descripcion = models.TextField()
    eve_fecha_hora = models.DateTimeField()

    def __str__(self):
        return self.eve_nombre