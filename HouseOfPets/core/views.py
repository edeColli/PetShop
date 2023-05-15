from django.shortcuts import render
from core.forms import ContatoForm
from core.forms import ReservaForm
from .models import Reserva
from .models import Contato

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')
    
def contato(request):
    #{%csrf_token%} é um template para não deixar qualquer injetar codigo no seu 
    # dentro do arquivo HTML:
    # {{ Server para localizar a variavel que foi passada no context}} 
    # | serve para utilizar o filtro, por exemplo {{ nome|upper }} -> transforma o nome em maiúsculo
    sucesso = False
    print(sucesso);

    if request.method == 'GET':
      print("iniciando formulario")      
      form = ContatoForm()
    else:
      print(request)        
      form = ContatoForm(request.POST)
      if form.is_valid():
        sucesso = True
        # contato = Contato(
        #   nome=form.cleaned_data['nome'],
        #   email=form.cleaned_data['email'],
        #   mensagem=form.cleaned_data['mensagem']
        # )
        # contato.save()
        form.save()
    
    context = {
        'formulario': form,
        'sucesso': sucesso
    }
    
    return render(request, 'contato.html', context)

def reserva(request):
    sucesso = False

    if request.method == 'GET':      
      form = ReservaForm()
    else:
      form = ReservaForm(request.POST)
      if form.is_valid():
        # schedule = Reserva(
        #   nome=form.cleaned_data['nome'],
        #   telefone=form.cleaned_data['telefone'],
        #   data=form.cleaned_data['data'],
        #   horario=form.cleaned_data['horario'],
        #   observacao=form.cleaned_data['observacoes']
        # )
        # schedule.save()
        form.save()
        sucesso = True

    
    context = {
        'formulario': form,
        'sucesso': sucesso
    }
    
    return render(request, 'reserva.html', context)


def sobre(request):
    return render(request, 'about.html')