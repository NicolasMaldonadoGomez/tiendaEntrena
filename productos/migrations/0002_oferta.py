# Generated by Django 4.1.3 on 2022-11-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=255)),
                ('descuento', models.FloatField()),
            ],
        ),
    ]
