from django.urls import path
from .views import coleccion_api_view, coleccion_detail_view, moneda_api_view, moneda_detail_view

urlpatterns = [
    path('colecciones/', coleccion_api_view, name="colecciones"), 
    path('coleccion/<int:pk>', coleccion_detail_view, name="coleccion"),

    path('monedas/', moneda_api_view, name='monedas'),
    path('moneda/<int:pk>', moneda_detail_view, name='moneda')
    
    
]
