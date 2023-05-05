# Generated by Django 4.2 on 2023-04-27 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('placa', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='Carro')),
                ('marca', models.CharField(max_length=150, verbose_name='Marca')),
                ('ano', models.CharField(max_length=7, verbose_name='Ano')),
                ('modelo', models.CharField(max_length=150, verbose_name='Modelo')),
                ('data_compra', models.DateField(verbose_name='Data de Compra')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='CPF')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Codigo')),
                ('data_alugel', models.DateField()),
                ('data_entrega', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('devolucao', models.BooleanField(verbose_name='Devolvido')),
                ('diaria', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Diaria')),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_alugueis', to='aluguel.cliente')),
                ('placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluguel.carro', verbose_name='Carro')),
            ],
        ),
    ]