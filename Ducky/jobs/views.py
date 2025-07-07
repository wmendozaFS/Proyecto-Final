from .decorators import headhunter_required # Asegúrate de la ruta correcta a tu decorador
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JobOfferForm

# @headhunter_required
def panel_headhunter(request):
    return render(request, 'jobs/crear_oferta.html', {
    'mensaje': 'Bienvenido al panel del headhunter'
})

# @headhunter_required
def crear_oferta(request):
    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.created_by = request.user  # usuario logueado
            oferta.save()
            messages.success(request, 'Oferta creada exitosamente.')
            return redirect('panel_headhunter')
    else:
        form = JobOfferForm()

    return render(request, 'headhunter/crear_oferta.html', {
        'form': form
    })