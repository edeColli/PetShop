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
from core import views

urlpatterns = [    
    path("", views.inicio),
    path("contato/", views.contato),
    path("reserva/", views.reserva),
    path("about/", views.sobre),
    path("signup/", views.signup),
    path("signin/", views.signin),
    path("dashboard/", views.dashboard),
    path('reserva/<int:reserva_id>/', views.reserva_detalhe, name='reserva_detalhe'),    
    path('finalizar_reserva/<int:reserva_id>', views.finalizar_reserva, name='finalizar_reserva'),
    path("excluir_reserva/<int:reserva_id>", views.excluir_reserva, name='excluir_reserva'),
    path("sair/", views.sair),
    path("admin/", admin.site.urls),
]
