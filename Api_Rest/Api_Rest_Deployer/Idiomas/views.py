from django.shortcuts import render

# Vista
from rest_framework import viewsets

# Modelo
from .models import Idiomas

# Serializador
from .serializers import IdiomasSerializer

# Vista de Idiomas
class IdiomasView(viewsets.ModelViewSet):
	queryset = Idiomas.objects.all()
	serializer_class = IdiomasSerializer