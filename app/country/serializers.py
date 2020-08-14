from rest_framework import serializers

# Modelos
from .models import Pais

# Serializador de Pais
class PaisSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pais
		fields = ('id', 'url', 'name', 'state', 'country', 'phone', 'email')