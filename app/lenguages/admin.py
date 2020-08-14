from django.contrib import admin

# Modelos
from .models import Idiomas

# Registro de los Idiomas para Django - Admin
admin.site.register(Idiomas)
class IdiomasAdmin(admin.ModelAdmin):
    search_fields = ["name", "paradigma", "expect"]
    list_display  = ["name", "paradigma", "expect"]
