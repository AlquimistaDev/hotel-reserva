from impl.UsuarioDAOImpl import UsuarioDAOImpl
from impl.ReservaDAOImpl import ReservaDAOImpl
from impl.HabitacionDAOImpl import HabitacionDAOImpl
from dto.UsuarioDTO import Usuario
from dto.ReservaDTO import ReservaDTO
from dto.HabitacionDTO import HabitacionDTO
from datetime import datetime
from dto.PasajeroDTO import PasajeroDTO
from impl.PasajeroDAOImpl import PasajeroDAOImpl


def mostrar_terminos_y_condiciones():
    print("--- Términos y Condiciones de Uso ---")
    print("1. Aceptación de los Términos")
    print("Al acceder y utilizar el sistema de reservas de hotel, usted acepta cumplir y estar sujeto a los siguientes términos y condiciones, así como a cualquier política o lineamiento adicional publicado por el proveedor del sistema.")
    print()
    print("2. Uso del Sistema")
    print("* El sistema de reservas de hotel está diseñado para uso personal y no comercial. Queda prohibido el uso del sistema con fines ilegales o dañinos.")
    print("* Los usuarios deben proporcionar información precisa y actualizada al momento de crear una cuenta o realizar reservaciones. Proporcionar información falsa o engañosa puede resultar en la suspensión o cancelación de la cuenta.")
    print("* Cada usuario es responsable de mantener la confidencialidad de su contraseña y cuenta de usuario. El proveedor no se hace responsable por el uso no autorizado de cuentas.")
    print()
    print("3. Reservas y Cancelaciones")
    print("* Las reservas están sujetas a disponibilidad y pueden estar limitadas durante temporadas altas o eventos especiales.")
    print("* El usuario es responsable de cancelar o modificar oportunamente sus reservas. Las políticas de cancelación y penalizaciones se detallan en el proceso de reserva.")
    print("* El proveedor se reserva el derecho de cancelar o modificar una reserva en caso de fuerza mayor, mantenimiento o problemas operativos.")
    print()
    print("4. Privacidad y Seguridad de Datos")
    print("* El proveedor se compromete a proteger la información personal de los usuarios de acuerdo con las leyes y regulaciones aplicables.")
    print("* Los datos proporcionados por los usuarios serán utilizados únicamente para brindar el servicio de reservas y mejorar la experiencia del usuario.")
    print("* El proveedor no compartirá ni venderá la información de los usuarios a terceros sin su consentimiento, excepto cuando sea requerido por ley.")
    print()
    print("5. Limitación de Responsabilidad")
    print("* El proveedor no se hace responsable por cualquier daño, directo o indirecto, que pueda derivarse del uso del sistema de reservas de hotel.")
    print("* El proveedor no garantiza la disponibilidad ininterrumpida o libre de errores del sistema. Los usuarios aceptan que pueden existir interrupciones, demoras o fallas en el servicio.")
    print()
    print("6. Modificaciones a los Términos")
    print("* El proveedor se reserva el derecho de modificar estos Términos y Condiciones de Uso en cualquier momento.")
    print("* Los cambios se publicarán en el sistema y se considerará que los usuarios han aceptado las modificaciones al continuar utilizando el servicio.")
    print()
    print("7. Contacto y Soporte")
    print("* Para cualquier consulta, comentario o reporte de problemas, los usuarios pueden comunicarse con el equipo de soporte a través del siguiente correo electrónico: soporte@reservashotel.com")
    print()
    
    while True:
        aceptacion = input("Al utilizar el sistema de reservas de hotel, usted acepta cumplir con estos Términos y Condiciones de Uso. Si no está de acuerdo, le solicitamos que se abstenga de utilizar este servicio. ¿Acepta? (s/n): ").lower()
        if aceptacion == 's':
            return True
        elif aceptacion == 'n':
            return False
        else:
            print("Opción no válida. Ingrese 's' para aceptar o 'n' para rechazar.")

def imprimir_separador():
    print("════════════════════════════════════════════════════════════")

    # print("╚════════════════════════════════════════════════════════════╝")

