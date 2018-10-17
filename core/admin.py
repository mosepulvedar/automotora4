from django.contrib import admin

from .models import Automovil, Marca

# Register your models here.
#clase de configuracion para
#el automovil en el admin de django
class AutomovilAdmin(admin.ModelAdmin):
    #declaramos una tupla
    list_display = ('patente', 'marca', 'modelo', 'anio')
    search_fields = ['patente', 'modelo']
    #agregaremos un filtro personalizado en el admin
    list_filter = ('marca',)

admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)
