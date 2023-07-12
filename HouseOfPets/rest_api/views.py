from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Reserva
from core.models import Petshop
from core.models import Categoria
from rest_api.serializers import AgendamentoModelSerializer
from rest_api.serializers import PetshopModelSerializer
from rest_api.serializers import CategoriaModelSerializer
from datetime import date
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, SAFE_METHODS, AllowAny, IsAdminUser
)
from django_filters.filterset import FilterSet

# Create your views here.

    
class ReservaFilterSet(FilterSet):
    class Meta:
        model = Reserva
        fields = {
            'data': ['gte'],
            'email': ['icontains'],
            'nome': ['icontains'],
            'nome_pet': ['icontains'],
            'isFinalizado': ['exact'],
            'categoria': ['exact'],            
        }

class CategoriaFilterSet(FilterSet):
    class Meta:
        model = Categoria
        fields = {
            'descricao': ['icontains']
        }

class CategoriaModelViewSet(ModelViewSet):    
    serializer_class = CategoriaModelSerializer
    queryset = Categoria.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]    
    filterset_class = CategoriaFilterSet

    @action(detail=True, methods=['GET'])
    def reservas(self, request, pk):
        categoria = self.get_object()
        agendamentos = categoria.agendamentos.all()
        serializer = AgendamentoModelSerializer(instance=agendamentos, many=True)
        return Response(data=serializer.data)
    
class AgendamentoModelViewSet(ModelViewSet):
    serializer_class = AgendamentoModelSerializer    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = ReservaFilterSet
    
    def get_queryset(self):
        if self.request.method in SAFE_METHODS:            
            return Reserva.objects.all()        
        return Reserva.objects.filter(isFinalizado=False)
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user_id=self.request.user.id)
        else:
            serializer.save()

    def get_permissions(self):
    #     print('get_permis')
        if self.action == 'create':
    #         print('action-create')
            return[AllowAny()]
    #     print(self.request.user)
    #     print(self.request.user.is_staff)
        return [IsAdminUser()]

class PetshopModelViewSet(ModelViewSet):
    serializer_class = PetshopModelSerializer
    queryset = Petshop.objects.all()
    authentication_classes = [TokenAuthentication]    
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'World API'})
