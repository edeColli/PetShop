from django.shortcuts import render
from core.forms import CategoriaForm
from django.contrib.auth.decorators import login_required

@login_required
def categoria(request):
    sucesso = False

    if request.method == 'GET':
      form = CategoriaForm()
    else:
      print(request)
      form = CategoriaForm(request.POST)
      if form.is_valid():
        sucesso = True
        form.save()

    context = {
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'categoria.html', context)