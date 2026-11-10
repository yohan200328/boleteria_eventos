from django.db import models

class Lugar(models.Model):
    lug_nombre = models.CharField(max_length=150)
    lug_direccion = models.CharField(max_length=255)
    lug_ciudad = models.CharField(max_length=100)
    lug_capacidad = models.IntegerField()

    def __str__(self):
        return self.lug_nombre