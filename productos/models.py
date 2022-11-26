from django.db import models


class Producto (models.Model):
    nombre     = models.CharField(max_length=255)
    precio     = models.FloatField(blank=True, null=True)
    stock      = models.IntegerField(blank=True)
    url_imagen = models.CharField(max_length=2083)