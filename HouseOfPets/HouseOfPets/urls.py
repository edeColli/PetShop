"""
URL configuration for HouseOfPets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.Views.contato import contato
from core.Views.reserva import reserva
from core.Views.signup import signup
from core.Views.signin import signin
from core.Views.reservas import reservas
from core.Views.reserva_detalhe import reserva_detalhe, finalizar_reserva, excluir_reserva
from core import views


urlpatterns = [    
    path("", views.inicio, name='unicio'),
    path("about/", views.sobre, name='sobre'),
    path("sair/", views.sair),
    path("admin/", admin.site.urls),
    path("contato/", contato, name='contato'),
    path("reserva/", reserva, name='reserva'),
    path("signup/", signup, name='signup'),
    path("signin/", signin, name='signin'),
    path("reservas/", reservas, name='reservas'),
    path('reserva/<int:reserva_id>/', reserva_detalhe, name='reserva_detalhe'),
    path('finalizar_reserva/<int:reserva_id>', finalizar_reserva, name='finalizar_reserva'),
    path("excluir_reserva/<int:reserva_id>", excluir_reserva, name='excluir_reserva'),
]
