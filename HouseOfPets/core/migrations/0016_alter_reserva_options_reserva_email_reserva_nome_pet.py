# Generated by Django 4.2 on 2023-06-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_reserva_tamanho_alter_reserva_isfinalizado"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reserva",
            options={
                "ordering": ["-data"],
                "verbose_name": "Reserva de banho",
                "verbose_name_plural": "Reservas de banho",
            },
        ),
        migrations.AddField(
            model_name="reserva",
            name="email",
            field=models.EmailField(
                default="Maria", max_length=254, verbose_name="Email"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reserva",
            name="nome_pet",
            field=models.CharField(
                default="Maria", max_length=50, verbose_name="Nome do pet"
            ),
            preserve_default=False,
        ),
    ]