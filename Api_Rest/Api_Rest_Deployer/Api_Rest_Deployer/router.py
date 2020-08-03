from rest_framework import routers
from Idiomas.views import IdiomasView
from Pais.views import PaisView

# Se crea el Router Predeterminado
router = routers.DefaultRouter()

# URL de Idiomas
router.register('Idiomas', IdiomasView)

# URL de Pais
router.register('Pais', PaisView)