# Generated by Django 4.0.6 on 2022-07-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
