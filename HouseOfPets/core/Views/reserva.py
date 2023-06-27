from datetime import date
from django.shortcuts import render
from ..models import Reserva
from core.forms import ReservaForm
from django.contrib.auth.decorators import login_required

@login_required
def reserva(request):
    sucesso = False
    data_atual = date.today()
    reservas = Reserva.objects.filter(isFinalizado=False,  data=data_atual).order_by('data', 'horario')
    horas_disponiveis = ['07:00', '08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    horarios_ocupados = [reserva.horario for reserva in reservas]

    if request.method == 'GET':
      form = ReservaForm()
    else:
      form = ReservaForm(request.POST)
      if form.is_valid():
        reserva = form.save(commit=False)
        reserva.user = request.user
        reserva.save()
        sucesso = True

        reservas = Reserva.objects.filter(isFinalizado=False, data=data_atual).order_by('data', 'horario')
        horarios_ocupados = [reserva.horario for reserva in reservas]
      else:
        print('o form não esta valido')
    context = {
        'formulario': form,
        'sucesso': sucesso,
        'reservas': reservas,
        'horas_disponiveis': horas_disponiveis,
        'horarios_ocupados': horarios_ocupados
    }

    return render(request, 'reserva.html', context)