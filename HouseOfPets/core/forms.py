from django import forms
from datetime import date
from core.models import Contato
from core.models import Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class ReservaForm(forms.ModelForm):

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
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'placeholder':'dd/mm/yyyy','style': 'width: 15%'}),
            'horario': forms.Select(attrs={'class': 'form-control', 'style': 'width: 20%'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'style': 'display: block; width: 20%; required: true'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(ReservaForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.items():
    #         # Adiciona a classe CSS para todos os campos
    #         field.widget.attrs['class'] = 'form-control' 
    #         # Remove o sufixo padrão ':' dos rótulos
    #         field.label_suffix = ''

    def clean(self):
        cleaned_data = super().clean()
        # suas validações e manipulações aqui
        return cleaned_data
    
    def clean_data(self):
        data = self.cleaned_data.get('data')

        # Verificar se a data é mario que a data atual
        if data and data < date.today():
            #raise forms.ValidationError('Este horário já está reservado.')
            self.add_error('data', 'A data da reserva deve ser maior ou igual à data atual.')

        # Verificar se já existem mais de 10 reservas para o dia selecionado
        reservas_existentes = Reserva.objects.filter(data=data).count()
        if reservas_existentes > 10:
            raise forms.ValidationError('Já foram realizadas 10 reservas para este dia.')
        
        return data
    
    #def clean_telefone(self):
    #    telefone = self.cleaned_data.get('telefone')
    #     print(telefone)
    #    if len(telefone) < 9:
    #        self.add_error('telefone', 'O telefone informado é inválido.')
    #         if not telefone.isdigit():
    #             self.add_error('telefone', 'Este campo só aceita números.')

    def clean_horario(self):
        horario = self.cleaned_data.get('horario')
        reserva_id = self.instance.id

        # Verificar se já existe uma reserva com o mesmo horário, desde que não seja ela mesma ou um registro novo
        reservas_existentes = Reserva.objects.filter(horario=horario).exclude(id=reserva_id).exclude(id__isnull=False)

        if reservas_existentes.exists():
            #raise forms.ValidationError('Este horário já está reservado.')
            self.add_error('horario', 'Este horário já está reservado.')

        return horario
    
# class ReservaForm(forms.Form):
    # nome = forms.CharField(label='Nome', max_length=100)
    # telefone = forms.CharField(label='Telefone', max_length=100)
    # data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), label="Data da reserva")
    # horario = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}), label="Hora da reserva")
    # observacoes = forms.CharField(widget=forms.Textarea, label='Observação', max_length=500)