def mostrar_menu_principal():
    imprimir_separador()
    print("\n--- Sistema de Reservas de Hotel ---")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Reservas")
    print("3. Gestionar Habitaciones")
    print("4. Gestionar Pasajeros")
    print("5. Salir\n")
    imprimir_separador()
    return input("Seleccione una opción: ")

def gestionar_pasajeros():
    pasajero_dao = PasajeroDAOImpl()
    while True:
        print("\n--- Gestión de Pasajeros ---")
        print("1. Listar todos los pasajeros")
        print("2. Buscar pasajero por ID")
        print("3. Crear nuevo pasajero")
        print("4. Actualizar pasajero")
        print("5. Eliminar pasajero")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            pasajeros = pasajero_dao.get_all_pasajeros()
            for pasajero in pasajeros:
                print(f"Pasajero (ID: {pasajero.ID_PASAJERO}) - {pasajero.NOMBRE_PASAJERO} {pasajero.APELLIDO_PASAJERO}, Email: {pasajero.USER_EMAIL_PASAJERO}")
            if not pasajeros:
                print("No se encontraron pasajeros.")
            
             
        elif opcion == '2':
            id_pasajero = input("Ingrese el ID pasajero a buscar: ")
            try:
                id_pasajero = int(id_pasajero)
                pasajero = pasajero_dao.buscar_pasajero(id_pasajero)
                if pasajero:
                    print(f"Pasajero (ID: {pasajero.ID_PASAJERO}) - {pasajero.NOMBRE_PASAJERO} {pasajero.APELLIDO_PASAJERO}, Email: {pasajero.USER_EMAIL_PASAJERO}")
                else:
                    print(f"No se encontró ningun pasajero  con la ID {id_pasajero}")
            except ValueError:
                print(f"El ID ingresado no es valido. Debe ser número entero.")
            
            pass
        elif opcion == '3':
            print("\nCrear nuevo pasajero:")
            try:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fec_nacimiento = input("fecha de nacimiento(YYYY-MM-DD): ")
                email = input("Email: ")
                direccion = input("Dirección: ")
                id_region = int(input("ID región: "))
                id_provincia = int(input("ID de la provincia: "))
                id_comuna = int(input("ID de la comuna: "))


                nuevo_pasajero = PasajeroDTO(
                     ID_PASAJERO=None,
                    NOMBRE_PASAJERO=nombre,
                    APELLIDO_PASAJERO=apellido,
                    FEC_NAC_PASAJERO=datetime.strptime(fec_nacimiento, "%Y-%m-%d").date(),
                    USER_EMAIL_PASAJERO=email,
                    DIRE_PASAJERO=direccion,
                    ID_REGION=id_region,
                    ID_PROVINCIA=id_provincia,
                    ID_COMUNA=id_comuna
                 )
                if pasajero_dao.crear_pasajero(nuevo_pasajero):
                    print("Pasajero creado exitosamente.")
                else:
                    print("Error al crear pasajero.")
            except ValueError as e:
                print(f"Error de entrada: {e}")
            
        elif opcion == '4':
            id_pasajero = input("Ingrese el ID del pasajero a actualizar: ")
            try:
                id_pasajero = int(id_pasajero)
                pasajero_actual = pasajero_dao.buscar_pasajero(id_pasajero)
                if pasajero_actual:
                    print(f"Pasajero actual: {pasajero_actual}")
                    nombre = input(f"Nuevo nombre ({pasajero_actual.NOMBRE_PASAJERO}): ") or pasajero_actual.NOMBRE_PASAJERO 
                    print(nombre)
                    apellido = input(f"Nuevo apellido ({pasajero_actual.APELLIDO_PASAJERO}): ") or pasajero_actual.APELLIDO_PASAJERO
                    fec_nacimiento = input(f"Nueva fecha de nacimiento ({pasajero_actual.FEC_NAC_PASAJERO}): ") or str(pasajero_actual.FEC_NAC_PASAJERO)
                    email = input(f"Nuevo email ({pasajero_actual.USER_EMAIL_PASAJERO}): ") or pasajero_actual.USER_EMAIL_PASAJERO
                    direccion = input(f"Nueva dirección ({pasajero_actual.DIRE_PASAJERO}): ") or pasajero_actual.DIRE_PASAJERO
                    id_region = int(input(f"Nuevo ID de región ({pasajero_actual.ID_REGION}): ") or pasajero_actual.ID_REGION)
                    id_provincia = int(input(f"Nuevo ID de provincia ({pasajero_actual.ID_PROVINCIA}): ") or pasajero_actual.ID_PROVINCIA)
                    id_comuna = int(input(f"Nuevo ID de comuna ({pasajero_actual.ID_COMUNA}): ") or pasajero_actual.ID_COMUNA)

                    pasajero_actualizado = PasajeroDTO(
                        ID_PASAJERO=id_pasajero,
                        NOMBRE_PASAJERO=nombre,
                        APELLIDO_PASAJERO=apellido,
                        FEC_NAC_PASAJERO=datetime.strptime(fec_nacimiento, "%Y-%m-%d").date(),
                        USER_EMAIL_PASAJERO=email,
                        DIRE_PASAJERO=direccion,
                        ID_REGION=id_region,
                        ID_PROVINCIA=id_provincia,
                        ID_COMUNA=id_comuna
                    )
                    print('pasajero_actualizado::::::::::::::',pasajero_actualizado)
                    if pasajero_dao.actualizar_pasajero(pasajero_actualizado):
                        print("Pasajero actualizado exitosamente.")
                    else:
                        print("Error al actualizar el pasajero.")
                else:
                    print(f"No se encontró ningún pasajero con el ID {id_pasajero}")
            except ValueError as e:
                print(f"Error de entrada: {e}")

        elif opcion == '5':
            id_pasajero = input("Ingrese el ID del pasajero a eliminar: ")
            try:
                id_pasajero = int(id_pasajero)
                pasajero = pasajero_dao.buscar_pasajero(id_pasajero)
                if pasajero:
                    print(f"Pasajero a eliminar: {pasajero}")
                    confirmacion = input("¿Está seguro de que desea eliminar este pasajero? (s/n): ").lower()
                    if confirmacion == 's':
                        if pasajero_dao.eliminar_pasajero(id_pasajero):
                            print("Pasajero eliminado exitosamente.")
                        else:
                            print("Error al eliminar el pasajero.")
                    else:
                        print("Operación de eliminación cancelada.")
                else:
                    print(f"No se encontró ningún pasajero con el ID {id_pasajero}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def gestionar_usuarios():
    usuario_dao = UsuarioDAOImpl()
    while True:
        imprimir_separador()
        print("\n--- Gestión de Usuarios ---")
        print("1. Listar todos los usuarios")
        print("2. Buscar usuario por ID")
        print("3. Agregar nuevo usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Volver al menú principal")
        imprimir_separador()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            usuarios = usuario_dao.get_all_usuario()
            if usuarios:
                print("\nLista de Usuarios:")
                for usuario in usuarios:
                    print(f"ID: {usuario.ID_USUARIO}, usuario: {usuario.USER_NOMBRE} - {usuario.USER_APELLIDO}, Email: {usuario.USER_EMAIL}")
            else:
                print("No se encontraron usuarios.")
        elif opcion == '2':
            id_usuario = input("Ingrese el ID del usuario a buscar: ")
            try:
                id_usuario = int(id_usuario)
                usuario = usuario_dao.buscar_usuario(id_usuario)
                print('usuario::::::::::', usuario)
                if usuario:
                    print(f"\nUsuario encontrado:")
                    print(f"ID: {usuario.ID_USUARIO}, Nombre: {usuario.USER_NOMBRE} {usuario.USER_APELLIDO}, Email: {usuario.USER_EMAIL}, Es Admin: {usuario.ES_ADMINISTRADOR}")
                else:
                    print(f"No se encontró ningún usuario con el ID {id_usuario}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '3':
            print("\n Agregar nuevo usuario:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            es_admin = input("¿Es administrador (s/n): ").lower() == 's'

            nuevo_usuario = Usuario(
                ID_USUARIO=None,
                USER_NOMBRE=nombre,
                USER_APELLIDO=apellido,
                USER_EMAIL=email,
                CONTRASENA=password,
                ES_ADMINISTRADOR=es_admin
            )
            if usuario_dao.crear_usuario(nuevo_usuario):
                print("Usuario creado exitosamente.")
            else:
                print("Error al crear el usuario.")
        elif opcion == '4':
            id_usuario = input("Ingrese el Id del usuario a actualizar: ")
            try:
                id_usuario = int(id_usuario)
                usuario = usuario_dao.buscar_usuario(id_usuario)
                if usuario:
                    print(f"Usuario actual: {usuario}")
                    nombre = input(f"Nuevo nombre ({usuario.USER_NOMBRE}): ") or usuario.USER_NOMBRE
                    apellido = input(f"Nuevo apellido({usuario.USER_APELLIDO}): ") or usuario.USER_APELLIDO
                    email = input(f"Nuevo email({usuario.USER_EMAIL}): ") or usuario.USER_EMAIL
                    password = input(f"Nueva contraseña(dejar en blanco para no cambiar): ") or usuario.CONTRASENA
                    es_admin = input(f"¿Es administrador?(s/n)({usuario.ES_ADMINISTRADOR}): ").lower()
                    es_admin = es_admin == 's' if es_admin else usuario.ES_ADMINISTRADOR

                    usuario_actualizado = Usuario(
                        ID_USUARIO=id_usuario,
                        USER_NOMBRE=nombre,
                        USER_APELLIDO=apellido,
                        USER_EMAIL=email,
                        CONTRASENA=password,
                        ES_ADMINISTRADOR=es_admin
                    )
                    if usuario_dao.actualizar_usuario(usuario_actualizado):
                        print("Usuario actualizado exitosamente")
                    else:
                        print("Error al actualizar el usuario.")
                else:
                    print("No se encontró el usuario.")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '5':
            id_usuario = input("Ingrese el ID del usuario a eliminar: ")
            try:
                id_usuario = int(id_usuario)
                usuario = usuario_dao.buscar_usuario(id_usuario)
                if usuario:
                    print(f"Usuario a eliminar: ID: {usuario.ID_USUARIO}, Nombre: {usuario.USER_NOMBRE} {usuario.USER_APELLIDO}, Email: {usuario.USER_EMAIL}")
                    confirmacion = input("¿Está seguro de que desea eliminar este usuario? (s/n): ").lower()
                    if confirmacion == 's':
                        if usuario_dao.eliminar_usuario(id_usuario):
                            print("Usuario eliminado exitosamente.")
                        else:
                            print("Error al eliminar el usuario.")
                    else:
                        print("Operación de eliminación cancelada.")
                else:
                    print(f"No se encontró ningún usuario con el ID {id_usuario}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def gestionar_reservas():
    reserva_dao = ReservaDAOImpl()
    while True:
        print("\n--- Gestión de Reserva---")
        print("1. Listar todas las reservas")
        print("2. Buscar reserva por ID")
        print("3. Crear nueva reserva")
        print("4. Actualizar reserva")
        print("5. Eliminar reserva")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción:")

        if opcion == '1':
            reservas = reserva_dao.get_all_reservas()
            if reservas:
                print("\nLista de Reservas:")
                for reserva in reservas:
                    print(f"ID: {reserva.id_reserva} | Fecha Reserva: {reserva.fec_reserva} | Ingreso: {reserva.fec_llegada} | Salida: {reserva.fec_salida} | Habitación: {reserva.id_habitacion}")
            else:
                print("No se encontraron reservas.")
        elif opcion == '2':
            id_reserva = input("Ingrese el ID de la reserva a buscar: ")
            try:
                id_reserva = int(id_reserva)
                reserva = reserva_dao.buscar_reserva(id_reserva)
                if reserva:
                    print(f"\nReserva encontrada:")
                    print(f"ID: {reserva.id_reserva} | Fecha Reserva: {reserva.fec_reserva} | Ingreso: {reserva.fec_llegada} | Salida: {reserva.fec_salida} | Habitación: {reserva.id_habitacion}")
                else:
                    print(f"No se encontró ninguna reserva con el ID {id_reserva}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '3':
            print("\nCrear nueva reserva:")
            try:
                fec_reserva = datetime.now().date()
                fec_llegada = input("Fecha de llegada (YYYY-MM-DD): ")
                fec_salida = input("Fecha de salida (YYYY-MM-DD): ")
                cant_pasajeros = int(input("Cantidad de pasajeros: "))
                monto_total = float(input("Monto total: "))
                #id_estado_reserva = int(input("ID del estado de reserva: "))
                penalizacion = float(input("Penalización (si aplica): "))
                id_habitacion = int(input("ID de la habitación: "))

                nueva_reserva = ReservaDTO(
                    id_reserva=None,
                    fec_reserva=fec_reserva,
                    fec_llegada=datetime.strptime(fec_llegada, "%Y-%m-%d").date(),
                    fec_salida=datetime.strptime(fec_salida, "%Y-%m-%d").date(),
                    cant_pasajeros=cant_pasajeros,
                    monto_total=monto_total,
                    id_estado_reserva=1,
                    penalizacion=penalizacion,
                    id_habitacion=id_habitacion
                )

                if reserva_dao.crear_reserva(nueva_reserva):
                    print("Reserva creada exitosamente.")
                else:
                    print("Error al crear la reserva.")
            except ValueError as e:
                print(f"Error de entrada: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == '4':
            id_reserva = input("Ingrese el ID de la reserva a actualizar: ")
            try:
                id_reserva = int(id_reserva)
                reserva_actual = reserva_dao.buscar_reserva(id_reserva)
                if reserva_actual:
                    print(f"Reserva actual: {reserva_actual}")
                    fec_llegada = input(f"Nueva fecha de llegada ({reserva_actual.fec_llegada}): ") or str(reserva_actual.fec_llegada)
                    fec_salida = input(f"Nueva fecha de salida ({reserva_actual.fec_salida}): ") or str(reserva_actual.fec_salida)
                    cant_pasajeros = input(f"Nueva cantidad de pasajeros ({reserva_actual.cant_pasajeros}): ") or reserva_actual.cant_pasajeros
                    monto_total = input(f"Nuevo monto total ({reserva_actual.monto_total}): ") or reserva_actual.monto_total
                    
                    id_estado_reserva = input(f"Nuevo ID de estado de reserva ({reserva_actual.id_estado_reserva}): ") or reserva_actual.id_estado_reserva
                    penalizacion = input(f"Nueva penalización ({reserva_actual.penalizacion}): ") or reserva_actual.penalizacion
                    id_habitacion = input(f"Nuevo ID de habitación ({reserva_actual.id_habitacion}): ") or reserva_actual.id_habitacion

                    reserva_actualizada = ReservaDTO(
                        id_reserva=id_reserva,
                        fec_reserva=reserva_actual.fec_reserva,
                        fec_llegada=datetime.strptime(fec_llegada, "%Y-%m-%d").date(),
                        fec_salida=datetime.strptime(fec_salida, "%Y-%m-%d").date(),
                        cant_pasajeros=int(cant_pasajeros),
                        monto_total=float(monto_total),
                        id_estado_reserva=int(id_estado_reserva),
                        penalizacion=float(penalizacion),
                        id_habitacion=int(id_habitacion)
                    )

                    if reserva_dao.actualizar_reserva(reserva_actualizada):
                        print("Reserva actualizada exitosamente.")
                    else:
                        print("Error al actualizar la reserva.")
                else:
                    print(f"No se encontró ninguna reserva con el ID {id_reserva}")
            except ValueError as e:
                print(f"Error de entrada: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == '5':
            id_reserva = input("Ingrese el ID de la reserva a eliminar: ")
            try:
                id_reserva = int(id_reserva)
                reserva = reserva_dao.buscar_reserva(id_reserva)
                if reserva:
                    print(f"Reserva a eliminar: ID: {reserva.id_reserva}, Fecha: {reserva.fec_reserva}, Habitación: {reserva.id_habitacion}")
                    confirmacion = input("¿Está seguro de que desea eliminar esta reserva? (s/n): ").lower()
                    if confirmacion == 's':
                        if reserva_dao.eliminar_reserva(id_reserva):
                            print("Reserva eliminada exitosamente.")
                        else:
                            print("Error al eliminar la reserva.")
                    else:
                        print("Operación de eliminación cancelada.")
                else:
                    print(f"No se encontró ninguna reserva con el ID {id_reserva}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def gestionar_habitaciones():
    habitacion_dao = HabitacionDAOImpl()
    while True:
        print("\n--- Gestión de Habitaciones ---")
        print("1. Listar todas las habitaciones")
        print("2. Buscar habitación por ID")
        print("3. Crear nueva habitación")
        print("4. Actualizar habitación")
        print("5. Eliminar habitación")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            habitaciones = habitacion_dao.get_all_habitaciones()
            if habitaciones:
                print("\nLista de Habitaciones:")
                for habitacion in habitaciones:
                    print(habitacion)
            else:
                print("No se encontraron habitaciones.")
        elif opcion == '2':
            id_habitacion = input("Ingrese el ID de la habitación a buscar: ")
            try:
                id_habitacion = int(id_habitacion)
                habitacion = habitacion_dao.buscar_habitacion(id_habitacion)
                if habitacion:
                    print(f"\nHabitación encontrada:")
                    print(habitacion)
                else:
                    print(f"No se encontró ninguna habitación con el ID {id_habitacion}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '3':
            if habitacion_dao.crear_habitacion():
                pass
            else:
                print("Error al crear la habitación.")
        elif opcion == '4':
            id_habitacion = input("Ingrese el ID de la habitación a actualizar: ")
            try:
                id_habitacion = int(id_habitacion)
                habitacion_actual = habitacion_dao.buscar_habitacion(id_habitacion)
                if habitacion_actual:
                    print(f"Habitación actual: {habitacion_actual}")
                    numero_habitacion = int(input(f"Nuevo número de habitación ({habitacion_actual.numero_habitacion}): ") or habitacion_actual.numero_habitacion)
                    capacidad = int(input(f"Nueva capacidad ({habitacion_actual.capacidad}): ") or habitacion_actual.capacidad)
                    id_tipo_cama = int(input(f"Nuevo ID de tipo de cama ({habitacion_actual.id_tipo_cama}): ") or habitacion_actual.id_tipo_cama)
                    id_orientacion = int(input(f"Nuevo ID de orientación ({habitacion_actual.id_orientacion}): ") or habitacion_actual.id_orientacion)
                    id_estado_hab = int(input(f"Nuevo ID de estado de habitación ({habitacion_actual.id_estado_hab}): ") or habitacion_actual.id_estado_hab)

                    habitacion_actualizada = HabitacionDTO(
                        id_habitacion=id_habitacion,
                        numero_habitacion=numero_habitacion,
                        capacidad=capacidad,
                        id_tipo_cama=id_tipo_cama,
                        id_orientacion=id_orientacion,
                        id_estado_hab=id_estado_hab
                    )

                    if habitacion_dao.actualizar_habitacion(habitacion_actualizada):
                        print("Habitación actualizada exitosamente.")
                    else:
                        print("Error al actualizar la habitación.")
                else:
                    print(f"No se encontró ninguna habitación con el ID {id_habitacion}")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        elif opcion == '5':
            id_habitacion = input("Ingrese el ID de la habitación a eliminar: ")
            try:
                id_habitacion = int(id_habitacion)
                habitacion = habitacion_dao.buscar_habitacion(id_habitacion)
                if habitacion:
                    print(f"Habitación a procesar: {habitacion}")
                    confirmacion = input("¿Está seguro de que deseas procesar esta habitación? (s/n): ").lower()
                    if confirmacion == 's':
                        if habitacion_dao.eliminar_habitacion(id_habitacion):
                            print("Operación completada exitosamente.")
                        else:
                            print("No se pudo procesar  la habitación.")
                    else:
                        print("Operación cancelada.")
                else:
                    print(f"No se encontró ninguna habitación activa con el ID {id_habitacion}")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def main():
    if mostrar_terminos_y_condiciones():
        while True:
            opcion = mostrar_menu_principal()
            if opcion == '1':
                gestionar_usuarios()
            elif opcion == '2':
                gestionar_reservas()
            elif opcion == '3':
                gestionar_habitaciones()
            elif opcion == '4':
                gestionar_pasajeros()
            elif opcion == '5':
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
    else:
        print("No se puede acceder al sistema sin aceptar los Términos y Condiciones.")

if __name__ == "__main__":
    main()

