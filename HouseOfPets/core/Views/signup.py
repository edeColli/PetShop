from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
  SIGNUP ='signup.html'

  if request.method == 'GET':
    return render(request, SIGNUP, {
      'form': UserCreationForm
    })
  else:
    print(request.POST)
    if 'password1' in request.POST and 'password2' in request.POST:
      pass1 = request.POST['password1']
      pass2 = request.POST['password2']
      if pass1.strip() and pass2.strip() and pass1 == pass2:
        try:
          user = User.objects.create_user(
            username=request.POST['username'], 
            password=request.POST['password1'])
          
          user.first_name=request.POST['first_name']
          user.last_name=request.POST['last_name']
          user.email=request.POST['email']
          user.save()
          login(request, user)
          return redirect('/reserva/')
        except:
          return render(request, SIGNUP, {
            'form': UserCreationForm,
            'error': 'usuário e/ou e-mail já cadastrado'
          })
      else:
        return render(request, SIGNUP, {
          'form': UserCreationForm(),
          'error': 'As senhas informadas são inválidas'
        })
    return render(request, SIGNUP, {
      'form': UserCreationForm,
      'error': 'As senhas não foram informadas'
    })

