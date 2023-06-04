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

