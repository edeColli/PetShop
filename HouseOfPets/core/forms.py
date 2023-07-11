from django import forms
from datetime import date
from core.models import Contato, Reserva, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descricao']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['nome', 'email', 'telefone', 'nome_pet', 'data', 'horario', 'categoria_pet', 'tamanho', 'observacao']
        labels = {
            'nome_pet': 'Nome do Pet',
            'categoria_pet': 'Categoria',
            'data': 'Data da reserva',
            'horario': 'Hora da reserva',
            'observacao': 'Observações'
        }
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'placeholder':'dd/mm/yyyy','style': 'width: 15%'}),
            'horario': forms.Select(attrs={'class': 'form-control', 'style': 'width: 20%'}),
            'categoria_pet': forms.Select(attrs={'class': 'form-control', 'style': 'display: block; width: 20%; required: true'}),
            'tamanho': forms.Select(attrs={'class': 'form-control', 'style': 'display: block; width: 20%; required: true'})
        }
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
