from django.db import models


class Oferta (models.Model):
    code        = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=50)
    descuento   = models.FloatField(null=True)