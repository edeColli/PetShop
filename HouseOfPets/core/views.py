from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

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

    if request.method == 'GET':
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
        'responsavel': 'John Doe',
        'telefone': '555-5555',
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


def signup(request):
  SIGNUP ='signup.html'

  if request.method == 'GET':
    return render(request, SIGNUP, {
      'form': UserCreationForm
    })
  else:
    if request.POST['password1'] == request.POST['password2']:
        try:
          print('objeto')
          user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
          user.save()
          login(request, user)
          return redirect('../signin')
        except:
          return render(request, SIGNUP, {
            'form': UserCreationForm,
            'error': 'E-mail já cadastrado'
          })
    return render(request, SIGNUP, {
      'form': UserCreationForm,
      'error': 'Senhas são diferentes'
    })


def signin(request):
  SIGNIN ='signin.html'

  if (request.method == 'GET'):
    return render(request, SIGNIN, {
      'form': AuthenticationForm
    })
  else:
    user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
    if user is None:
      return render(request, 'signin.html', {
          'form': AuthenticationForm,
          'error': 'Usuário ou senha inválido'
      })
    else:
      login(request, user)
      return redirect('../dashboard')

@login_required
def sair(request):
  logout(request)
  return redirect('../')

@login_required
def dashboard(request):  
  reservas = Reserva.objects.filter(isFinalizado=False)
  return render(request, 'dashboard.html', {'reservas': reservas})

@login_required
def reserva_detalhe(request, reserva_id):
  if request.method == 'GET':
    reservas = get_object_or_404(Reserva, pk=reserva_id)
    form = ReservaForm(instance=reservas)
    return render(request, 'reserva_detalhe.html', {'reservas': reservas, 'form': form})
  else:
    try:
      reservas = get_object_or_404(Reserva, pk=reserva_id)
      form = ReservaForm(instance=reservas)
      form.save
      return render(request, 'dashboard.html')
    except ValueError:
      return render(request, 'reserva_detalhe.html', {
        'reserva': reservas,
        'form': form,
        'error': 'Erro ao atualizar a reserva!'
      })
    
@login_required
def atualizar_reserva(request, reserva_id):
  reserva = get_object_or_404(Reserva, pk=reserva_id)  
  if request.method == 'POST':
    reserva.save()
    return redirect(reverse('../dashboard'))
  

@login_required
def finalizar_reserva(request, reserva_id):  
  reserva = get_object_or_404(Reserva, pk=reserva_id)
  if request.method == 'POST':
    reserva.isFinalizado = True
    reserva.save()
    return redirect(reverse('../dashboard'))

@login_required
def excluir_reserva(request, reserva_id):
  reserva = get_object_or_404(Reserva, pk=reserva_id)
  if request.method == 'POST':
    reserva.delete()
    return redirect('../dashboard')    