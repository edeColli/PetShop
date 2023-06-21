from django.core.management.base import BaseCommand
from model_bakery import baker
from core.models import Reserva

class Command(BaseCommand):
    help = 'Cria dados fake para testar a API'

    def handle(self, *args, **options):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'Criando {total} agendamentos')
        )
        for i in range(total):
            reserva = baker.make(Reserva)
            reserva.save()
        self.stdout.write(
            self.style.SUCCESS('Agendamentos criaddos')
        )

