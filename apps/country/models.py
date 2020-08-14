from django.db import models

# Modelo de Pais
class Pais(models.Model):
	name = models.CharField(verbose_name = 'Nombre de tú Pais', max_length = 50)
	state = models.CharField(verbose_name = 'Nombre del Estado', max_length = 50)
	country = models.CharField(verbose_name = 'Capital', max_length = 50)
	phone = models.CharField(verbose_name = 'Número de Tlf.', max_length = 15)
	email = models.EmailField(verbose_name = 'Correo', max_length = 50)

	def __str__(self):
		return self.name