from django.contrib import admin
from .models import Reserva
from .models import Contato
# Register your models here.

#class ReservaAdmin(admin.ModelAdmin):
#    readonly_fields = ("dreated")

@admin.register(Reserva)
class ResevaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'data', 'horario']
    search_fields = ['nome', 'data', 'categoria']
    list_filter = ['data','horario', 'categoria']


    # nome = models.CharField(max_length=100)
    # telefone = models.CharField(max_length=20)
    # data = models.DateField()
    # horario = models.CharField(max_length=5, verbose_name="Horário", choices=horario_list)
    # categoria = models.CharField(max_length=30, verbose_name="Categoria", choices=categoria_list)
    # observacao = models.TextField(blank=True)
    # isFinalizado = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']