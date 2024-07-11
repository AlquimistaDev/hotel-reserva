
# 1. Descripción general del proyecto:

## Sistema de Reservas de Hotel

- Este proyecto es un sistema de gestión de reservas de hotel. Permite a los usuarios realizar las siguientes funcionalidades principales:                   

- Gestionar usuarios (crear, actualizar, eliminar)
- Gestionar reservas de habitaciones (crear, actualizar, eliminar)
- Gestionar habitaciones (crear, actualizar, eliminar)
- Gestionar pasajeros (crear, actualizar, eliminar)

El objetivo del sistema es automatizar y optimizar el proceso de reservas de habitaciones en un hotel, brindando una interfaz amigable y segura para los usuarios.

# 2. Instrucciones de instalación y configuración:

## Requisitos

- Python 3.7 o superior
- MySQL Server 5.7 o superior
- pip (gestor de paquetes de Python)

## Pasos de instalación

1. Clonar el repositorio del proyecto:
- git clone https://github.com/tu-usuario/reservas-hotel.git

2. Crear un entorno virtual de Python:
- python -m venv env
3. Activar el entorno virtual:
- En Windows: `env\Scripts\activate`
- En macOS/Linux: `source env/bin/activate`

4. Instalar las dependencias del proyecto:
- pip install -r requirements.txt

5. Crear la base de datos MySQL:
- Ejecutar el script SQL `sql_MySql.sql` para crear la base de datos y las tablas necesarias.

6. Configurar los datos de conexión a la base de datos:
- Abrir el archivo `impl/DatabaseSingleton.py` y actualizar los parámetros de conexión (host, user, password, database).

7. Ejecutar la aplicación:
- python main.py

- Ahora el sistema de reservas de hotel debería estar listo para su uso.

# 3. Documentación de clases, métodos y módulos:
## Documentación del código

### Capa DAO (Data Access Object)


#### `HabitacionDAO`
- Interfaz que define los métodos de acceso a los datos de las habitaciones.
- Métodos:
  - `get_all_habitaciones()`: Obtiene todas las habitaciones.
  - `buscar_habitacion(id_habitacion: int)`: Busca una habitación por su ID.
  - `crear_habitacion(habitacion: HabitacionDTO)`: Crea una nueva habitación.
  - `actualizar_habitacion(habitacion: HabitacionDTO)`: Actualiza una habitación existente.
  - `eliminar_habitacion(id_habitacion: int)`: Elimina una habitación.

#### `PasajeroDAO`
- Interfaz que define los métodos de acceso a los datos de los pasajeros.
- Métodos:
  - `get_all_pasajeros()`: Obtiene todos los pasajeros.
  - `buscar_pasajero(id_pasajero: int)`: Busca un pasajero por su ID.
  - `crear_pasajero(pasajero: PasajeroDTO)`: Crea un nuevo pasajero.
  - `actualizar_pasajero(pasajero: PasajeroDTO)`: Actualiza un pasajero existente.
  - `eliminar_pasajero(id_pasajero: int)`: Elimina un pasajero.

#### `ReservaDAO`
- Interfaz que define los métodos de acceso a los datos de las reservas.
- Métodos:
  - `get_all_reservas()`: Obtiene todas las reservas.
  - `buscar_reserva(id_reserva: int)`: Busca una reserva por su ID.
  - `crear_reserva(reserva: ReservaDTO)`: Crea una nueva reserva.
  - `actualizar_reserva(reserva: ReservaDTO)`: Actualiza una reserva existente.
  - `eliminar_reserva(id_reserva: int)`: Elimina una reserva.

#### `UsuarioDAO`
- Interfaz que define los métodos de acceso a los datos de los usuarios.
- Métodos:
  - `get_all_usuario()`: Obtiene todos los usuarios.
  - `buscar_usuario(idUsuario: int)`: Busca un usuario por su ID.
  - `crear_usuario(usuario: Usuario)`: Crea un nuevo usuario.
  - `actualizar_usuario(usuario: Usuario)`: Actualiza un usuario existente.
  - `eliminar_usuario(id_usuario: int)`: Elimina un usuario.

### Capa DTO (Data Transfer Object)

