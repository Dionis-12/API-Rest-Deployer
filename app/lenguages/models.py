from django.db import models

# Modelo de Idiomas
class Idiomas(models.Model):
	name = models.CharField(verbose_name = 'Nombre del Lenguaje', max_length = 50)
	paradigma = models.CharField(verbose_name = 'Objetivo del Lenguaje', max_length = 50)
	expect = models.CharField(verbose_name = 'Expectativas', max_length = 100)

	def __str__(self):
		return self.name