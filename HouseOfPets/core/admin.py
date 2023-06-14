from django.contrib import admin
from .models import Reserva
from .models import Contato
from django.contrib import messages
# Register your models here.

#class ReservaAdmin(admin.ModelAdmin):
#    readonly_fields = ("dreated")
@admin.action(description='Marcar Reserva como finalizada')
def marcar_como_finalizada(modeladmin, request, queryset):
    queryset.update(isFinalizado=True)
    modeladmin.message_user(request, 'Reserva foi finalizada', messages.SUCCESS)


@admin.register(Reserva)
class ResevaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'nome_pet','data', 'horario', 'isFinalizado']
    search_fields = ['nome', 'data', 'nome_pet', 'categoria', 'tamanho']
    list_filter = ['data','horario', 'categoria', 'tamanho', 'isFinalizado']
    actions = [marcar_como_finalizada]


    # nome = models.CharField(max_length=100)
    # telefone = models.CharField(max_length=20)
    # data = models.DateField()
    # horario = models.CharField(max_length=5, verbose_name="Horário", choices=horario_list)
    # categoria = models.CharField(max_length=30, verbose_name="Categoria", choices=categoria_list)
    # observacao = models.TextField(blank=True)
    # isFinalizado = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
@admin.action(description='Marcar formulário de contato como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulário de contato marcado como lido', messages.SUCCESS)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data', 'lido']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido]
