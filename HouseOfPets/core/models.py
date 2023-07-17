from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    mensagem = models.TextField(verbose_name='Mensagem', blank=True)
    data = models.DateTimeField(verbose_name='Data envio', auto_now_add=True)
    lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)
    
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['-data']

class Reserva(models.Model):

    TAMANHO_LIST = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande'),
    )

    HORARIO_LIST = (
        ('07:00', '07:00'),
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
    )

    nome = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='Email')
    nome_pet = models.CharField(verbose_name='Nome do pet',max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=20)
    data = models.DateField(verbose_name='Data Reserva')
    horario = models.CharField(max_length=5, verbose_name="Horário", choices=HORARIO_LIST)    
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_LIST)
    observacao = models.TextField(verbose_name='Observação', blank=True)
    isFinalizado = models.BooleanField(verbose_name='Serviço Finalizado', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(
        'Categoria', 
        related_name='agendamentos', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    petshop = models.ForeignKey(
        'Petshop', 
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.nome} [{self.data}] [{self.horario}]'

    class Meta:
        verbose_name = 'Reserva de banho'
        verbose_name_plural = 'Reservas de banho'
        ordering = ['-data']


class Petshop(models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Rua', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)

    def __str__(self):
        return self.nome
    
    def quantidade_reservas(self):
        return self.reservas.count()

class Categoria(models.Model):
    descricao = models.CharField(verbose_name='Nome da categoria', max_length=50)

    def __str__(self):
        return self.descricao