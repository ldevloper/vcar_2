"""vcar URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import index, listar_carros, detalhar_carro, realizar_aluguel, realizar_cadastro

urlpatterns = [
    path('carros/', listar_carros, name='listar_carros'),
    path('carros/<str:pk>', detalhar_carro, name='detalhar_carro'),
    path('aluguel/',realizar_aluguel, name='realizar_aluguel'),
    path('clientes/cadastrar',realizar_cadastro, name='realizar_cadastro'),
]