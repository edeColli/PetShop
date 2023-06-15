# Generated by Django 4.2 on 2023-06-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_alter_reserva_data"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contato",
            options={
                "ordering": ["-data"],
                "verbose_name": "Formulário de contato",
                "verbose_name_plural": "Formulários de contatos",
            },
        ),
        migrations.AlterModelOptions(
            name="reserva",
            options={
                "ordering": ["-data"],
                "verbose_name": "Formulário de reserva",
                "verbose_name_plural": "Formulários de reservas",
            },
        ),
        migrations.AddField(
            model_name="contato",
            name="lido",
            field=models.BooleanField(blank=True, default=False, verbose_name="Lido"),
        ),
        migrations.AlterField(
            model_name="contato",
            name="data",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Data envio"),
        ),
        migrations.AlterField(
            model_name="contato",
            name="email",
            field=models.EmailField(max_length=100, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="contato",
            name="mensagem",
            field=models.TextField(blank=True, verbose_name="Mensagem"),
        ),
        migrations.AlterField(
            model_name="contato",
            name="nome",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="data",
            field=models.DateField(verbose_name="Data Reserva"),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="isFinalizado",
            field=models.BooleanField(
                default=False, verbose_name="Servicço Finalizado"
            ),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="nome",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="observacao",
            field=models.TextField(blank=True, verbose_name="Observação"),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="telefone",
            field=models.CharField(max_length=20, verbose_name="Telefone"),
        ),
    ]