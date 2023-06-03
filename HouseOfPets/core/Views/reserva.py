from django.shortcuts import render
from core.forms import ReservaForm

def reserva(request):
    sucesso = False

    if request.method == 'GET':
      form = ReservaForm()
    else:
      form = ReservaForm(request.POST)
      if form.is_valid():
        reserva = form.save(commit=False)
        reserva.user = request.user 
        reserva.save()
        sucesso = True

    context = {
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'reserva.html', context)