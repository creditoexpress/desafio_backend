from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('simular-financiamento/<int:pk>', views.simularFinanciamento,
         name='simularFinanciamento'),
    path('importar/', views.importar, name='importar'),
]
