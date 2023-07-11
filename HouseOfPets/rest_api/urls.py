from django.urls import path
from rest_api.views import hello_world, AgendamentoModelViewSet, PetshopModelViewSet, CategoriaModelViewSet
from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

#Uma maneira de definir rotas
urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
]

#Outra maneira de definir rotas
#por padrao o SimpleRouter() sempre adicionar uma / no final da rota, para que isso não acontece tem que adicionar o parametro trailing_slash
router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet, basename='agendamentos')
router.register('petshop', PetshopModelViewSet, basename='petshop')
router.register('categorias', CategoriaModelViewSet, basename='categorias')

urlpatterns += router.urls