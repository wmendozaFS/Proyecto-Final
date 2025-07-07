
from django.urls import path
from .views import crear_oferta, panel_headhunter

urlpatterns = [
    path('panel/headhunter/', panel_headhunter, name='panel_headhunter'),
    path('panel/headhunter/crear_oferta/', crear_oferta, name='crear_oferta'),
]