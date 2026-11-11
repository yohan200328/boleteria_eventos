from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from localidades.models import Localidad
from compras.models import Compra
from detalles_compra.models import DetalleCompra

@login_required(login_url='login')
def comprar_localidad(request, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)
    
    try:
        cliente_actual = request.user.cliente_perfil
    except Exception:
        return redirect('registro')

    if request.method == 'POST':
        if localidad.loc_cupo_total > 0:
            localidad.loc_cupo_total -= 1
            localidad.save()

            # Creamos la compra asegurando el estado 'Completado'
            compra = Compra.objects.create(
                cliente=cliente_actual,
                com_total=localidad.loc_precio,
                com_estado='Completado',
            )

            DetalleCompra.objects.create(
                compra=compra,
                localidad=localidad,
                det_cantidad=1,
                det_subtotal=localidad.loc_precio
            )

            return redirect('mis_compras')

    return render(request, 'compras/confirmar_compra.html', {'localidad': localidad})

@login_required(login_url='login')
def mis_compras(request):
    try:
        cliente_actual = request.user.cliente_perfil
        compras = Compra.objects.filter(cliente=cliente_actual)
    except Exception:
        compras = []
    
    return render(request, 'compras/mis_compras.html', {'compras': compras})