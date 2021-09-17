# Generated by Django 3.2.7 on 2021-09-14 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Coleccion')),
                ('cantidadMonedas', models.IntegerField(verbose_name='Cantidad Monedas Coleccion')),
            ],
            options={
                'verbose_name': 'Coleccion',
                'verbose_name_plural': 'Colecciones',
            },
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('agno', models.IntegerField(verbose_name='Año')),
                ('imagen', models.URLField(verbose_name='URL Imagen')),
                ('encontrada', models.BooleanField(default=False, verbose_name='Encontrada')),
                ('coleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coleccion')),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
            },
        ),
    ]