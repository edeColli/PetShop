# def __str__(self):
#         return f'{self.nome} [{self.data}] [{self.categoria}]'

from datetime import date
import pytest
from model_bakery import baker
from core.models import Reserva
from core.models import Categoria
from core.models import Petshop

@pytest.fixture
def reserva():
    data = date.today()
    reserva = baker.make(
        Reserva,
        nome = 'Tom',
        data = data,
        horario = '09:00'
    )
    return reserva


@pytest.mark.django_db
def test_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == f'Tom [{date.today()}] [09:00]'

@pytest.mark.django_db
def test_quantidade_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 3
    baker.make(
        Reserva,
        quantidade,
        petshop=petshop
    )
    assert petshop.quantidade_reservas() == 3