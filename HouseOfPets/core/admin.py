from django.contrib import admin
from .models import Reserva
from .models import Contato
from .models import Categoria
from django.contrib import messages

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


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    list_filter = ['descricao']