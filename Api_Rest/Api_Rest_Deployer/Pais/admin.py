from django.contrib import admin

# Modelos
from .models import Pais

# Registro de los Paises para Django - Admin
admin.site.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	search_fields = ['name', 'state', 'country', 'phone', 'email']
	list_display = ['name', 'state', 'country', 'phone', 'email']