#### `HabitacionDTO`
- Clase que representa los datos de una habitación.
- Atributos:
  - `id_habitacion`: ID de la habitación.
  - `numero_habitacion`: Número de la habitación.
  - `capacidad`: Capacidad de la habitación.
  - `id_tipo_cama`: ID del tipo de cama.
  - `id_orientacion`: ID de la orientación.
  - `id_estado_hab`: ID del estado de la habitación.

#### `PasajeroDTO`
- Clase que representa los datos de un pasajero.
- Atributos:
  - `ID_PASAJERO`: ID del pasajero.
  - `NOMBRE_PASAJERO`: Nombre del pasajero.
  - `APELLIDO_PASAJERO`: Apellido del pasajero.
  - `FEC_NAC_PASAJERO`: Fecha de nacimiento del pasajero.
  - `USER_EMAIL_PASAJERO`: Correo electrónico del pasajero.
  - `DIRE_PASAJERO`: Dirección del pasajero.
  - `ID_REGION`: ID de la región del pasajero.
  - `ID_PROVINCIA`: ID de la provincia del pasajero.
  - `ID_COMUNA`: ID de la comuna del pasajero.

#### `ReservaDTO`
- Clase que representa los datos de una reserva.
- Atributos:
  - `id_reserva`: ID de la reserva.
  - `fec_reserva`: Fecha de la reserva.
  - `fec_llegada`: Fecha de llegada.
  - `fec_salida`: Fecha de salida.
  - `cant_pasajeros`: Cantidad de pasajeros.
  - `monto_total`: Monto total de la reserva.
  - `id_estado_reserva`: ID del estado de la reserva.
  - `penalizacion`: Penalización de la reserva.
  - `id_habitacion`: ID de la habitación reservada.

#### `Usuario`
- Clase que representa los datos de un usuario.
- Atributos:
  - `ID_USUARIO`: ID del usuario.
  - `USER_NOMBRE`: Nombre del usuario.
  - `USER_APELLIDO`: Apellido del usuario.
  - `USER_EMAIL`: Correo electrónico del usuario.
  - `CONTRASENA`: Contraseña del usuario.
  - `ES_ADMINISTRADOR`: Indica si el usuario es administrador.

### Capa de Implementación (IMPL)

#### `HabitacionDAOImpl`
- Implementación concreta de la interfaz `HabitacionDAO`.
- Utiliza el `DatabaseSingleton` para interactuar con la base de datos.
- Incluye métodos como `insertar_habitacion_en_db()`, `actualizar_habitacion()` y `eliminar_habitacion()`.

#### `PasajeroDAOImpl`
- Implementación concreta de la interfaz `PasajeroDAO`.
- Utiliza el `DatabaseSingleton` para interactuar con la base de datos.
- Incluye métodos como `crear_pasajero()`, `actualizar_pasajero()` y `eliminar_pasajero()`.

#### `ReservaDAOImpl`
- Implementación concreta de la interfaz `ReservaDAO`.
- Utiliza el `DatabaseSingleton` para interactuar con la base de datos.
- Incluye métodos como `crear_reserva()`, `actualizar_reserva()` y `eliminar_reserva()`.

#### `UsuarioDAOImpl`
- Implementación concreta de la interfaz `UsuarioDAO`.
- Utiliza el `DatabaseSingleton` para interactuar con la base de datos.
- Incluye métodos como `crear_usuario()`, `actualizar_usuario()` y `eliminar_usuario()`.

### Otros componentes

#### `DatabaseSingleton`
- Clase encargada de la conexión a la base de datos MySQL.
- Implementa el patrón Singleton para garantizar una única instancia de la conexión.
- Proporciona el método `get_connection()` para obtener la conexión a la base de datos.

#### `main.py`
- Punto de entrada de la aplicación.
- Contiene el código principal que maneja el flujo de ejecución del sistema de reservas de hotel.
- Llama a los métodos de las implementaciones DAO para realizar las operaciones de gestión de usuarios, reservas, habitaciones y pasajeros.

#### `C:\\cursos\\reserva_hotel\\queries.json`
- Archivo que almacena las consultas SQL utilizadas en el proyecto.
- Las implementaciones DAO hacen uso de estas consultas para interactuar con la base de datos.


# 4. Información sobre la estructura del proyecto:
## Estructura del proyecto

El proyecto sigue una arquitectura de n-capas, con las siguientes componentes principales:

