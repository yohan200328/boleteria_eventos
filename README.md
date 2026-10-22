
# Sistema de Boletería de Eventos

Proyecto desarrollado en Django para la Universidad de La Guajira (Segundo Corte)[cite: 5].

## 👥 Integrantes del Grupo
- **Yohan Fabian Mejia Ruiz** - `@yohan200328` (Líder)[cite: 10]
- **David Araujo** - `@davidaraujo-web`[cite: 10]

## 📋 Descripción del Proyecto
Sistema web desarrollado en Python con el framework Django para la gestión y venta de boletería de eventos, administrando lugares, eventos, localidades, clientes, compras y detalles de compra[cite: 5, 10].

## 📂 Documentación y Diagramas
Los diagramas solicitados se encuentran ubicados en la carpeta `docs/` del repositorio[cite: 2, 3, 5]:
- **Diagrama de Actores / Casos de Uso (Entregable 1):** `docs/diagrama_actores.png`[cite: 2, 5]
- **Diagrama Entidad-Relación (Entregable 2):** `docs/diagrama_er.png`[cite: 3, 5]

## 🔑 Credenciales del Superusuario (Admin)
Para acceder al panel de administración de Django (`/admin/`), utilice las siguientes credenciales[cite: 5]:
- **URL:** `http://127.0.0.1:8000/admin/`[cite: 10]
- **Usuario:** `yohan`[cite: 10]
- **Contraseña:** `yohan1123400577`[cite: 10]

## ⚙️ Requisitos e Instalación Local (Para el Profesor)
1. Clonar el repositorio[cite: 5, 10].
2. Crear y activar el entorno virtual (`python -m venv venv`)[cite: 5, 10].
3. Instalar dependencias: `pip install -r requirements.txt`[cite: 5, 10].
4. Ejecutar migraciones y servidor local[cite: 5, 10]:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
