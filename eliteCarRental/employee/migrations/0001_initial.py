# Generated by Django 3.2.4 on 2022-02-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=150)),
                ('phoneno', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleType', models.CharField(max_length=100)),
                ('available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rentalBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=150)),
                ('rentalDate', models.DateField(auto_now=True)),
                ('returnDate', models.DateField(blank=True, null=True)),
                ('vehicleType', models.CharField(max_length=150)),
            ],
        ),
    ]
