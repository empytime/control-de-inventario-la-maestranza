# inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.lista_productos, name='lista_productos'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
]
