from rest_framework import routers
from .api import MenuViewSet
from . import views

router = routers.DefaultRouter()
router.register('menu', MenuViewSet, 'menu')


urlpatterns = router.urls