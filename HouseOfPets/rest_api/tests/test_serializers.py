import pytest
import datetime
from model_bakery import baker
from core.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop = baker.make(Petshop)
    return {
        'nome': 'John Doe',
        'email': 'John@email.com',
        'nome_pet': 'Tom',
        'data': ontem,
        'tamanho': 0,
        'observacoes': '',
        'petshop': petshop.pk,
    }

@pytest.mark.django_db
def test_data_agendamento_invalida(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
    assert not serializer.is_valid()