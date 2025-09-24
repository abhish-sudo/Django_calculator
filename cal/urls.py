from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
    path('api/calculate/', views.calculate_api, name='calculate_api'),
    path('api/history/', views.history_api, name='history_api'),
]
