from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Reserva

@login_required
def reservas(request):
  usuario_admin = request.user.is_superuser
  if usuario_admin:
    reservas = Reserva.objects.filter(isFinalizado=False).order_by('data','horario')
  else:
    reservas = Reserva.objects.filter(user=request.user, isFinalizado=False).order_by('data','horario')

  return render(request, 'reservas.html', {'reservas': reservas, 'usuario_admin': usuario_admin})

