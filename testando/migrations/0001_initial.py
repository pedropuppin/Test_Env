# Generated by Django 4.2.5 on 2023-09-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoLente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('status', models.CharField(choices=[('Aguardando início', 'Aguardando início'), ('Aguardando aprovacao', 'Aguardando aprovacao'), ('Aprovado. Aguardando Setups', 'Aprovado. Aguardando Setups'), ('Aguardando produção e envio', 'Aguardando produção e envio'), ('Em produção', 'Em produção'), ('Aguardando envio', 'Aguardando envio'), ('Arquivado', 'Arquivado')], default='Aguardando início', max_length=100, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Lente',
                'verbose_name_plural': 'Lentes',
            },
        ),
        migrations.CreateModel(
            name='PedidoPlaca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('status', models.CharField(choices=[('Aguardando início', 'Aguardando início'), ('Aguardando aprovacao', 'Aguardando aprovacao'), ('Aprovado. Aguardando Setups', 'Aprovado. Aguardando Setups'), ('Aguardando produção e envio', 'Aguardando produção e envio'), ('Em produção', 'Em produção'), ('Aguardando envio', 'Aguardando envio'), ('Arquivado', 'Arquivado')], default='Aguardando início', max_length=100, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Placa',
                'verbose_name_plural': 'Placas',
            },
        ),
    ]
