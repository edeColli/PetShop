from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from ..models import Reserva

@login_required
def reservas(request):
  usuario_admin = request.user.is_superuser

  # Obter o valor do parâmetro filtro_data da solicitação GET
  dateFilter = request.GET.get('dateFilter')

  if usuario_admin:
    reservas = Reserva.objects.filter(isFinalizado=False).order_by('data','horario')
  else:
    reservas = Reserva.objects.filter(user=request.user, isFinalizado=False).order_by('data','horario')

  if dateFilter:
      #Converter o filtro_data em objeto datetime
      filteredDate = datetime.strptime(dateFilter, '%Y-%m-%d').date()
      #Filtrar as reservas pela data
      reservas = reservas.filter(data=filteredDate)

  return render(request, 'reservas.html', {'reservas': reservas, 'usuario_admin': usuario_admin})

