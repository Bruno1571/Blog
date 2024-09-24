TÍTULO - Blog
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

DESCRIPCIÓN
Este proyecto es una aplicación web de blog donde los usuarios pueden crear, editar y eliminar publicaciones. El sistema permite a los usuarios registrarse, iniciar sesión y gestionar sus publicaciones de manera sencilla, proporcionando una interfaz fácil de usar.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
INSTALACIÓN

  1) Clona el repositorio:
        git clone https://github.com/Bruno1571/Blog.git
    
  2) Navega al directorio donde pusiste el proyecto:
        cd nombreQueUsaste
      
  3) Crea y activa un entorno virtual:
        python -m venv entorno
        source entorno/bin/activate  # En Windows: entorno\Scripts\activate
    
  4)Luego de activar el entorno virtual, instala las dependencias del archivo requirements.txt del proyecto:
        pip install -r requirements.txt
        
  5)Aplica las migraciones de la base de datos:
      python manage.py migrate
      
  6)Ejecuta el servidor:
      python manage.py runserver
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

USO
  Accede a la aplicación en tu navegador en http://localhost:8000/.
  
  Utiliza las siguiente ruta:
    /posts/ para ver la lista de publicaciones.
  
  Luego de que ingreses se te va a pedir iniciar sesion si no tienes cuenta entra a la opcion del nav bar que es registrarse
  
  Luego de iniciar sesion vas a poder utilizar el nav bar para desplazarte libremente por las paginas
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

REQUISITOS
  Python 3.11
  Django 4.2
  SQLite
