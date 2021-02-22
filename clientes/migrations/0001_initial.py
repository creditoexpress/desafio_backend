# Generated by Django 3.0.5 on 2021-02-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('celular', models.CharField(max_length=11)),
                ('score', models.CharField(max_length=3)),
                ('negativado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
