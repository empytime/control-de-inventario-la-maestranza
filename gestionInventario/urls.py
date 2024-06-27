from django.contrib import admin
from django.urls import include, path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # Ruta para la página de inicio
    path('inventario/', include('inventario.urls')),
]