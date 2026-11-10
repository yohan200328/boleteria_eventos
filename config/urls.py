from django.contrib import admin
from django.urls import path
from eventos.views import lista_eventos, detalle_evento
from compras.views import comprar_localidad, mis_compras
from clientes.views import registrar_cliente, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_eventos, name='lista_eventos'),
    path('evento/<int:evento_id>/', detalle_evento, name='detalle_evento'),
    path('comprar/<int:localidad_id>/', comprar_localidad, name='comprar_localidad'),
    path('mis-compras/', mis_compras, name='mis_compras'),
    path('registro/', registrar_cliente, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]