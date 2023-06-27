from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Reserva
from rest_api.serializers import AgendamentoModelSerializer
from datetime import date
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AgendamentoModelViewSetFinalizados(ModelViewSet):
    queryset = Reserva.objects.all().filter(isFinalizado=True)
    serializer_class = AgendamentoModelSerializer

class AgendamentoModelViewSetAtivos(ModelViewSet):
    queryset = Reserva.objects.all().filter(isFinalizado=False)
    serializer_class = AgendamentoModelSerializer

class AgendamentoModelViewSetDoDia(ModelViewSet):
    dataAtual = date.today()
    queryset = Reserva.objects.all().filter(data=dataAtual)
    serializer_class = AgendamentoModelSerializer

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'World API'})
