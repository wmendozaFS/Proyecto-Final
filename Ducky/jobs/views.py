from django.shortcuts import render
from .decorators import headhunter_required # Asegúrate de la ruta correcta a tu decorador

@headhunter_required
def crear_oferta_empleo(request):
    # Lógica de la vista para crear una oferta de empleo
    return render(request, 'mi_app/crear_oferta.html')

@headhunter_required
def panel_headhunter(request):
    # Lógica para el panel de control del headhunter
    return render(request, 'mi_app/panel_headhunter.html')

def 