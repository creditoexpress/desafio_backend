from django.urls import path
from .views import TaxaCalc


urlpatterns = [
    path('taxas/api/v1/<int:pk>/<str:str>/', TaxaCalc.as_view())
]
