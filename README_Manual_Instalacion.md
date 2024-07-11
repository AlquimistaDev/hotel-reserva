# Manual de Instalación
## Sistema de Reservas de Hotel
** Requisitos del sistema
** Hardware

* Procesador: Intel Core i5 o equivalente (mínimo)
* Memoria RAM: 8 GB (mínimo)
* Espacio en disco: 500 MB (mínimo)

### Software

* Sistema Operativo: Windows 10/11, macOS 10.15 o superior, o distribución de Linux compatible con Python 3.11
* Python 3.11
* MySQL Workbench 8.0 o superior

### Pasos de instalación

1. Clonar el repositorio del proyecto:

* Abre una terminal o símbolo del sistema.
* Ejecuta el siguiente comando para - clonar el repositorio:
Copygit clone https://github.com/AlquimistaDev/hotel-reserva/tree/solucionMenuReserva

* Navega hacia la carpeta del proyecto clonado:
- cd reservas-hotel



2. Crear y activar un entorno virtual de Python:

* Crea un entorno virtual de Python ejecutando el siguiente comando:
- python -m venv env

* Activa el entorno virtual:

* En Windows: env\Scripts\activate
* En macOS/Linux: source env/bin/activate




3. Instalar las dependencias del proyecto:

* Con el entorno virtual activado, instala las dependencias del proyecto utilizando el archivo requirements.txt:
- pip install -r requirements.txt




# Configuración de la base de datos

1. Crear la base de datos MySQL:

* Abre MySQL Workbench.
* Ejecuta el script SQL sql_MySql.sql que se encuentra en la carpeta del proyecto para crear la base de datos y las tablas necesarias.


2. Configurar los datos de conexión:

* Abre el archivo DatabaseSingleton.py en tu editor de código.
* Actualiza los siguientes parámetros de conexión con los valores correspondientes a tu entorno:
```
self.connection = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="hotel_mpc"
)
```



# Ejecución de la aplicación

1. Asegúrate de tener el entorno virtual activado.
2. Ejecuta el archivo main.py para iniciar el sistema de reservas de hotel:
- python main.py

## Creacion de instalador
- en un terminal cmd instalaremos la extencion (pyinstaller)
1. una vez abierto el terminal cmd se escribira el comando (pip install pyinstaller)
* en caso de  que el proceso de instalacion de pyinstaller arroje un error se debe actualizar la exxtencion (pip)
## comando para actualizar
- python.exe -m pip install --upgrade pip
* en caso de haber actualizado el pip se debe terminar de implementar pyinstaller ejecutando nuevamente el comando.

## configurar PATH
1. abre la lupa de windows y buscamos ( editar las variables de entorno del sistema).
2. se abrira una venta que dice Propiedades de sistema
- en la pestaña opciones avanzadas, buscaremos (variables de entorno)
- se abrira una pestala llamada (varables de entorno) y dentro buscaremos la lista (variables de sistema).
- dentro de esta lista buscaremos la variable (Path).
- selecionar el Path y presionamos el boton editar.
- se abrira una pestaña llamada (editar variables de entorno).
- dentro tenemos que seleccionar un boton (nuevo) y pegaremos la ruta donde tengamos instalado los script de python
- presiona aceptar todo, y cerramos las ventanas que estan abiertas.


## Creacion Main.exe
1. abre visual estudio code
2. abrimos terminal
3. dentro del terminal nos dirigiremos a la ruta donde tengamos nuestro archivo main.py
4. una vez dentro de la ruta ejecutaremos el comando (pyinstaller main.py)
5. una vez realizado el comando en nuestra ruta nos creara 3 archivos (build, dist, main.spec)
6. dentro de la carpeta dist se creara una carpeta main donde esta alojado nuestro ejecutable .exe


## Solución de problemas comunes

### Error al conectar a la base de datos:

* Verifica que los datos de conexión (host, usuario, contraseña, base de datos) sean correctos.
* Asegúrate de que el servicio de MySQL Workbench esté en ejecución.


* ## Error al instalar las dependencias:

* Comprueba que tengas instalada la versión correcta de Python (3.11).
* Verifica que el entorno virtual esté activado correctamente.



### Si tienes algún otro problema o necesitas asistencia, no dudes en comunicarte con nuestro equipo de soporte técnico a través del siguiente correo electrónico: soporte@reservashotel.com
### ¡Disfruta de tu experiencia con el sistema de reservas de hotel!