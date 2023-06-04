from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from ..models import Reserva

@login_required
def reservas(request):
  usuario_admin = request.user.is_superuser

  # Obter o valor do parâmetro dateFilter da solicitação GET
  dateFilter = request.GET.get('dateFilter')
  closed = request.GET.get('finalizadas')

  if usuario_admin:
    reservas = Reserva.objects.all().order_by('data','horario')
  else:
    reservas = Reserva.objects.filter(user=request.user, isFinalizado=False).order_by('data','horario')

  if dateFilter:
      #Converter o dateFilter em objeto datetime
      filteredDate = datetime.strptime(dateFilter, '%Y-%m-%d').date()
      #Filtrar as reservas pela data
      reservas = reservas.filter(data=filteredDate)  

  if not closed:
    reservas = reservas.filter(isFinalizado=False)


  return render(request, 'reservas.html', {'reservas': reservas, 'usuario_admin': usuario_admin})

