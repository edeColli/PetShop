# Generated by Django 4.2.2 on 2023-07-11 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_reserva_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='categoria_pet',
            new_name='categoria',
        ),
    ]