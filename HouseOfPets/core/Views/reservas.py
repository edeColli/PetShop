from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Reserva

@login_required
def reservas(request):  
  if request.user.is_superuser:
    reservas = Reserva.objects.filter(isFinalizado=False).order_by('data','horario')
  else:
    reservas = Reserva.objects.filter(user=request.user, isFinalizado=False).order_by('data','horario')

  return render(request, 'reservas.html', {'reservas': reservas})

