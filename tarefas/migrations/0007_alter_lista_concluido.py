# Generated by Django 4.2.1 on 2023-05-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0006_alter_lista_concluido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]
