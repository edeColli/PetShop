import pytest
from datetime import date, timedelta
from pytest_django.asserts import assertTemplateUsed


def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva.html')

def test_contato_view_deve_retornar_template(client):
    response = client.get('/contato/')

    assert  response.status_code == 200
    assertTemplateUsed(response='contato.html')

@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client):
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'John Doe',
        'email': 'johndoe@email.com',
        'nome_pet': 'Tom',
        'data': amanha,
        'horario': '10:00',
        'tamanho': 0,
        'observacoes': 'usar shampoo neutro'
    }
    response = client.post('/reserva/', dados)
    assert response.status_code == 200
    assert 'Reserva efetuada com sucesso' in str(response.content)