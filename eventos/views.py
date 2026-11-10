from django.shortcuts import render, get_object_or_404
from .models import Evento
from localidades.models import Localidad

def lista_eventos(request):
    query = request.GET.get('q', '')
    if query:
        eventos = Evento.objects.filter(nombre_evento__icontains=query)
    else:
        eventos = Evento.objects.all()
    
    return render(request, 'eventos/lista_eventos.html', {
        'eventos': eventos, 
        'query': query
    })

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Filtramos las localidades que pertenecen a este evento
    localidades = Localidad.objects.filter(evento=evento)
    
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento,
        'localidades': localidades
    })