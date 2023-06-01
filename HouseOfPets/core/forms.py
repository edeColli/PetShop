from django import forms
from core.models import Contato
from core.models import Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class ReservaForm(forms.ModelForm):
    class Meta:
        OPCOES = [
            ('-', 'Selecione uma opção'),
            ('cat', 'GATO'), 
            ('dog', 'CACHORRO'),
            ('bird', 'AVE')
        ]
        model = Reserva
        fields = ['nome', 'telefone', 'data', 'horario', 'categoria', 'observacao']
        labels = {
            'nome': 'Nome do Pet',
            'data': 'Data da reserva',
            'horario': 'Hora da reserva', 
            'observacao': 'Observações'
        }
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'format': '%d/%m/%Y'}),
            'horario': forms.DateInput(attrs={'type': 'time'}),
            'categoria': forms.Select(choices=OPCOES, attrs={'style': 'display: block; width: 100%;'})
        }
# class ReservaForm(forms.Form):
    # nome = forms.CharField(label='Nome', max_length=100)
    # telefone = forms.CharField(label='Telefone', max_length=100)
    # data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), label="Data da reserva")
    # horario = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}), label="Hora da reserva")
    # observacoes = forms.CharField(widget=forms.Textarea, label='Observação', max_length=500)
