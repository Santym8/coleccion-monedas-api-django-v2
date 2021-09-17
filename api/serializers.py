
from .models import Moneda, Coleccion
from rest_framework import serializers


class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = "__all__"


class ColeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coleccion
        fields =  "__all__"
