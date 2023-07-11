from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from core.models import Categoria, Reserva, Petshop

class CategoriaModelSerializer(ModelSerializer):    
    class Meta:
        model = Categoria
        fields = '__all__'

class PetshopModelSerializer(ModelSerializer):
    # reservas = HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name='api:reserva-detail'
    # )
    class Meta:
        model = Petshop
        fields = '__all__'

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopModelSerializer(read_only=True)
    categoria = CategoriaModelSerializer(read_only=True)
    class Meta:
        model = Reserva
        fields = '__all__'    