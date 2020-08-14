from rest_framework import serializers

# Modelos
from .models import Idiomas

# Serializador de Idiomas
class IdiomasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Idiomas
		fields = ('id', 'url', 'name', 'paradigma', 'expect')