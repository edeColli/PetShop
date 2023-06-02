from django import forms
from datetime import date
from core.models import Contato
from core.models import Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class ReservaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'text', 'class': 'datepicker', 'style': 'width: 15%', 'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%Y']
    )
    class Meta:
        model = Reserva
        fields = ['nome', 'telefone', 'data', 'horario', 'categoria', 'observacao']
        labels = {
            'nome': 'Nome do Pet',
            'data': 'Data da reserva',
            'horario': 'Hora da reserva', 
            'observacao': 'Observações'
        }
        widgets = {
            #'data': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'style': 'width: 15%'}),
            'horario': forms.DateInput(attrs={'type': 'time', 'style': 'width: 15%'}),
            'categoria': forms.Select(attrs={'style': 'display: block; width: 100%; required: true'})
        }

    def clean(self):
        cleaned_data = super().clean()
        horario = cleaned_data.get('horario')
        data = cleaned_data.get('data')

        # Verificar se a data é mario que a data atual
        if data and data < date.today():
            #raise forms.ValidationError('Este horário já está reservado.')
            self.add_error('data', 'A data da reserva deve ser maior ou igual à data atual.')

        # Verificar se já existe uma reserva com o mesmo horário
        reservas_existentes = Reserva.objects.filter(horario=horario)
        if reservas_existentes.exists():
            #raise forms.ValidationError('Este horário já está reservado.')
            self.add_error('horario', 'Este horário já está reservado.')

        # Verificar se já existem mais de 10 reservas para o dia selecionado
        reservas_existentes = Reserva.objects.filter(data=data).count()
        self.add_error('data', 'total: '+ str(reservas_existentes))
        if reservas_existentes >= 10:
            raise forms.ValidationError('Já foram realizadas 10 reservas para este dia.')
        
        return cleaned_data
    
# class ReservaForm(forms.Form):
    # nome = forms.CharField(label='Nome', max_length=100)
    # telefone = forms.CharField(label='Telefone', max_length=100)
    # data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), label="Data da reserva")
    # horario = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}), label="Hora da reserva")
    # observacoes = forms.CharField(widget=forms.Textarea, label='Observação', max_length=500)
