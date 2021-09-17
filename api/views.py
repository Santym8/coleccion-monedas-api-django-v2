

from .models import Moneda, Coleccion
from .serializers import MonedaSerializer, ColeccionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# ---------------Colecciones---------------------------

@api_view(['GET'])
def coleccion_api_view(request):

    if(request.method == 'GET'):
        colecciones = Coleccion.objects.all()
        coleccion_serializada = ColeccionSerializer(colecciones, many=True)
        return Response(coleccion_serializada.data)


@api_view(['GET'])
def coleccion_detail_view(request, pk=None):

    colecion = Coleccion.objects.filter(id=pk).first()

    if(colecion):
        if(request.method == "GET"):
            coleccion_serializada = ColeccionSerializer(colecion)
            return Response(coleccion_serializada.data)
    else:
        return Response({'mensaje': "Coleccion no encontrada"})
    

# ----------Monedas-----------------------------


@api_view(['Get'])
def moneda_api_view(request):

    monedas = Moneda.objects.all()

    if(monedas):
        if(request.method == 'GET'):
            monedas_serializadas = MonedaSerializer(monedas, many=True)
            return Response(monedas_serializadas.data)


@api_view(['GET', 'PUT'])
def moneda_detail_view(request, pk=None):

    moneda = Moneda.objects.filter(id=pk).first()

    if(moneda):
        if(request.method == 'GET'):
            moneda_serializada = MonedaSerializer(moneda)
            return Response(moneda_serializada.data)

        elif(request.method == 'PUT'):

            moneda_serializada = MonedaSerializer(moneda, request.data)
            if(moneda_serializada.is_valid()):
                moneda_serializada.save()
                return Response(moneda_serializada.data)
            else:
                return Response(moneda_serializada.errors)
    else:
        return Response({'mensaje': 'Moneda no encontrada'})
