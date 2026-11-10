<<<<<<< HEAD
=======
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
>>>>>>> dfabd3f5f8ca9d6f0c492ebdc6a32b4c126b3163
from django.contrib import admin
from django.urls import path
from eventos.views import lista_eventos, detalle_evento
from compras.views import comprar_localidad, mis_compras
<<<<<<< HEAD
from clientes.views import registrar_cliente, iniciar_sesion, cerrar_sesion
=======
>>>>>>> dfabd3f5f8ca9d6f0c492ebdc6a32b4c126b3163

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_eventos, name='lista_eventos'),
    path('evento/<int:evento_id>/', detalle_evento, name='detalle_evento'),
    path('comprar/<int:localidad_id>/', comprar_localidad, name='comprar_localidad'),
    path('mis-compras/', mis_compras, name='mis_compras'),
<<<<<<< HEAD
    path('registro/', registrar_cliente, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
=======
>>>>>>> dfabd3f5f8ca9d6f0c492ebdc6a32b4c126b3163
]