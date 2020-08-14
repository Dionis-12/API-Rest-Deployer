from rest_framework import routers
from apps.lenguages.views import IdiomasView
from apps.country.views import PaisView

# Se crea el Router Predeterminado
router = routers.DefaultRouter()

# URL de Idiomas
router.register('lenguages', IdiomasView)

# URL de Pais
router.register('country', PaisView)