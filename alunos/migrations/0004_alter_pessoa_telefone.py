# Generated by Django 4.2.18 on 2025-02-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]