### Capa DAO (Data Access Object)
Esta capa contiene las interfaces que definen los métodos de acceso a los datos, como `HabitacionDAO`, `PasajeroDAO`, `ReservaDAO` y `UsuarioDAO`.

### Capa DTO (Data Transfer Object)
Esta capa define las clases que representan los objetos de datos, como `HabitacionDTO`, `PasajeroDTO`, `ReservaDTO` y `Usuario`.

### Capa de Implementación (IMPL)
Esta capa contiene las implementaciones concretas de las interfaces DAO, como `HabitacionDAOImpl`, `PasajeroDAOImpl`, `ReservaDAOImpl` y `UsuarioDAOImpl`.

### Capa de presentación
El proyecto actual no incluye una capa de presentación explícita, ya que se trata de una aplicación de consola. Sin embargo, el punto de entrada `main.py` actúa como la capa de presentación y coordina la interacción entre las demás capas.

### Otros componentes
- `DatabaseSingleton`: Clase encargada de la conexión a la base de datos MySQL.
- `C:\\cursos\\reserva_hotel\\queries.json`: Archivo que almacena las consultas SQL utilizadas en el proyecto. 

# 5. Otra información relevante:
## Pautas de desarrollo

### Convenciones de nomenclatura
- Las clases deben seguir el formato `NombreClase`.
- Los métodos deben seguir el formato `nombre_metodo()`.
- Las variables deben seguir el formato `nombre_variable`.

### Estrategia de pruebas
- Se han implementado pruebas unitarias básicas para validar el almacenamiento de datos en los métodos `insertar_habitacion_en_db()` y `crear_pasajero()`.
- Se recomienda ampliar la cobertura de pruebas unitarias a medida que se añadan más funcionalidades al proyecto.
- Además de las pruebas unitarias, se deberían implementar pruebas de integración y pruebas de extremo a extremo para validar el correcto funcionamiento del sistema en su conjunto.

### Pautas de estilo de código
- Se debe mantener un estilo de código consistente, siguiendo las convenciones de Python (PEP 8).
- Los comentarios deben ser claros y conciso

# Validación del almacenamiento de datos y documentación de pruebas
- Debido a las limitaciones de tiempo, no he podido implementar completamente las validaciones y pruebas unitarias requeridas en este punto de la rúbrica. Sin embargo, a continuación se detalla cómo abordaría este proceso en un escenario ideal:

## Validaciones de almacenamiento de datos
- En los métodos de almacenamiento de datos, como insertar_habitacion_en_db() en HabitacionDAOImpl y crear_pasajero() en PasajeroDAOImpl, implementaría las siguientes validaciones:

### Verificar que los datos de entrada cumplan con los formatos y restricciones esperados, como:

- Campos numéricos (ID, números de habitación, capacidad, etc.) deben ser enteros positivos.
- Campos de texto (nombres, direcciones, etc.) deben cumplir con una longitud máxima y no estar vacíos.
- Fechas deben tener el formato esperado (YYYY-MM-DD).
- Correos electrónicos deben tener un formato válido.


### Comprobar que los valores de las claves foráneas (ID de tipo de cama, orientación, estado de habitación, región, provincia, comuna, etc.) correspondan a registros existentes en las tablas maestras.
### Manejar adecuadamente las excepciones que puedan ocurrir durante el almacenamiento de datos, como errores de conexión a la base de datos o violaciones de integridad.

## Pruebas unitarias
- Para validar el correcto almacenamiento de datos, crearía archivos de pruebas unitarias, como test_habitacion_dao.py y test_pasajero_dao.py, que incluirían los siguientes casos de prueba:

## Escenarios de éxito:

- Inserción de datos válidos para habitaciones y pasajeros.
- Verificación de que los datos se almacenen correctamente en la base de datos.


## Escenarios de error:

* Inserción de datos con formatos o valores inválidos (fuera de rango, vacíos, etc.).
* Inserción de datos con claves foráneas no existentes en las tablas maestras.
* Validación de que se manejen adecuadamente las excepciones durante el almacenamiento.



## Documentaría en detalle los pasos a seguir para ejecutar estas pruebas unitarias, así como los resultados esperados.
- Lamentablemente, debido a las limitaciones de tiempo, no he podido implementar completamente estas validaciones y pruebas. Sin embargo, en un escenario ideal, este sería el enfoque que seguiría para asegurar la calidad y robustez del almacenamiento de datos en el sistema.