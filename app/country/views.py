from django.shortcuts import render

# Vista
from rest_framework import viewsets

# Modelo
from .models import Pais

# Serializador
from .serializers import PaisSerializer

# Vista de Pais
class PaisView(viewsets.ModelViewSet):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer
