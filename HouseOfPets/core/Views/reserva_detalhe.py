from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.forms import ReservaForm
from ..models import Reserva

RESERVAS = '/reservas/'
RESERVA_DETALHE = 'reserva_detalhe.html'

@login_required
def reserva_detalhe(request, reserva_id):
  if request.method == 'GET':
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    form = ReservaForm(instance=reserva)
    return render(request, RESERVA_DETALHE, {'reserva': reserva, 'form': form})
  else:
    try:
      reserva = get_object_or_404(Reserva, pk=reserva_id)
      form = ReservaForm(request.POST, instance=reserva)
      if form.is_valid():
        reserva = form.save()
      return redirect('/reservas/')
    except ValueError:
      return render(request, RESERVA_DETALHE, {
        'reserva': reserva,
        'form': form,
        'error': 'Erro ao atualizar a reserva!'
      })

@login_required
def finalizar_reserva(request, reserva_id):  
  reserva = get_object_or_404(Reserva, pk=reserva_id)
  if request.method == 'POST':
    reserva.isFinalizado = True
    reserva.save()
    messages.success(request, 'Reserva ' + str(reserva_id) + ' finalizada com sucesso!')
    return redirect(RESERVAS)

@login_required
def excluir_reserva(request, reserva_id):
  reserva = get_object_or_404(Reserva, pk=reserva_id)
  if request.method == 'POST':
    reserva.delete()
    messages.warning(request, 'Reserva ' + str(reserva_id) + ' excluída com sucesso!')
    return redirect(RESERVAS)