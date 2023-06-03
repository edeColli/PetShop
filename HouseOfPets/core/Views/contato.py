from django.shortcuts import render
from core.forms import ContatoForm

def contato(request):
    sucesso = False

    if request.method == 'GET':
      form = ContatoForm()
    else:
      print(request)
      form = ContatoForm(request.POST)
      if form.is_valid():
        sucesso = True
        form.save()

    context = {
        'responsavel': 'John Doe',
        'telefone': '555-5555',
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'contato.html', context)