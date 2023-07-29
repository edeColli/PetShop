import random
from django.core.management.base import BaseCommand
from core.models import Petshop

class Command(BaseCommand):
    def getPetshops(self):
        return Petshop.objects.values_list('pk', flat='True')

    def escolher_reservas(self, reservas, quantidade):
        banhos = list(reservas)
        if quantidade > len(banhos):
            quantidade = len(banhos)

        return random.sample(banhos, quantidade)
    
    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write()
        self.stdout.write(
            self.style.NOTICE('Dados das pessoas e animais sorteados')
        )
        self.stdout.write('='*35)
        for reserva in reservas:
            self.stdout.write(f'Pet: {reserva.nome_pet}')
            self.stdout.write(f'Tutor: {reserva.nome} = {reserva.email}')
        self.stdout.write('='*35)

    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO('Dados do petshop que fez o sorteio')
        )
        self.stdout.write(
            f'Petshop -> {petshop.nome}'
        )

    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas vão participar do sorteio'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.getPetshops(),
            help='Código de identificação do Petshop'
        )

    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']

        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()

        banhos_escolhidos = self.escolher_reservas(reservas, quantity)
        

        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos)

        self.stdout.write(
            self.style.SUCCESS('Sorteio Concluido')
        )