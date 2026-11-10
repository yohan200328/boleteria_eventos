from django.shortcuts import get_object_or_404, redirect, render
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from localidades.models import Localidad
from compras.models import Compra
from detalles_compra.models import DetalleCompra

# Cambiamos login_url a la vista de registro o login pública
@login_required(login_url='registro')
def comprar_localidad(request, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)
    
    try:
        cliente_actual = request.user.cliente_perfil
    except Exception:
        # Si el usuario logueado (como el admin) no tiene perfil de cliente,
        # lo mandamos a registrarse/completar datos en lugar del admin
        return redirect('registro')

    if request.method == 'POST':
        if localidad.loc_cupo_total > 0:
            localidad.loc_cupo_total -= 1
            localidad.save()

            compra = Compra.objects.create(
                cliente=cliente_actual,
                com_total=localidad.loc_precio,
                com_estado='Completado',
            )

=======
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
>>>>>>> dfabd3f5f8ca9d6f0c492ebdc6a32b4c126b3163
            DetalleCompra.objects.create(
                compra=compra,
                localidad=localidad,
                det_cantidad=1,
                det_subtotal=localidad.loc_precio
            )
<<<<<<< HEAD

            return redirect('mis_compras')

    return render(request, 'compras/confirmar_compra.html', {'localidad': localidad})


@login_required(login_url='registro')
def mis_compras(request):
    try:
        cliente_actual = request.user.cliente_perfil
        compras = Compra.objects.filter(cliente=cliente_actual)
    except Exception:
        compras = []
    
    return render(request, 'compras/mis_compras.html', {'compras': compras})
=======
            
    return redirect('mis_compras')

def mis_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/mis_compras.html', {'compras': compras})

from django.shortcuts import get_object_or_404, redirect, render
from localidades.models import Localidad

def confirmar_compra(request, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)
    return render(request, 'compras/confirmar_compra.html', {'localidad': localidad})
>>>>>>> dfabd3f5f8ca9d6f0c492ebdc6a32b4c126b3163
