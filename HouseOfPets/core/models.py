from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

class Reserva(models.Model):
    categoria_list = (
        ("Gato", "Gato"), 
        ("Cachorro", "Cachorro")
    )

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data = models.DateTimeField()
    horario = models.TimeField()
    categoria = models.CharField(max_length=30, verbose_name="Categoria", choices=categoria_list)
    observacao = models.TextField(blank=True)
    isFinalizado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username