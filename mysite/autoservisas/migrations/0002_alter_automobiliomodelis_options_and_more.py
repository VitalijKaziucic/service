# Generated by Django 4.1.1 on 2022-09-19 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobiliomodelis',
            options={'verbose_name': 'Automobilio modelis', 'verbose_name_plural': 'Automobilio modeliai'},
        ),
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='paslauga',
            options={'verbose_name': 'Paslaug', 'verbose_name_plural': 'Paslaugos'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymas',
            options={'verbose_name': 'Užsakymas', 'verbose_name_plural': 'Užsakymai'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymoeilutes',
            options={'verbose_name': 'Užsakymo eilutė', 'verbose_name_plural': 'Užsakymo eilutės'},
        ),
    ]
