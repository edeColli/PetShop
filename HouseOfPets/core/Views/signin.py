from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


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
      return redirect('/reservas/')