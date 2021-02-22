from rest_framework import routers
from django.urls import path, include
from .views import ClientesViewSet

router = routers.DefaultRouter()
router.register('clientes/api/v1', ClientesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
