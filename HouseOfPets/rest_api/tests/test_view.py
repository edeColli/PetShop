import datetime
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from rest_api.serializers import PetshopModelSerializer
from core.models import Petshop


@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'John Doe',
        'email': 'John@email.com',
        'nome_pet': 'Tom',
        'data': hoje,
        'tamanho': 0,
        'observacoes': '',
        'petshop': petshop.pk,
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_todos_petshops():
    client = APIClient()
    resposta = client.get('/api/petshop')
    assert len(resposta.data['results']) == 0

@pytest.mark.django_db
def test_api_petshop_com_petshop_salvo():
    client = APIClient()
    baker.make(Petshop, nome='Petshop House of Pets')
    resposta = client.get('/api/petshop')
    assert len(resposta.data['results']) == 1


#aqui sim carrega do banco de dados
@pytest.mark.django_db
def test_api_petshop_com_petshop_salvo_usando_serializer():
    client = APIClient()
    baker.make(Petshop, nome='Petshop House of Pets')
    resposta = client.get('/api/petshop')
    serializer = PetshopModelSerializer(Petshop.objects.all(), many=True)

    assert resposta.data['results'] == serializer.data

@pytest.mark.django.db
def test_api_agendamento_vazio():
    cliente = APIClient()
    resposta  = cliente.get('/api/agendamento', dados_agendamento)

    assert len(resposta.data['results']) == 0


@pytest.mark.django.db
def test_api_agendamento_com_agendamento_salvo(agendamento):
    cliente = APIClient()
    resposta  = cliente.get('/api/agendamento', dados_agendamento)

    assert len(resposta.data['results']) == 1

# @pytest.mark.django_db
# def test_criar_agendamento(usuario, dados_agendamento):
#     cliente = APIClient()
#     cliente.force_authenticate(usuario)
#     resposta = cliente.post('/api/agendamento', dados_agendamento)
#     assert resposta.status_code == 201    