import pytest
from model_bakery import baker
from core.models import Reserva

@pytest.fixture
def agendamento():
    return baker.make(Reserva)