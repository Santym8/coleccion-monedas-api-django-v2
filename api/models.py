from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


# Create your models here.

class Coleccion(models.Model):

    nombre = models.CharField('Nombre Coleccion',max_length=50)
    cantidadMonedas = models.IntegerField('Cantidad Monedas Coleccion')

    class Meta:
        verbose_name = "Coleccion"
        verbose_name_plural = "Colecciones"

    def __str__(self):
        return self.nombre


class Moneda(models.Model):

    id = models.AutoField("Id",primary_key=True)


    coleccion = models.ForeignKey(Coleccion, on_delete=CASCADE)

    monedaNumero = models.IntegerField('# Moneda en la coleccion',null=False, blank=False)
    nombre = CharField('Nombre',max_length=100)
    agno = models.IntegerField('Año',null=False, blank=False)
    imagen = models.CharField('URL Imagen', max_length=300,null=False, blank=False)
    encontrada = models.BooleanField('Encontrada',default=False)

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"

    def __str__(self):
        return f'{self.agno}--{self.nombre}'
