# Generated by Django 4.2.7 on 2023-11-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('postal', models.BigIntegerField()),
                ('state', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=150)),
                ('mc_number', models.BigIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
