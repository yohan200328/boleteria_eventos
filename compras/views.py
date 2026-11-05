from django.shortcuts import get_object_or_404, redirect, render
from localidades.models import Localidad
from compras.models import Compra
from detalles_compra.models import DetalleCompra
from clientes.models import Cliente

def comprar_localidad(request, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)
    
    if localidad.loc_cupo_total > 0:
        # 1. Descontamos el cupo
        localidad.loc_cupo_total -= 1
        localidad.save()
        
        # 2. Obtenemos el primer cliente existente en la base de datos
        cliente_actual = Cliente.objects.first()
        
        if cliente_actual:
            # 3. Creamos la Compra principal
            compra = Compra.objects.create(
                cliente=cliente_actual,
                com_total=localidad.loc_precio,
                com_estado='Completado'
            )
            
            # 4. Creamos el Detalle de la Compra
            DetalleCompra.objects.create(
                compra=compra,
                localidad=localidad,
                det_cantidad=1,
                det_subtotal=localidad.loc_precio
            )
            
    return redirect('mis_compras')

def mis_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/mis_compras.html', {'compras': compras})

from django.shortcuts import get_object_or_404, redirect, render
from localidades.models import Localidad

def confirmar_compra(request, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)
    return render(request, 'compras/confirmar_compra.html', {'localidad': localidad})