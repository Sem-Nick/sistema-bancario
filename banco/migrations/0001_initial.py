# Generated by Django 5.1.2 on 2024-10-09 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_responsavel', models.TextField()),
                ('limite', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fatura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorEmprestimo', models.DecimalField(decimal_places=2, max_digits=4)),
                ('prazo', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cliente')),
            ],
        ),
    ]
