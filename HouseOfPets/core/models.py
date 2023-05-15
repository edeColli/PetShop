from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data = models.DateTimeField()
    horario = models.TimeField()
    observacao = models.TextField(blank=True)

