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


## Solución de problemas comunes

### Error al conectar a la base de datos:

* Verifica que los datos de conexión (host, usuario, contraseña, base de datos) sean correctos.
* Asegúrate de que el servicio de MySQL Workbench esté en ejecución.


* ## Error al instalar las dependencias:

* Comprueba que tengas instalada la versión correcta de Python (3.11).
* Verifica que el entorno virtual esté activado correctamente.



### Si tienes algún otro problema o necesitas asistencia, no dudes en comunicarte con nuestro equipo de soporte técnico a través del siguiente correo electrónico: soporte@reservashotel.com
### ¡Disfruta de tu experiencia con el sistema de reservas de hotel!