<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from clientes.models import Cliente

def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        documento = request.POST.get('documento')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            return render(request, 'clientes/registro.html', {'error': 'El correo electrónico ya está registrado.'})

        # Crear el usuario de Django
        user = User.objects.create_user(username=email, email=email, password=password, first_name=nombre, last_name=apellido)
        
        # Crear el perfil de Cliente vinculado
        Cliente.objects.create(
            usuario=user,
            cli_nombre=nombre,
            cli_apellido=apellido,
            cli_documento=documento,
            cli_telefono=telefono,
            cli_correo=email
        )

        # Iniciar sesión automáticamente
        login(request, user)
        return redirect('lista_eventos')

    return render(request, 'clientes/registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_eventos')
        else:
            return render(request, 'clientes/login.html', {'error': 'Correo o contraseña incorrectos.'})

    return render(request, 'clientes/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('lista_eventos')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> dfabd3f5f8ca9d6f0c492ebdc6a32b4c126b3163
