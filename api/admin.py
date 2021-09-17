from django.contrib import admin
from .models import Moneda, Coleccion

from import_export import resources
from import_export.admin import ImportExportModelAdmin


#-----------------------------------------------------

class MonedaResource(resources.ModelResource):
    class Meta:
        model = Moneda


#-----------------------------------------------------
class MonedaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id', 'monedaNumero','coleccion','nombre', 'agno', 'encontrada']
    search_fields = ['nombre','coleccion', 'agno','encontrada']


class ColeccionAdmin(admin.ModelAdmin):
    display = ['id','nombre', 'cantidadMonedas']


admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Coleccion, ColeccionAdmin)