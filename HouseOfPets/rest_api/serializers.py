from datetime import date
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from rest_framework import serializers
from core.models import Categoria, Reserva, Petshop

class CategoriaModelSerializer(ModelSerializer):    
    # agendamentos = HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name='api:categorias-detail'
    # )
    class Meta:
        model = Categoria
        fields = [
            'id',
            'descricao',
        ]

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )
    class Meta:
        model = Petshop
        fields = '__all__'

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopModelSerializer(read_only=True)
    # categoria = CategoriaModelSerializer(read_only=True)

    def validate_data(self, value):
        hoje = date.today()
        if value < hoje:
            raise serializers.ValidationError('Não é possível fazer um agendamento com data inferior a data atual.')
        return value
    class Meta:
        model = Reserva
        fields = '__all__'