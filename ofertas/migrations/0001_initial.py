# Generated by Django 4.1.3 on 2022-11-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=50)),
                ('descuento', models.FloatField(null=True)),
            ],
        ),
    ]