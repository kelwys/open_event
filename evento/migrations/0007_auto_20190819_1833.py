# Generated by Django 2.2.4 on 2019-08-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0006_remove_agenda_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='nome_palestra',
            field=models.CharField(max_length=50, verbose_name='Nome da Palestra'),
        ),
    ]
