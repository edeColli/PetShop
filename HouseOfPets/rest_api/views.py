from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Reserva
from core.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer
from rest_api.serializers import PetshopModelSerializer
from datetime import date
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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
class PetshopModelViewSet(ModelViewSet):
    serializer_class = PetshopModelSerializer
    queryset = Petshop.objects.all()
    authentication_classes = [TokenAuthentication]    
    permission_classes = [IsAuthenticatedOrReadOnly]

class AgendamentoModelViewSet(ModelViewSet):
    serializer_class = AgendamentoModelSerializer
    queryset = Reserva.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #filterset_fields = ['data', 'isFinalizado', 'categoria']
    filterset_class = ReservaFilterSet

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'World API'})
