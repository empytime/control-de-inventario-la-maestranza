# inventario/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'inventario'  # Define el app_label para asociar el modelo a la aplicación 'inventario'