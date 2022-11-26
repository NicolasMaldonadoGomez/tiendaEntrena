from django.contrib import admin
from .models import Producto

class AdministracionProducto(admin.ModelAdmin):
    list_display = ("nombre", "precio","stock")

admin.site.register(Producto,AdministracionProducto)
