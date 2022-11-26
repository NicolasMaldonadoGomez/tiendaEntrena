from django.contrib import admin
from .models import Producto, Oferta

class AdministracionProductos(admin.ModelAdmin):
    list_display = ("nombre", "precio","stock")

class AdministracionOfertas(admin.ModelAdmin):
    list_display= ("codigo", "descripcion", "descuento")

admin.site.register(Producto,AdministracionProductos)
admin.site.register(Oferta,AdministracionOfertas)
