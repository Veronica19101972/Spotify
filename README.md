# TRABAJO FINAL DE PYTHON

En la Tercera Entrega PYTHON

Esto es un proyecto web Django con patrón MVT que incluya herencia de HTML, clases en el modelo y formularios para insertar datos.

Aquí están los pasos generales para crear el proyecto:

1. Configuración inicial:
   - Instala Python en tu sistema si no lo tienes instalado.
   - Instala Django usando el administrador de paquetes pip.
   - Crea un nuevo proyecto Django usando el comando `django-admin startproject project`.

2. Define el modelo:
   - Abre el archivo `models.py` en la carpeta del proyecto y define tus clases de modelo.
   - Asegúrate de utilizar la herencia de modelos si deseas implementar herencia en tus clases.

3. Crea las vistas:
   - Abre el archivo `views.py` en la carpeta de la aplicación y define las vistas para manejar las solicitudes del usuario.
   - Las vistas pueden renderizar plantillas HTML, procesar formularios y realizar operaciones en el modelo.

4. Configura las URL:
   - Crea un archivo `urls.py` en la carpeta de la aplicación y define las URL que corresponden a cada vista.
   - Configura las URL del proyecto principal para incluir las URL de la aplicación.

5. Crea las plantillas HTML:
   - Crea una carpeta llamada `templates` en la carpeta de la aplicación.
   - Crea plantillas HTML para cada vista y utiliza la herencia de plantillas para evitar la duplicación de código HTML.

6. Define los formularios:
   - Crea un archivo `forms.py` en la carpeta de la aplicación y define los formularios para insertar datos en el modelo.
   - Utiliza las clases de formulario proporcionadas por Django para facilitar la validación y el procesamiento de los datos del formulario.

7. Ejecuta el servidor de desarrollo:
   - Abre una terminal, navega hasta la carpeta del proyecto y ejecuta el comando `python manage.py runserver`.
   - Accede al servidor de desarrollo en tu navegador para probar y verificar las funcionalidades.

Se ha creado las aplicaciones HOME, ALBUM, ARTISTA, CUENTA en estas tres ultimas se generaron las clases CREAR, LEER, ACTUALIZAR Y BORRAR es decir CRUD.

Se ha generado cuatro tipos de niveles de usuario que son los siguientes:
   1 - El usuario no registrado.
   2 - El registrado y que no pertenece al staff.
   3 - El registrado y que si pertenece al staff.
   4 - Y el ADMIN
