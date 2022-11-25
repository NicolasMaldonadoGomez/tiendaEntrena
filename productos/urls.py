from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),
    path("nuevo/",views.nuevo)
]