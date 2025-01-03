from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Asegúrate de tener una vista para la raíz
] 