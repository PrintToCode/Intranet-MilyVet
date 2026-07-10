# Intranet MilivetV2



# ╔══════════════════════════════════════════════════════════╗
# ║                      IMPORTAR LIBRERIAS                  ║
# ╚══════════════════════════════════════════════════════════╝

# Importar módulo os para crear la función "limpiar_pantalla"
import os

# Importar módulo getpass para ocultar las contraseñas ingresadas por los usuarios
import getpass

# Importar módulo re para usar regex
import re

# Importar la clase datetime (módulo datetime) para validar la fecha de nacimiento de las mascotas
from datetime import datetime

# Importar módulo radom para generar código de pago
import random

# ╔══════════════════════════════════════════════════════════╗
# ║                  FIN IMPORTAR LIBRERIAS                  ║
# ╚══════════════════════════════════════════════════════════╝



# ╔══════════════════════════════════════════════════════════╗
# ║                  CONSTRUCCION DE BD                      ║
# ╚══════════════════════════════════════════════════════════╝

# Se crea un diccionario que ayudará a generar el ID al registrar una mascota
contador_id = {
    "CAN": 1
}

# Se crea un diccionario que ayudará a generar el ID de atención
atencion_id = {
    "ATN": 1
}

#Se crea una lista de usuarios para simular una tabla de BD
tabla_usuarios = []

#Se crea una lista de mascotas para simular una tabla de BD
tabla_mascotas = []

#Se crea una lista de atenciones para simular una tabla de BD
tabla_atenciones = []

#Se crea una lista de citas para simular una tabla de BD
tabla_citas = []

#Se crea una lista de pagos para simular una tabla de BD
tabla_pagos = []

#Se crea la clase usuario
class Usuario:
    def __init__(self, correo, contrasena, preguntas_respuestas, bloqueado, rol):
        self.correo = correo
        self.contrasena = contrasena
        self.preguntas_respuestas = preguntas_respuestas
        self.bloqueado = bloqueado
        self.rol = rol

# Se crea la clase mascota
class Mascota:
    def __init__(self, id, correo_dueno, nombre, sexo, especie, raza, fecha_nacimiento, peso_kg):
        self.id = id
        self.correo_dueno = correo_dueno
        self.nombre = nombre
        self.sexo = sexo
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.peso_kg = peso_kg

# Se crea la clase atencion
class Atencion:
    def __init__(self, id_atencion, correo_dueno, id_mascota, motivo, diagnostico, tratamiento, precio_soles, fecha_atencion):
        self.id_atencion = id_atencion
        self.correo_dueno = correo_dueno
        self.id_mascota = id_mascota
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.precio_soles = precio_soles
        self.fecha_atencion = fecha_atencion

#Se crea clase cita
class Cita:

    def __init__(self, id_mascota, medico, especialidad, fecha, hora, estado):

        self.id_mascota = id_mascota
        self.medico = medico
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

#Se crea la clase pagos
class Pago:

    def __init__(self, id_mascota, medico, fecha, hora, metodo, monto, estado, codigo_pago):
        self.id_mascota = id_mascota
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.metodo = metodo
        self.monto = monto
        self.estado = estado
        self.codigo_pago = codigo_pago

#Se crea un usuario de prueba
usuario1 = Usuario(
    correo = "luis.alberca.munive@gmail.com",
    contrasena = "clave123",
    preguntas_respuestas = [
        ("¿Nombre de tu mascota?", "firulais"),
        ("¿Ciudad donde naciste?", "lima"),
        ("¿Película favorita?", "matrix")
    ],
    bloqueado = False,
    rol = "VET"
)

#Se agrega el usuario creado a la "tabla_usuarios"
tabla_usuarios.append(usuario1)

#Se crea una lista de medicos para simular una tabla de BD
tabla_medicos = [

    {"nombre":"Dr. Carlos Pérez","especialidad":"Medicina General"},
    {"nombre":"Dra. Ana Ruiz","especialidad":"Medicina General"},

    {"nombre":"Dr. Luis Gómez","especialidad":"Vacunación"},
    {"nombre":"Dra. Rosa Torres","especialidad":"Vacunación"},

    {"nombre":"Dr. Miguel Flores","especialidad":"Desparasitación"},
    {"nombre":"Dra. Ana Mendoza","especialidad":"Desparasitación"},

    {"nombre":"Dr. Javier Ruiz","especialidad":"Cirugía"},
    {"nombre":"Dra. Claudia León","especialidad":"Cirugía"}

]

#Precios referenciales por especialidad
precios_especialidad = {
    "Medicina General": 50.00,
    "Vacunación": 40.00,
    "Desparasitación": 35.00,
    "Cirugía": 200.00
}

#Se crea una mascota de prueba
mascota1 = Mascota(
    id = "CAN-001",
    correo_dueno = "luis.alberca.munive@gmail.com",
    nombre = "Firulais",
    sexo = "Macho",
    especie = "Perro",
    raza = "Bulldog",
    fecha_nacimiento = "04/07/2025",
    peso_kg = "24.50"
)

#Se agrega la mascota creada a la "tabla_mascotas"
tabla_mascotas.append(mascota1)

#Se crea una atención de prueba
atencion1 = Atencion(
    id_atencion = "ATN-001",
    correo_dueno = "luis.alberca.munive@gmail.com",
    id_mascota = "CAN-001",
    motivo = "Mascota presenta cansancio excesivo",
    diagnostico = "Sobrepeso",
    tratamiento = "Dieta",
    precio_soles = "50.00",
    fecha_atencion = "15/07/2026",
)

#Se agrega la mascota creada a la "tabla_atenciones"
tabla_atenciones.append(atencion1)

# ╔══════════════════════════════════════════════════════════╗
# ║                  FIN CONSTRUCCION DE BD                  ║
# ╚══════════════════════════════════════════════════════════╝



# ╔══════════════════════════════════════════════════════════╗
# ║                      FUNCIONES DE APOYO                  ║
# ╚══════════════════════════════════════════════════════════╝

####FUNCION LIMPIAR PANTALLA####
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
########################

####FUNCION VALIDAR CONTRASEÑA####
def validar_contrasena(contrasena):

    # Se define un arreglo para guardar los erroes relacionados con la contraseña ingresada
    errores = []

    # Se evalua si la contraseña ingresada tiene una longitud menor a 20 caracteres
    if len(contrasena) < 20:
        #Si la contraseña no cumple con el criterio, entonces se agrega el mensaje de error respectivo al arreglo errores
        errores.append("La contraseña debe tener una longitud mínima de 20 caracteres")

    # Se evalua si la contraseña ingresada tiene por lo menos 1 caracter especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\/;'~`]", contrasena):
        #Si la contraseña no cumple con el criterio, entonces se agrega el mensaje de error respectivo al arreglo errores
        errores.append("La contraseña debe tener por los menos 1 caracter especial")
    
    # Se evalua si la contraseña ingresada tiene por lo menos 1 número
    if not re.search(r"[0-9]", contrasena):
        #Si la contraseña no cumple con el criterio, entonces se agrega el mensaje de error respectivo al arreglo errores
        errores.append("La contrseña debe tener por lo menos 1 número")
    
    # Se evalua si la contraseña ingresada tiene por lo menos 1 caracter en mayúscula
    if not re.search(r"[A-Z]", contrasena):
        #Si la contraseña no cumple con el criterio, entonces se agrega el mensaje de error respectivo al arreglo errores
        errores.append("La contraseña debe tener por lo menos 1 caracter en mayúscula")
    
    # Se evalua si la contraseña ingresada tiene por lo menos 1 caracter en minúscula
    if not re.search(r"[a-z]", contrasena):
        #Si la contraseña no cumple con el criterio, entonces se agrega el mensaje de error respectivo al arreglo errores
        errores.append("La contraseña debe tener por lo menos 1 caracter en minúscula")

    # Si no se presentan errores de validación en la contraseña, entonces el valor de la variable contrasena_valida es true, de lo contrario es false
    contrasena_valida = len(errores) == 0

    # Si la contraseña cumple con la complejidad
    if contrasena_valida == True:
        # Se imprime el mensaje de éxito correspondiente
        print("\nContraseña válida ✅")
        # Se retorna el string "valida"
        return "valida"
    # Si la contraseña NO cumple con la complejidad
    else:
        # Se imprime el mensaje de error correspondiente
        print("\nContraseña inválida ❌. Errores encontarados:\n")
        # Se listan los errores encontrados en la complejidad de la contraseña
        for error in errores:
            print(f"- {error}")
        
        # Se utiliza un while para validar si el usuario quiere reintentar ingresar el la contraseña
        while True:
            # Se espera que el usuario presione R para reintentar o S para salir, elminan los espacios alrededor de la opción ingresada y se convierte a minúscula
            opcion = input("\nPresione (R) para reintentar ó (S) para salir: ").strip().lower()

            # Se evalúa la opción ingresada
            match opcion:
                # Si es 'r'
                case 'r':
                    # Se retorna el valor "reintentar"
                    return "reintentar"
                # Si es 's'
                case 's':
                    # Se retorna el valor "inicial"
                    return "inicial"
                # Si la opción ingresada no es válida
                case _:
                    # Se limpia la pantalla
                    limpiar_pantalla()
                    # Se imprime el mensaje de error correspondinete
                    print("\nOpción inválida ❌")
                    # Se pasa a la siguiente iteración del while que valida la variable 'opcion'
                    continue
##############################

####FUNCION VALIDAR CORREO####
def validar_correo(correo_ingresado):
    
    # Se valida el correo ingresado utilizando Regex
        validar_correo = re.fullmatch(r"[a-zA-Z1-9._-]+@[a-zA-Z1-9._-]+\.[a-zA-Z1-9]{2,}", correo_ingresado)

        # Si el correo ingresado no cumple con el formato
        if not validar_correo:
            # Se inprime el mensaje de error respectivo
            print("\nEl formato de correo ingresado no es válido ❌")

            # Se utiliza un while para validar si el usuario quiere reintentar ingresar el correo
            while True:
                # Se espera que el usuario presione R para reintentar o S para salir, elminan los espacios alrededor de la opción ingresada y se convierte a minúscula
                reintentar = input("\nPresione (R) para reintentar ó (S) para salir: ").strip().lower()

                # Se evalúa la opción ingresada
                match reintentar:
                    
                    # Si es 'r'
                    case 'r':
                        # Se retorna el valor "reintentar"
                        return "reintentar"

                    # Si es 's'
                    case 's':
                        # Se retorna el valor "salir"
                        return "salir"
                    
                    # Si la opción ingresada no es válida
                    case _:
                        # Se limpia la pantalla
                        limpiar_pantalla()
                        # Se imprime el mensaje de error correspondinete
                        print("\nOpción inválida ❌")
                        # Se pasa a la siguiente iteración del while que valida la variable 'reintentar'
                        continue
        # Si el correo ingresado cumple con el formato
        else:
            # Se retorna el valor "correcto"
            return "correcto"
##############################
    
####FUNCION GENERAR ID MASCOTA####
def generar_id_mascota(especie):

    # Se evalua la especie
    match especie:

        # Si es Perro
        case "Perro":
            # Se genera el nuevo número de mascota
            nuevo_numero_mascota = contador_id.get("CAN", 0) + 1
            # Se retorna el id generado
            return f"CAN-{nuevo_numero_mascota:03d}"
        
        # Si es Gato
        case "Gato":
            # Se genera el nuevo número de mascota
            nuevo_numero_mascota = contador_id.get("FEL", 0) + 1
            # Se retorna el id generado
            return f"FEL-{nuevo_numero_mascota:03d}"
        
        # Si es Ave
        case "Ave":
            # Se genera el nuevo número de mascota
            nuevo_numero_mascota = contador_id.get("AVE", 0) + 1
            # Se retorna el id generado
            return f"AVE-{nuevo_numero_mascota:03d}"
        
        # Si es Conejo
        case "Conejo":
            # Se genera el nuevo número de mascota
            nuevo_numero_mascota = contador_id.get("CON", 0) + 1
            # Se retorna el id generado
            return f"CON-{nuevo_numero_mascota:03d}"
        
        # Si es Otro
        case "Otro":
            # Se genera el nuevo número de mascota
            nuevo_numero_mascota = contador_id.get("OTR", 0) + 1
            # Se retorna el id generado
            return f"OTR-{nuevo_numero_mascota:03d}"
##################################

####FUNCION ACTUALIZAR CONTADOR ID####
def actualizar_contador_id(especie):

    # Se evalua la especie
    match especie:

        # Si es Perro
        case "Perro":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["CAN"] = contador_id.get("CAN", 0) + 1
            # Se termina la función
            return
        
        # Si es Gato
        case "Gato":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["FEL"] = contador_id.get("FEL", 0) + 1
            # Se termina la función
            return
        
        # Si es Ave
        case "Ave":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["AVE"] = contador_id.get("AVE", 0) + 1
            # Se termina la función
            return
        
        # Si es Conejo
        case "Conejo":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["CON"] = contador_id.get("CON", 0) + 1
            # Se termina la función
            return
        
        # Si es Otro
        case "Otro":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["OTR"] = contador_id.get("OTR", 0) + 1
            # Se termina la función
            return
##################################

####FUNCION RESUMEN DEL DIA####
def resumen_dia():

    # Se obtiene la fecha actual
    fecha_actual = datetime.now().date().strftime("%d/%m/%Y")

    # Se inicializa el contador "total_atenciones"
    total_atenciones = 0

    # Se inicializa el acumulador "total_ingresos"
    total_ingresos = 0

    # Se recorren todas las atenciones de la lista "tabla_atenciones"
    for atencion in tabla_atenciones:
        # Si la atención fue realizada en "fecha_actual"
        if atencion.fecha_atencion == fecha_actual:
            # Se incrementa en 1 el contador "total_atenciones"
            total_atenciones += 1

            # Se acumula el precio en la variable "total_ingresos"
            total_ingresos += float(atencion.precio_soles)

    # Se retorna el total de atenciones y el total de ingresos
    return total_atenciones, total_ingresos
###############################

####FUNCION GENERAR ID ATENCION####
def generar_id_atencion():

    # Se genera el número de la nueva atención
    num_nueva_atencion = atencion_id.get("ATN", 0) + 1

    # Se genera el ID de la nueva atención
    id_nueva_atencion = f"ATN-{num_nueva_atencion:03d}"

    # Se retorna el número e ID de la nueva atención
    return num_nueva_atencion, id_nueva_atencion
####################################

# ╔══════════════════════════════════════════════════════════╗
# ║                  FIN FUNCIONES DE APOYO                  ║
# ╚══════════════════════════════════════════════════════════╝



# ╔══════════════════════════════════════════════════════════╗
# ║                  FUNCIONES MENÚ INICIAL                  ║
# ╚══════════════════════════════════════════════════════════╝

####1.FUNCION MENU INICIAL####
def menu_inicial():
    while True:

        #Se limpia la pantalla
        limpiar_pantalla()
        
        #Se muestra el Menú Inicial
        print(r"""
    /\_/\        __  ____ ___ _    __     __       / \__ 
    ( o.o )      /  |/  (_) (_) |  / /__  / /_     (    @\_
    > ^ <      / /|_/ / / / /| | / / _ \/ __/     /       O
                / /  / / / / / | |/ /  __/ /_      /   (____/
            /_/  /_/_/_/_/  |___/\___/\__/      /___/  U  
    """)
        print("====MENU INICIAL - MilyVet====")
        print("1. Iniciar Sesion")
        print("2. Nuevo Usuario")
        print("3. Recuperar Contraseña")
        print("4. Salir")

        #Se pide al usuario que ingrese una opción
        main_option = int(input("Ingrese una opción: "))

        #Se evalúa la opción ingresada en el menú inicial
        match main_option:

            #INICIAR SESION
            case 1:
                #Se limpia la pantalla
                limpiar_pantalla()

                # Se ejecuta función iniciar_sesion
                iniciar_sesion()

            #NUEVO USUARIO
            case 2:
                #Se limpia la pantalla
                limpiar_pantalla()

                #Se ejecuta función nuevo_usuario
                nuevo_usuario()

            #RECUPERAR CONTRASEÑA
            case 3:
                #Se limpia la pantalla
                limpiar_pantalla()

                #Se ejecuta función recuperar_contrasena
                recuperar_contrasena()

            #SALIR
            case _:
                #Se limpia la pantalla
                limpiar_pantalla()

                #Se imprime mensaje de despedida
                print("🐶🐱Hasta luego🐾...\n")

                #Se sale del bucle
                break
############################

####1.1.FUNCION INICIAR SESION####
def iniciar_sesion():

    # While que se utiliza para validar la variable "correo"
    while True:

        # Se solicita al usuario ingresar su correo
        correo = input("\nIngresar correo: ").strip().lower()
        
        # Se valida el correo ingresado
        correo_valido = validar_correo(correo)

        # Se evalúa el valor de la variable "correo_valido"
        match correo_valido:

            # Si es "reintentar"
            case "reintentar":
                # Se limpía la pantalla
                limpiar_pantalla()
                # Se pasa a la siguien te iteración del while que valida la variable "correo"
                continue
            
            # Si es "salir"
            case "salir":
                # Se regresa al Menú Inicial
                return
            
            # Si es "correcto"
            case "correcto":
                # Se sale del while que valida la variable "correo"
                break

    # Se itera sobre los objetos user del arreglo tabla_usuarios
    for user in tabla_usuarios:

        # Si se encuentra el correo ingresado
        if user.correo == correo:

            # Si la cuenta está bloqueada
            if user.bloqueado:
                # Se imprime el mensaje correspondiente
                print("\n¡La cuenta se encuentra bloqueada! ❌")

                # Se espera que el usuario presione cualquier tecla para continuar
                input("\nPresione cualquier tecla para continuar...")

                # Se retorna el Menú Inicial
                return
            
            # Si la cuenta no está bloqueada
            else:

                # Se solicita ingresar la contraseña hasta un máximo de 3 veces
                for intentos in range(3):
                    # Se solicita al usuario ingresar la contraseña de la cuenta
                    contrasena = getpass.getpass("Ingresar contraseña: ")

                    # Si la contraseña ingresada coincide con la contraseña del objeto usuario
                    if user.contrasena == contrasena:

                        # Se muestra el mensaje de éxito respectivo
                        print("\nInicio de Sesión Correcto ✅")

                        # Se espera que el usuario presione cualquier tecla para continuar
                        input("\nPresione cualquier tecla para continuar...")

                        # Se ejecuta la función menu_sistema y se envía como parámetro el correo ingresado
                        menu_sistema(correo)

                        # Se retorna el Menú Inicial
                        return
                    
                    #Si la contraseña ingresada no coincide con la contraseña del objeto usuario
                    else:
                            # Se muestra el mensaje de error respectivo
                            print(f"\nContraseña incorrecta ❌. Le quedan {2 - intentos} intentos.")

                # Si se superan los 3 intentos, se bloquea la cuenta
                user.bloqueado = True

                # Se imprime el mensaje correspondiente
                print("\n¡Se bloqueó la cuenta! ❌")

                # Se espera que el usuario presione cualquier tecla para continuar
                input("\nPresione cualquier tecla para continuar...")

                # Se retorna el Menú Inicial
                return

    # Si no se encuenra el correo ingresado, se imprime el mensaje correspondiente
    print("\n¡No se encontró el correo ingresado! ❌")

    # Se espera que el usuario presione cualquier tecla para continuar
    input("\nPresione cualquier tecla para continuar...")
        
##############################

####1.2.FUNCION NUEVO USUARIO####
def nuevo_usuario():

    # While que se utiliza para validar la variable "correo"
    while True:

        # Se solicita al usuario ingresar su correo
        correo = input("\nIngresar correo: ").strip().lower()

        # Se valida el correo ingresado
        correo_valido = validar_correo(correo)

        # Se evalúa el valor de la variable "correo_valido"
        match correo_valido:

            # Si es "reintentar"
            case "reintentar":
                # Se limpía la pantalla
                limpiar_pantalla()
                # Se pasa a la siguien te iteración del while que valida la variable "correo"
                continue
            
            # Si es "salir"
            case "salir":
                # Se regresa al Menú Inicial
                return
            
            # Si es "correcto"
            case "correcto":
                # Se sale del while que valida la variable "correo"
                break

    # Se verifica si el correo ingresado ya se encuentra registrado
    for user in tabla_usuarios:
        # Si el correo ingresado por el usuario ya se encuentra registrado, entonces se retorna al menú inicial
        if (user.correo).lower() == correo.lower():
            print("\nEl correo ingresado ya se encuentra registrado ❌\n")
            input("Presione cualquier tecla para continuar...")
            return

    # La validación de la contraseña se realiza mediante un bucle while
    while True:

        # Se solicita al usuario ingresar su contraseña
        contrasena = getpass.getpass("Ingresar contraseña: ")

        # Se envía la contraseña introducida por el usuario a la función validar_contrasena para evaluar su complejidad.
        valida = validar_contrasena(contrasena)

        # Si la función retorna el string "valida", se sale del while
        if valida == "valida":
            break
        # Caso contrario, si la función retorna el string "inicial", se vuelve al menú inicial
        elif(valida == "inicial"):
            return
        #Caso contrario(reintentar), se limpia la pantalla y se repite el bucle
        else:
            limpiar_pantalla()

    # Se define un arreglo para ingresar las tuplas: pregunta, respuesta del usuario
    preguntas_respuestas = []

    # Se utiliza un for para que el usuario pueda ingresar las 3 tuplas de pregunta, respuesta
    for i in range(3):
        # Se solicita al usuario que ingrese una pregunta de seguridad
        pregunta = input(f"\nEscriba pregunta de seguridad {i + 1}: ")
        # Se solicita al usuario que ingrese una respuesta de seguridad
        respuesta = getpass.getpass(f"Escriba respuesta de seguridad {i + 1}: ")
        # Se agrega la tupla pregunta, respuesta ingresada por el usuario a al arreglo preguntas_respuestas
        preguntas_respuestas.append((pregunta, respuesta))
    
    # Se crea el objeto usuario_nuevo con los datos ingresados
    usuario_nuevo = Usuario(
        correo = correo,
        contrasena = contrasena,
        preguntas_respuestas = preguntas_respuestas,
        bloqueado = False,
        rol = "USER"
    )

    # Se agrega el nuevo objeto de usuario al arreglo tabla_usuarios
    tabla_usuarios.append(usuario_nuevo)

    # Se imprime mensaje de confirmación
    print("\n¡Usuario creado de manera exitosa! ✅")

    # Se espera que el usuario presione cualquier tecla para continuar
    input("\nPresione cualquier tecla para continuar...")
####################################

####1.3.FUNCION RECUPERAR CONTRASEÑA####
def recuperar_contrasena():

    # While que se utiliza para validar la variable "correo_ingresado"
    while True:

        #Se pide al usuario que introduzca su correo
        correo_ingresado = input("Ingrese su correo: ").strip().lower()

        # Se valida el correo ingresado
        correo_valido = validar_correo(correo_ingresado)

        # Se evalúa el valor de la variable "correo_valido"
        match correo_valido:

            # Si es "reintentar"
            case "reintentar":
                # Se limpía la pantalla
                limpiar_pantalla()
                # Se pasa a la siguien te iteración del while que valida la variable "correo"
                continue
            
            # Si es "salir"
            case "salir":
                # Se regresa al Menú Inicial
                return
            
            # Si es "correcto"
            case "correcto":
                # Se sale del while que valida la variable "correo"
                break

    #Se busca el correo ingresado en la "tabla_usuarios"
    for user in tabla_usuarios:
        # Si se encuentra el usuario
        if user.correo == correo_ingresado:

            print("\n¡Usuario encontrado!✅ Responda las siguientes preguntas de seguridad: \n")
            
            # Se solicita al usuario contestar de manera correcta las 3 preguntas de seguridad
            for pregunta, respuesta in user.preguntas_respuestas:
                respuesta_usuario = getpass.getpass(f"{pregunta}\n")
                # Si contesta de manera errónea alguna pregunta de seguridad
                if respuesta_usuario != respuesta:
                    print("Respuesta Incorreta ❌\n")
                    input("Presione cualquier tecla para continuar...")
                    # Se retorna al menú inicial
                    return
                # Si el usuario contesta de manera correcta las 3 preguntas de seguridad, entonces se le solicita una nueva contraseña
                else:
                    print("Respuesta Correcta ✅\n")
            
            print("Ha contestado de manera correcta todas las preguntas ✅\n")

            # La validación de la contraseña se realiza mediante un bucle while
            while True:

                # Se solicita al usuario ingresar una contraseña nueva
                password_nueva = getpass.getpass("Ingrese una contraseña nueva: ")

                # Se envía la contraseña introducida por el usuario a la función validar_contrasena para evaluar su complejidad.
                valida = validar_contrasena(password_nueva)

                # Si la función retorna el string "valida", se sale del while
                if valida == "valida":
                    break
                # Caso contrario, si la función retorna el string "inicial", se vuelve al menú inicial
                elif(valida == "inicial"):
                    return
                #Caso contrario(reintentar), se limpia la pantalla y se repite el bucle
                else:
                    limpiar_pantalla()

            # Se actualiza la contraseña del usuario
            user.contrasena = password_nueva

            # Se imprime mensaje de éxito
            print(f"\n¡Contraseña actualizada! ✅")

            # Se solicita al usuario presionar "Enter" para continuar
            input("\nPresione cualquier tecla para continuar...")

            # Se retorna al menú inicial
            return

    # Si no se encuentra al usuario en el arreglo "tabla_usuarios"
    print("\nNo se encontró el usuario ❌\n")

    # Se imprime el mensaje de error correspondiente
    input("Presione cualquier tecla para continuar...")
####################################

# ╔══════════════════════════════════════════════════════════╗
# ║              FIN FUNCIONES MENÚ INICIAL                  ║
# ╚══════════════════════════════════════════════════════════╝



# ╔══════════════════════════════════════════════════════════╗
# ║              FUNCIONES MENÚ DEL SISTEMA                  ║
# ╚══════════════════════════════════════════════════════════╝

####2.FUNCION MENU DEL SISTEMA####
def menu_sistema(correo_usuario):

    while True:

        # Se limpia la pantalla
        limpiar_pantalla()

        # Se muestra el Menú del Sistema
        print("====MENU DEL SISTEMA - MilyVet====")
        print("1. Registrar Mascota")
        print("2. Registrar Cita")
        print("3. Cambiar Contraseña")
        print("4. Registrar Atención (VETERINARIO)")
        print("5. Pagar cita")
        print("6. Cerrar Sesión")

        # Se pide al usuario que ingrese una opción
        opcion = int(input("Ingrese una opción: "))

        # Se evalúa la opción ingresada en el Menú del Sistema
        match opcion:

            # REGISTRAR MASCOTA
            case 1:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se ejecuta función registrar_mascota
                registrar_mascota(correo_usuario)

            # REGISTRAR CITA
            case 2:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se ejecuta función registrar_cita
                registrar_cita(correo_usuario)

            # CAMBIAR CONTRASEÑA
            case 3:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se ejecuta función cambiar_contrasena
                cambiar_contrasena(correo_usuario)

            # REGISTRAR ATENCIÓN
            case 4:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se ejecuta función registrar_atencion
                registrar_atencion(correo_usuario)

            # PAGAR CITA
            case 5:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se ejecuta función pagar_cita
                pagar_cita(correo_usuario)

            # SALIR
            case _:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se imprime mensaje de despedida
                print("¡Sesión Cerrada con Éxito! ✅\n")

                # Se espera que el usuario presione cualquier tecla para continuar
                input("Presione cualquier tecla para continuar...")

                # Se sale del bucle
                break

################################

 ####2.1.FUNCION REGISTRAR MASCOTA####
def registrar_mascota(correo):

    errores = 0

    def validar_errores():
        nonlocal errores

        # Se incrementa el contador de errores
        errores += 1

        # Si el contador de errores es mayor a 3
        if errores > 3:
            # Se muetra el mensaje de error respectivo
            print("Demasiados intentos ❌")

            # Se solicita al usuario presionar "Enter" para continuar
            input("\nPresione cualquier tecla para continuar...")

            # Retorna True
            return True
        
        else:
            # Retorna False
            return False

    # Se utiliza un while para introducir los datos de la mascota
    while True:

        # Se ingresa el nombre de la mascota
        nombre = input("Ingrese nombre de la mascota: ").strip().capitalize()

        # Se ingresa el sexo de la mascota
        while True:

            # Se solicita ingresar el sexo de la mascota, se quitan los espacios en blanco adelante y atras del valor ingresado, y se coloca en mayúscula
            sexo = input("Ingrese sexo Macho(M) ó Hembra(H): ").strip().upper()

            # Se evalúa el valor ingresado
            match sexo:

                # Si el valor ingresado es "M" entonces se establece el valor de la variable "sexo" a "Macho"
                case "M":
                    sexo = "Macho"
                    errores = 0
                    # Se sale del while
                    break

                # Si el valor ingresado es "H" entonces se establece el valor de la variable "sexo" a "Hembra"
                case "H":
                    sexo = "Hembra"
                    errores = 0
                    # Se sale del while
                    break

                # Si el valor ingresado no es "M" ni "H", se muestra un mensaje de error
                case _:
                    print("Valor ingresado inválido ❌")

                    if validar_errores(): return

        # Se ingresa la especie de la mascota
        while True:

            # Se solicita ingresar la especie de la mascota, se quitan los espacios en blanco adelante y atras del valor ingresado, y se coloca en mayúscula
            especie = input("Ingrese especie Perro(P), Gato(G), Ave(A), Conejo(C) u Otro(O): ").strip().upper()

            # Se evalúa el valor ingresado
            match especie:
                # Si el valor ingresado es "P" entonces se establece el valor de la variable "especie" a "Perro"
                case "P":
                    especie = "Perro"
                    errores = 0
                    # Se sale del while
                    break
                
                # Si el valor ingresado es "G" entonces se establece el valor de la variable "especie" a "Gato"
                case "G":
                    especie = "Gato"
                    errores = 0
                    # Se sale del while
                    break
                
                # Si el valor ingresado es "A" entonces se establece el valor de la variable "especie" a "Ave"
                case "A":
                    especie = "Ave"
                    errores = 0
                    # Se sale del while
                    break

                # Si el valor ingresado es "C" entonces se establece el valor de la variable "especie" a "Conejo"
                case "C":
                    especie = "Conejo"
                    errores = 0
                    # Se sale del while
                    break
                
                # Si el valor ingresado es "O" entonces se establece el valor de la variable "especie" a "Otro"
                case "O":
                    especie = "Otro"
                    errores = 0
                    # Se sale del while
                    break
                
                # Si el valor ingresado no es ninguno de los solicitados, entonces se muestra el mensaje de error correspondiente
                case _:
                    print("Valor ingresado inválido ❌")

                    if validar_errores(): return

        # Se ingresa la raza de la mascota
        raza = input("Ingrese raza: ").strip().capitalize()

        # Se ingresa la fecha de nacimiento de la mascota
        while True:

            # Se solicita ingresar la fecha de nacimiento de la mascota en el formato dd/mm/yyyy, se quitan los espacios en blanco adelante y atras del valor ingresado
            fecha_nacimiento = input("Ingrese fecha de nacimiento (dd/mm/yyyy) :").strip()

            # Se valida que la fecha ingresada tenga el formato dd/mm/yyyy
            try:
                fecha_valida = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

            # Si la validación arroja un error, entonces se muestra el mensaje de error respectivo y se vuelve al inicio del while
            except ValueError:
                print("Formato de fecha inválido ❌. Use dd/mm/yyyy (Ejemplo: 04/07/2025) y asegúrese de que la fecha exista.")

                if validar_errores(): return

                continue  
            
            # Si la fecha ingresada es en el futuro, se muestra el mensaje de error respectivo y se vuelve al inicio del while
            if fecha_valida > datetime.now():
                print("La fecha de nacimiento no puede ser en el futuro ❌.")

                if validar_errores(): return

                continue 
            
            # Si la fecha ingresada pasa por todas las validaciones, se sale del while
            errores = 0
            break

        # Se ingresa el peso de la mascota en Kg
        while True:

            # Se solicita ingresar el peso de la mascota en Kg
            try:
                peso_kg = float(input("Ingrese peso en Kg: ").strip())

                # Si el peso es menor ó igual a cero, entonces se muestra el mensaje de error correspondiente
                if peso_kg <= 0:
                    print("El peso debe ser mayor a 0 ❌.")

                    if validar_errores(): return
                
                # Si el peso peso es mayor a cero, se guarda el peso ingresado como string en formato de 2 decimales y se sale del while
                else:
                    peso_kg = f"{peso_kg:.2f}"
                    errores = 0
                    break
            
            # Si el peso ingresado no es un número, se muestra el mensaje de error respectivo
            except ValueError:
                print("Ingrese un número válido (Ej: 25.50) ❌.")

                if validar_errores(): return
        
        # Se crea el nuevo objeto mascota con los valores ingresados
        mascota_nueva = Mascota(
            id = generar_id_mascota(especie),
            correo_dueno = correo,
            nombre = nombre,
            sexo = sexo,
            especie = especie,
            raza = raza,
            fecha_nacimiento = fecha_nacimiento,
            peso_kg = peso_kg
        )

        # Se limpia la pantalla
        limpiar_pantalla()

        # Se muestra el resumen de la nueva mascota
        print("####RESUMEN DE NUEVA MASCOTA####")
        print(f"\nID-Mascota: {mascota_nueva.id}")
        print(f"\nCorreo Dueño: {mascota_nueva.correo_dueno}")
        print(f"\nNombre de Mascota: {mascota_nueva.nombre}")
        print(f"\nSexo: {mascota_nueva.sexo}")
        print(f"\nEspecie: {mascota_nueva.especie}")
        print(f"\nRaza: {mascota_nueva.raza}")
        print(f"\nFecha de Nacimiento: {mascota_nueva.fecha_nacimiento}")
        print(f"\nPeso: {mascota_nueva.peso_kg} Kg")

        # Se usa un while para validar la variable "confirmar"
        while True:
            # Se solicita al usuario indicar si los datos de su mascota son correctos
            confirmar = input("\n¿Los datos de la mascota son correctos? Sí(S) No(N): ").strip().lower()

            # Se evalua el valor de la variable "confirmar"
            match confirmar:
                
                # Si el valor es 's'
                case 's':
                    # Se agrega la nueva mascota al arreglo tabla_mascotas
                    tabla_mascotas.append(mascota_nueva)

                    # Se actualiza el diccionario "contador_id"
                    actualizar_contador_id(especie)

                    # Se imprime mensaje de confirmación
                    print("\n¡Mascota registrada con éxito! ✅")

                    # Se sale del while que valida la variable "confirmar"
                    break

                # Si el valor es 'n'
                case 'n':
                    # Se limpia la pantalla
                    limpiar_pantalla()

                    # Se sale del while que valida la variable "confirmar"
                    break

                case _:
                    # Se muestra el mensaje de error correspondiente
                    print("Valor ingresado inválido ❌")

                    # Se valida que la cantidad de errores sea menor o igual a 3
                    if validar_errores(): return

                    # Se vuelve a solicitar el valor
                    continue

        
        # Si el valor de la variable "confirmar" en 'n'
        if confirmar == 'n':
            # Se continua con la siguiente iteración del while que solicita los datos de la mascota
            continue

        # while de validación para variable "nuevo_registro"
        while True:

            # Se consulta al usuario si desea registrar otra mascota
            nuevo_registro = input("\n¿Registrar otra mascota? Si(S) No(N): ").strip().upper()

            # Se evalua el valor ingresado
            match nuevo_registro:

                # Si el valor ingresado es "S"
                case "S":
                    # Se limpia la pantalla
                    limpiar_pantalla()
                    # La variable "errores" se establece en 0
                    errores = 0
                    # Se sale del while de validación y se vuelve a repetir el proceso
                    break
                
                # Si el valor ingresado es "N"
                case "N":
                    # La variable "errores" se establece en 0
                    errores = 0
                     # Se sale del while de validación y se vuelve a repetir el proceso
                    return

                # Si el valor ingresado no es "S" ni "N"
                case _:
                    # Se muestra el mensaje de error correspondiente
                    print("Valor ingresado inválido ❌")

                    # Se valida que la cantidad de errores sea menor o igual a 3
                    if validar_errores(): return

                    # Se vuelve a solicitar el valor
                    continue
#################################

####2.2.FUNCION REGISTRAR CITA####

def registrar_cita(correo_usuario):

    errores = 0

    def validar_errores():
        nonlocal errores

        errores += 1

        if errores >= 3:
            print("\nDemasiados intentos ❌")
            input("Presione Enter para continuar...")
            return True

        return False

    while True:

        limpiar_pantalla()

        print("===== REGISTRAR CITA =====\n")

        # Buscar mascotas del usuario logueado
        mascotas_usuario = []

        for mascota in tabla_mascotas:
            if mascota.correo_dueno == correo_usuario:
                mascotas_usuario.append(mascota)

        # Validar que tenga mascotas
        if len(mascotas_usuario) == 0:
            print("No tiene mascotas registradas ❌")
            input("\nPresione Enter para continuar...")
            return

        print("Seleccione una mascota:\n")

        for i, mascota in enumerate(mascotas_usuario):
            print(f"{i+1}. {mascota.nombre}")
            print(f"   ID: {mascota.id}")
            print(f"   Especie: {mascota.especie}")
            print(f"   Raza: {mascota.raza}")
            print("--------------------------------")

        # Seleccionar mascota
        while True:

            try:

                opcion = int(input("Ingrese una opción: "))

                if opcion >= 1 and opcion <= len(mascotas_usuario):

                    mascota_seleccionada = mascotas_usuario[opcion-1]
                    errores = 0
                    break

                else:
                    print("Opción inválida ❌")

                    if validar_errores():
                        return

            except ValueError:

                print("Debe ingresar un número ❌")

                if validar_errores():
                    return

        limpiar_pantalla()

        print("===== REGISTRAR CITA =====\n")

        print("Mascota seleccionada")
        print("---------------------------")
        print(f"ID: {mascota_seleccionada.id}")
        print(f"Nombre: {mascota_seleccionada.nombre}")
        print(f"Especie: {mascota_seleccionada.especie}")
        print(f"Raza: {mascota_seleccionada.raza}")
        print()

        
        #============================
        # SELECCIONAR ESPECIALIDAD
        #============================

        while True:

            print("Especialidades disponibles")
            print("1. Medicina General")
            print("2. Vacunación")
            print("3. Desparasitación")
            print("4. Cirugía")

            opcion = input("\nSeleccione una opción: ").strip()

            match opcion:

                case "1":
                    especialidad = "Medicina General"
                    errores = 0
                    break

                case "2":
                    especialidad = "Vacunación"
                    errores = 0
                    break

                case "3":
                    especialidad = "Desparasitación"
                    errores = 0
                    break

                case "4":
                    especialidad = "Cirugía"
                    errores = 0
                    break

                case _:
                    print("Opción inválida ❌")

                    if validar_errores():
                        return

        limpiar_pantalla()

        print("===== REGISTRAR CITA =====\n")

        print(f"Mascota: {mascota_seleccionada.nombre}")
        print(f"Especialidad: {especialidad}\n")

        #============================
        # MOSTRAR MÉDICOS
        #============================

        medicos_disponibles = []

        for medico in tabla_medicos:

            if medico["especialidad"] == especialidad:
                medicos_disponibles.append(medico)

        print("Médicos disponibles:\n")

        for i, medico in enumerate(medicos_disponibles):
            print(f"{i+1}. {medico['nombre']}")

        while True:

            try:

                opcion = int(input("\nSeleccione un médico: "))

                if opcion >= 1 and opcion <= len(medicos_disponibles):

                    medico_seleccionado = medicos_disponibles[opcion-1]["nombre"]
                    errores = 0
                    break

                else:

                    print("Seleccione una opción válida ❌")

                    if validar_errores():
                        return

            except ValueError:

                print("Debe ingresar un número ❌")

                if validar_errores():
                    return

        #============================
        # FECHA
        #============================

        while True:

            fecha = input("\nIngrese la fecha (dd/mm/yyyy): ").strip()

            try:

                fecha_valida = datetime.strptime(fecha,"%d/%m/%Y")

                if fecha_valida.date() < datetime.now().date():

                    print("No puede registrar citas en fechas pasadas ❌")

                    if validar_errores():
                        return

                    continue

                errores = 0
                break

            except ValueError:

                print("Formato de fecha incorrecto ❌")

                if validar_errores():
                    return

        #============================
        # HORA
        #============================

        while True:

            hora = input("Ingrese la hora (HH:MM): ").strip()

            try:

                hora_valida = datetime.strptime(hora,"%H:%M")

                if hora_valida.hour < 8 or hora_valida.hour >= 18:

                    print("Horario de atención: 08:00 a 18:00 ❌")

                    if validar_errores():
                        return

                    continue

                errores = 0
                break

            except ValueError:

                print("Hora inválida ❌")

                if validar_errores():
                    return
                
        #============================
        # VALIDAR DISPONIBILIDAD
        #============================

        disponible = True

        for cita in tabla_citas:

            if (cita.medico == medico_seleccionado and
                cita.fecha == fecha and
                cita.hora == hora):

                disponible = False
                break

        if disponible == False:

            print("\nEl médico ya tiene una cita registrada en ese horario ❌")
            input("\nPresione Enter para continuar...")
            continue

        #============================
        # MOSTRAR RESUMEN
        #============================

        limpiar_pantalla()

        print("========== RESUMEN DE LA CITA ==========\n")

        print(f"Mascota       : {mascota_seleccionada.nombre}")
        print(f"ID Mascota    : {mascota_seleccionada.id}")
        print(f"Especie       : {mascota_seleccionada.especie}")
        print(f"Especialidad  : {especialidad}")
        print(f"Médico        : {medico_seleccionado}")
        print(f"Fecha         : {fecha}")
        print(f"Hora          : {hora}")
        print("----------------------------------------")

        while True:

            confirmar = input("\n¿Desea confirmar la cita? Si(S) No(N): ").strip().upper()

            match confirmar:

                case "S":

                    nueva_cita = Cita(
                        mascota_seleccionada.id,
                        medico_seleccionado,
                        especialidad,
                        fecha,
                        hora,
                        "Pendiente"
                    )

                    tabla_citas.append(nueva_cita)

                    print("\n¡Cita registrada correctamente! ✅")
                    errores = 0
                    break

                case "N":

                    print("\nRegistro cancelado.")
                    errores = 0
                    break

                case _:

                    print("Opción inválida ❌")

                    if validar_errores():
                        return

        #============================
        # REGISTRAR OTRA CITA
        #============================

        while True:

            opcion = input("\n¿Desea registrar otra cita? Si(S) No(N): ").strip().upper()

            match opcion:

                case "S":

                    errores = 0
                    limpiar_pantalla()
                    break

                case "N":

                    return

                case _:

                    print("Opción inválida ❌")

                    if validar_errores():
                        return

        if opcion == "S":
            continue


##################################

####2.3.FUNCION CAMBIAR CONTRASEÑA####
def cambiar_contrasena(correo_usuario):

    #Se busca el correo del usuario en la "tabla_usuarios"
    for user in tabla_usuarios:
        # Cuando se encuentra al objeto corespondiente
        if user.correo == correo_usuario:

            # La validación de la contraseña se realiza mediante un bucle while
            while True:

                # Se solicita al usuario ingresar una contraseña nueva
                password_nueva = getpass.getpass("Ingrese una contraseña nueva: ")

                # Se envía la contraseña introducida por el usuario a la función validar_contrasena para evaluar su complejidad.
                valida = validar_contrasena(password_nueva)

                # Si la función retorna el string "valida", se sale del while
                if valida == "valida":
                    break
                # Caso contrario, si la función retorna el string "inicial", se vuelve al menú del sistema
                elif(valida == "inicial"):
                    return
                #Caso contrario(reintentar), se limpia la pantalla y se repite el bucle
                else:
                    limpiar_pantalla()

            # Se actualiza la contraseña del usuario
            user.contrasena = password_nueva

            # Se imprime mensaje de éxito
            print(f"\n¡Contraseña actualizada! ✅")

            # Se solicita al usuario presionar "Enter" para continuar
            input("\nPresione cualquier tecla para continuar...")

            # Se retorna al menú del sistema
            return
##################################

####2.4.FUNCION REGISTRAR ATENCIÓN####
def registrar_atencion(correo):

    # Se inicializa la variable errores en 0
    errores = 0

    # Se define la función anidada "validar_errores"
    def validar_errores():
        # Se indica que la variable errores es no local (está fuera de la función validar_errores)
        nonlocal errores

        # Se incrementa el contador de errores
        errores += 1

        # Si el contador de errores es mayor a 3
        if errores > 3:
            # Se muestra el mensaje de error correspondiente
            print("Demasiados intentos ❌")

            # Se solicita al usuario presionar cualquier tecla para continuar
            input("\nPresione cualquier tecla para continuar...")

            # Retorna True
            return True
        
        # Si el contador de errores es menor ó igual a 3
        else:
            # Retorna False
            return False
        
    # Se valida que el usuario logueado tenga el rol de Veterinario (VET)
    # Se busca el correo del usuario en la "tabla_usuarios"
    for user in tabla_usuarios:
        # Cuando se encuentra al objeto corespondiente
        if user.correo == correo:
            # Si el usuario no tiene acceso al módulo
            if user.rol != "VET":
                # Se imprime el mensaje de error correspondiente
                print("¡No tiene acceso al módulo registrar atención! ❌")

                # Se espera que el usuario presione cualquier tecla para continuar
                input("\nPresione cualquier tecla para continuar...")

                # Se retorna al menú del sistema
                return

    # Se usa un while para volver a registrar otra atención, de ser necesario
    while True:

        # Se usa un while para validar el ID de mascota ingresado
        while True:

            # Se solicita ingresar el ID de la mascota, se quitan los espacios en blanco adelante y atras del valor ingresado, y se coloca en mayúscula
            id_mascota = input("\nIngrese el ID de la mascota a atender: ").strip().upper()

            # Se verifica si el ID de mascota ingresado existe en "tabla_mascotas"
            buscar_id_mascota = next((m for m in tabla_mascotas if m.id == id_mascota), None)

            # Si no se encuentra el ID de mascota
            if buscar_id_mascota is None:
                # Se muestra el mensaje de error correspondiente
                print("ID de mascota inválido ❌")

                # Se validan la cantidad de errores
                if validar_errores(): return

                # Se continua con la siguiente iteración del while que valida la variable "id_mascota"
                continue

            # Se busca si la mascota ingresada tiene citas agendadas (la fecha y hora de la cita debe ser mayor a la fecha y hora actual - Las citas pasadas no se muestran)
            citas_mascota = [c for c in tabla_citas if (c.id_mascota == id_mascota and datetime.strptime(f"{c.fecha} {c.hora}", "%d/%m/%Y %H:%M") >= datetime.now())]

            # Si la mascota no tiene citas agendadas, se muestra el mensaje de error correspondiente
            if citas_mascota is None:
                # Se muestra el mensaje de error correspondiente
                print("La mascota no tiene citas agendadas ❌")

                # Se validan la cantidad de errores
                if validar_errores(): return

                # Se continua con la siguiente iteración del while que valida la variable "id_mascota"
                continue

            # Si el ID de mascota pasa todas las validaciones
            # La cantidad de errores se restablece a 0
            errores = 0
            # Se sale del while que valida la variable "id_mascota"
            break

        # Se usa un while para validar el número de cita ingresado
        while True:
        
            # Se pide al usuario seleccionar la cita que se desea atender:
            print("Seleccione la cita que desea atender:\n")

            # Se recorren los índices "i" y elementos "cita"  de la lista "citas_mascota"
            for i, cita in enumerate(citas_mascota):

                # Se obtiene el monto asociado a cada cita
                monto = precios_especialidad.get(cita.especialidad, 50.00)

                # Se imprime el resumen de cada cita
                print(f"{i+1}. Mascota: {cita.id_mascota} | {cita.especialidad} | {cita.fecha} {cita.hora} | S/ {monto:.2f} | {cita.estado}")

            # Se imprime caracteres estéticos
            print("--------------------------------")

            # Se usa un try - except para validar la variable "opcion"
            try:
                # Se solicita al usuario ingresar una opión
                opcion = int(input("\nIngrese una opción: "))

                # Si la opción ingresada es válida
                if 1 <= opcion <= len(citas_mascota):

                    # Se selecciona la cita que corresponde a la opión ingresada
                    cita_seleccionada = citas_mascota[opcion - 1]

                    # Si el estado de la cita es "Pendiente"
                    if cita_seleccionada.estado == "Pendiente":

                        # Se imprime el mensaje de advertencia correspondiente
                        print("\nPrimero debe pagar la cita antes de atenderla ⚠️")

                        # Se usa una while para validar la variable "pagar_cita"
                        while True:
                            # Se solicita al usuario ingresar una opción
                            pagar_cita = input("\n¿Pagar Ahora? Sí(S) No(N): ").strip().upper()

                            # Si el valor de la variable "pagar_cita" es "S" ó "N"
                            if pagar_cita == 'S' or pagar_cita == 'N':
                                # Se sale del while que valida la variable "pagar_cita"
                                break
                            
                            # Si el valor de la variable "pagar_cita" es diferente a "S" y "N"
                            else:
                                # Se imprime el mensaje de error correspondiente
                                print("Opción inválida ❌")
                                # Se evalua la cantidad de errores
                                if validar_errores(): return
                                # Se continua con la siguiente iteración del while que valida la variable "pagar_cita"
                                continue
                        
                        # Se evalua el valor de la variable "pagar_cita"
                        match pagar_cita:
                            # Si el valor es 'S'
                            case 'S':
                                # Se ejecuta la función "pagar_cita" y el resultado se guarda en la variable "estado_cita"
                                estado_cita = pagar_cita(cita_seleccionada)
                                # Si el pago fue exitoso
                                if estado_cita == "Pagado":
                                    # Se limpia la pantalla
                                    limpiar_pantalla()
                                    # Se sale del while que valida el número de cita ingresado
                                    break
                                # Si el pago no fue exitoso
                                else:
                                    # Se limpia la pantalla
                                    limpiar_pantalla()
                                    # Se continua a la siguiente iteración del while que valida el número de cita ingresado
                                    continue

                            # Si el valor es 'N'
                            case 'N':
                                # Se limpia la pantalla
                                limpiar_pantalla()
                                # Se continua a la siguiente iteración del while que valida el número de cita ingresado
                                continue
                    
                    # Si el estado de la cita es "Pagado"
                    else:
                        # Se limpia la pantalla
                        limpiar_pantalla()
                        # La cantidad de errores se restablece a 0
                        errores = 0
                        # Se sale del while que valida el número de cita ingresado
                        break

                # Si la opción ingresada es inválida
                else:
                    # Se imprime el mensaje de error correspondiente
                    print("Opción inválida ❌")
                    # Se evalua la cantidad de errores
                    if validar_errores(): return
                    # Se continua a la siguiente iteración del while que valida el número de cita ingresado
                    continue
            
            # Si la opción ingresada no cunple con el formato int
            except ValueError:
                # Se imprime el mensaje de error correspondiente
                print("Debe ingresar un número ❌")
                # Se evalua la cantidad de errores
                if validar_errores(): return
                # Se continua a la siguiente iteración del while que valida el número de cita ingresado
                continue
        
        # Su usa un while para confirmar la atención (se vuelve a solicitar motivo, diagnóstico y tratamiento)
        while True:
            # Se usa un while para validar la variable "motivo"
            while True:
                # Se ingresa el motivo de la atención
                motivo = input("Ingrese motivo de la atención (min. 20 caracteres): ").strip().capitalize()

                # Si el motivo ingresado es menor de 20 caracteres
                if len(motivo) < 20:
                    # Se imprime el mensaje de error correspondiente
                    print("El campo Motivo debe tener una longitud mínima de 20 caracteres ❌")
                    # Se evalua la cantidad de errores
                    if validar_errores(): return
                    # Se continua con la siguiente iteración del while que valida la variable "motivo"
                    continue
                # Si el diagnóstico ingresado es mayor o igual a 20 caracteres
                else:
                    # Se sale del while que valida la variable "motivo"
                    break
            
            # Se usa un while para validar la variable "diagnostico"
            while True:
                # Se ingresa el diagnóstico de la mascota
                diagnostico = input("Ingrese diagnóstico (min. 20 caracteres): ").strip().capitalize()

                # Si el diagnóstico ingresado es menor de 20 caracteres
                if len(diagnostico) < 20:
                    # Se imprime el mensaje de error correspondiente
                    print("El campo Diagnóstico debe tener una longitud mínima de 20 caracteres ❌")
                    # Se evalua la cantidad de errores
                    if validar_errores(): return
                    # Se continua con la siguiente iteración del while que valida la variable "diagnostico"
                    continue
                # Si el diagnóstico ingresado es mayor o igual a 20 caracteres
                else:
                    # Se sale del while que valida la variable "diagnostico"
                    break
            
            # Se usa un while para validar la variable "tratamiento"
            while True:
                # Se ingresa el tratamiento indicado
                tratamiento = input("Ingrese tratamiento (min. 20 caracteres): ").strip().capitalize()

                # Si el tratamiento ingresado es menor de 20 caracteres
                if len(tratamiento) < 20:
                    # Se imprime el mensaje de error correspondiente
                    print("El campo Tratamiento debe tener una longitud mínima de 20 caracteres ❌")
                    # Se evalua la cantidad de errores
                    if validar_errores(): return
                    # Se continua con la siguiente iteración del while que valida la variable "tratamiento"
                    continue
                # Si el tratamiento ingresado es mayor o igual a 20 caracteres
                else:
                    # Se sale del while que valida la variable "tratamiento"
                    break

            # Se registra la fecha de atención automáticamente con la fecha actual del sistema
            fecha_atencion = datetime.now().strftime("%d/%m/%Y")

            # Se genera el número e ID de la nueva atención
            num_nueva_atencion, id_nueva_atencion = generar_id_atencion()

            # Se crea el nuevo objeto atencion con los valores ingresados
            atencion_nueva = Atencion(
                id_atencion = id_nueva_atencion,
                correo_dueno = correo,
                id_mascota = id_mascota,
                motivo = motivo,
                diagnostico = diagnostico,
                tratamiento = tratamiento,
                precio_soles = f"{monto:.2f}",
                fecha_atencion = fecha_atencion  
            )

            # Se obtiene la mascota en base a su ID
            mascota = next(m for m in tabla_mascotas if m.id == id_mascota)

            # Se muestra el resumen de la atención
            print("####RESUMEN DE ATENCIÓN###")
            print(f"\nID-Atencion: {id_nueva_atencion}")
            print(f"\nID-Mascota: {id_mascota}")
            print(f"\nCorreo Dueño: {correo}")
            print(f"\nNombre de Mascota: {mascota.nombre}")
            print(f"\nSexo: {mascota.sexo}")
            print(f"\nEspecie: {mascota.especie}")
            print(f"\nRaza: {mascota.raza}")
            print(f"\nFecha de Nacimiento: {mascota.fecha_nacimiento}")
            print(f"\nPeso: {mascota.peso_kg} Kg")
            print(f"\nMotivo: {motivo}")
            print(f"\nDiagnóstico: {diagnostico}")
            print(f"\nTratamiento: {tratamiento}")
            print(f"\nPrecio: S/{monto:.2f}")

            # Se usa un while para validar la variable "confirmar_atencion"
            while True:
                # Se solicita al usuario confirmar la atención
                confirmar_atencion = input("\n¿Confirmar Atención? Si(S) No(N): ").strip().upper()

                # Si el valor de la variable "confirmar_atencion" es diferente a "S" y "N"
                if confirmar_atencion != 'S' and confirmar_atencion != 'N':
                    # Se imprime el mensaje de error correspondinete
                    print("\nOpción inválida ❌")
                    # Se evalua la cantidad de errores
                    if validar_errores(): return
                    # Se pasa a la siguiente iteración del while que valida la variable "confirmar_atencion"
                    continue

                # Si el valor de la variable "confirmar_atencion" es "s" ó "n"
                else:
                    # La cantidad de errores se restablece a 0
                    errores = 0
                    # Se sale del while que valida la variable "confirmar_atencion"
                    break

            # Se evalúa el valor de la vatiable "confirmar_atencion"
            match confirmar_atencion:

                # Si el valor de la variable es "S"
                case 'S':
                    # Se sale del while que se utiliza para confirmar la atención (no se vuelve a solicitar motivo, diagnóstico y tratamiento)
                    break

                # Si el valor de la variable es "N"
                case 'N':
                    # Se limpia la pantalla
                    limpiar_pantalla()
                    # Se continua con la siguiente iteración del while que se utiliza para confirmar la atención (se vuelve a solicitar motivo, diagnóstico y tratamiento)
                    continue

        # Se agrega la nueva atención al arreglo tabla_atenciones
        tabla_atenciones.append(atencion_nueva)

        # Se actualiza el número de atenciones en el diccionario "atencion_id"
        atencion_id["ATN"] = num_nueva_atencion

        # Se imprime mensaje de confirmación
        print(f"\n¡Atención registrada con éxito! ✅ (ID: {atencion_nueva.id_atencion})")

        # while de validación para variable "nuevo_registro"
        while True:

            # Se consulta al usuario si desea registrar otra atención
            nuevo_registro = input("\n¿Registrar otra atención? Si(S) No(N): ").strip().upper()

            # Se evalua el valor de la variable "nuevo_registro"
            match nuevo_registro:

                # Si el valor ingresado es "S", 
                case "S":
                    # La cantidad de errores se restablece a 0
                    errores = 0
                    # Se sale del while de validación de la variable "nuevo_registro" y se vuelve a repetir el proceso (while para volver a registrar otra atención)
                    break

                # Si el valor ingresado es "N"
                case "N":
                    # La cantidad de errores se restablece a 0
                    errores = 0
                    # Se calcula el total de atenciones y el total de ingresos del día
                    total_atenciones, total_ingresos = resumen_dia()
                    # Se muestra el resumen del día
                    print("\n####RESUMEN DEL DÍA###")
                    print(f"\nTotal de Atenciones: {total_atenciones}")
                    print(f"\nTotal de Ingresos: S/{total_ingresos}")

                    # Se espera que el usuario presione cualquier tecla para continuar
                    input("\nPresione cualquier tecla para continuar...")
                    
                    # Se sale de la función registrar_atencion y se retorna el menú del sistema
                    return

                # Si el valor ingresado no es "S" ni "N"
                case _:
                    # Se imprime el mensaje de error correspondinete
                    print("Valor ingresado inválido ❌")
                    # Se evalua la cantidad de errores
                    if validar_errores(): return
                    # Se vuelve a solicitar el valor de la variable "nuevo_registro"
                    continue
######################################

####2.5.FUNCION PAGAR CITA####

#####FUNCION PAGAR CITA######
def pagar_cita(correo_usuario, cita_seleccionada = None):

    errores = 0

    def validar_errores():
        nonlocal errores
        errores += 1
        if errores >= 3:
            print("\nDemasiados intentos ❌")
            input("Presione Enter para continuar...")
            return True
        return False

    
    while True:

        if correo_usuario != None and cita_seleccionada == None:
            limpiar_pantalla()
            print("===== PAGAR CITA =====\n")

            # IDs de las mascotas del usuario logueado
            ids_mascotas_usuario = []
            for mascota in tabla_mascotas:
                if mascota.correo_dueno == correo_usuario:
                    ids_mascotas_usuario.append(mascota.id)

            # Se buscan las citas pendientes de pago del usuario
            citas_pendientes = []
            for cita in tabla_citas:
                if cita.id_mascota in ids_mascotas_usuario and cita.estado == "Pendiente":
                    citas_pendientes.append(cita)

            if len(citas_pendientes) == 0:
                print("No tiene citas pendientes de pago ❌")
                input("\nPresione Enter para continuar...")
                return

            print("Seleccione la cita que desea pagar:\n")
            for i, cita in enumerate(citas_pendientes):
                monto = precios_especialidad.get(cita.especialidad, 50.00)
                print(f"{i+1}. Mascota: {cita.id_mascota} | {cita.especialidad} | {cita.fecha} {cita.hora} | S/ {monto:.2f}")
            print("--------------------------------")

            # Seleccionar cita
            while True:
                try:
                    opcion = int(input("Ingrese una opción: "))
                    if 1 <= opcion <= len(citas_pendientes):
                        cita_seleccionada = citas_pendientes[opcion - 1]
                        errores = 0
                        break
                    else:
                        print("Opción inválida ❌")
                        if validar_errores(): return
                except ValueError:
                    print("Debe ingresar un número ❌")
                    if validar_errores(): return

        monto_a_pagar = precios_especialidad.get(cita_seleccionada.especialidad, 50.00)

        limpiar_pantalla()
        print("===== PAGAR CITA =====\n")
        print(f"Mascota      : {cita_seleccionada.id_mascota}")
        print(f"Especialidad : {cita_seleccionada.especialidad}")
        print(f"Fecha / Hora : {cita_seleccionada.fecha} {cita_seleccionada.hora}")
        print(f"Monto a pagar: S/ {monto_a_pagar:.2f}\n")

        #============================
        # SELECCIONAR MÉTODO DE PAGO
        #============================
        while True:
            print("Métodos de pago disponibles")
            print("1. Tarjeta de crédito/débito")
            print("2. Yape/Plin")
            print("3. Efectivo (pago en caja)")

            metodo_opcion = input("\nSeleccione una opción: ").strip()

            match metodo_opcion:
                case "1":
                    pago_exitoso = pagar_con_tarjeta(monto_a_pagar)
                    metodo = "Tarjeta"
                    errores = 0
                    break
                case "2":
                    pago_exitoso = pagar_con_yape_plin(monto_a_pagar)
                    metodo = "Yape/Plin"
                    errores = 0
                    break
                case "3":
                    codigo_pago = pagar_con_efectivo(
                        monto_a_pagar,
                        cita_seleccionada.id_mascota,
                        cita_seleccionada.especialidad,
                        cita_seleccionada.fecha,
                        cita_seleccionada.hora

                    )
                    pago_exitoso = True 
                    metodo ="Efectivo"
                    errores = 0
                    break
                case _:
                    print("Opción inválida ❌")
                    if validar_errores(): return

        #============================
        # REGISTRAR RESULTADO DEL PAGO
        #============================
        if pago_exitoso:

            if metodo == "Efectivo":
                estado_cita = "Pendiente"          # La cita sigue pendiente hasta que pague en caja
                estado_pago = "Pendiente en caja"
            else:
                estado_cita = "Pagado"             # Tarjeta/Yape/Plin se confirman al instante
                estado_pago = "Completado"
                codigo_pago = "" 

            cita_seleccionada.estado = estado_cita

            nuevo_pago = Pago(
                cita_seleccionada.id_mascota,
                cita_seleccionada.medico,
                cita_seleccionada.fecha,
                cita_seleccionada.hora,
                metodo,
                monto_a_pagar,
                estado_pago,
                codigo_pago 
            )

            # Se guarda el código de pago si el método fue efectivo
            nuevo_pago.codigo_pago = codigo_pago

            tabla_pagos.append(nuevo_pago)

            if metodo == "Efectivo":
                print(f"\n¡Código generado con éxito! Preséntelo en caja. ✅")
            else:
                print("\n¡Pago registrado con éxito! ✅")

        else:
            print("\nEl pago no pudo completarse ❌")

        input("\nPresione Enter para continuar...")

        if correo_usuario == None and cita_seleccionada != None:
            return estado_cita

        #============================
        # PAGAR OTRA CITA
        #============================
        while True:
            otro = input("\n¿Desea pagar otra cita? Si(S) No(N): ").strip().upper()
            match otro:
                case "S":
                    errores = 0
                    break
                case "N":
                    return
                case _:
                    print("Opción inválida ❌")
                    if validar_errores(): return
##################################################

####FUNCION PAGAR CON TARJETA ####
def pagar_con_tarjeta(monto):

    errores = 0

    # Validación de variable "numero_tarjeta"
    while True:

        # Número de tarjeta: se valida que tenga 16 dígitos numéricos
        numero_tarjeta = input("\nIngrese número de tarjeta (16 dígitos): ").strip().replace(" ", "")

        if not re.fullmatch(r"\d{16}", numero_tarjeta):
            print("Número de tarjeta inválido ❌. Debe contener 16 dígitos.")
            errores += 1
            if errores >= 3:
                print("Demasiados intentos ❌")
                return False
            continue
        # Se restablece la variable "errores"
        errores = 0
        # Se sale del while de validación
        break
    
    # Validación de variable "vencimiento"
    while True:

        # Fecha de vencimiento en formato MM/AA
        vencimiento = input("Ingrese fecha de vencimiento (MM/AA): ").strip()

        try:
            fecha_venc = datetime.strptime(vencimiento, "%m/%y")

            if fecha_venc.date() < datetime.now().date():

                print("La fecha de vencimiento no puede ser pasada ❌")
                errores += 1
                if errores >= 3:
                    print("Demasiados intentos ❌")
                    return False
                continue
            # Se restablece la variable "errores"
            errores = 0
            # Se sale del while de validación
            break

        except ValueError:
            print("Formato de fecha inválido ❌. Use MM/AA (Ejemplo: 09/27).")
            errores += 1
            if errores >= 3:
                print("Demasiados intentos ❌")
                return False
            continue

    # Validación de variable "cvv"
    while True:
        # CVV oculto con getpass, se valida que tenga 3 dígitos
        cvv = getpass.getpass("Ingrese CVV (3 dígitos): ").strip()

        if not re.fullmatch(r"\d{3}", cvv):
            print("CVV inválido ❌. Debe contener 3 dígitos.")
            errores += 1
            if errores >= 3:
                print("Demasiados intentos ❌")
                return False
            continue
        # Se restablece la variable "errores"
        errores = 0
        # Se sale del while de validación
        break

    # Simulación de autorización del banco (siempre aprobado en esta versión de práctica)
    print(f"\nProcesando pago de S/ {monto:.2f} con tarjeta terminada en {numero_tarjeta[-4:]}...")
    print("Autorización del banco: APROBADA ✅")

    return True
##################################
    
####FUNCION PAGAR CON YAPE/PLIN####
def pagar_con_yape_plin(monto):

    errores = 0

    # Validación de variable "celular"
    while True:

        # Número de celular afiliado a Yape (9 dígitos, empieza con 9)
        celular = input("\nIngrese su número de celular Yape/Plin: ").strip()

        if not re.fullmatch(r"9\d{8}", celular):
            print("Número inválido ❌. Debe tener 9 dígitos y empezar con 9.")
            errores += 1
            if errores >= 3:
                print("Demasiados intentos ❌")
                return False
            continue
        # Se sale del while de validación
        break
    
    # Validación de variable "codigo_generado"
    while True:
        # Se genera el código de confirmación (SIMULACION)
        codigo_generado = f"{random.randint(0, 9999):04d}"

        print(f"\nSe envió una notificación push a Yape ({celular[:3]}****{celular[-3:]}).")
        print(f"Código enviado: {codigo_generado}")  

        # Se le pide al usuario que ingrese el codigo enviado a su app de Yape
        codigo_ingresado = input("Ingrese el código de confirmación de la app (4 dígitos): ").strip()

        if codigo_ingresado != codigo_generado:
            print("Código inválido ❌.")
            errores += 1
            if errores >= 3:
                print("Demasiados intentos ❌")
                return False
            continue
        # Se sale del while de validación
        break

    print(f"\nProcesando pago de S/ {monto:.2f} vía Yape...")
    print("Pago APROBADO ✅")

    return True
###################################
 
####FUNCION PAGAR EN EFECTIVO (GENERA RECIBO PARA CAJA)####
def pagar_con_efectivo(monto, id_mascota, especialidad, fecha, hora):

    # Se genera un código único de 6 dígitos para presentar en caja
    codigo_pago = f"{random.randint(0, 999999):06d}"

    limpiar_pantalla()

    print("========== RECIBO DE PAGO EN EFECTIVO ==========\n")
    print(f"Código de pago : {codigo_pago}")
    print(f"Mascota (ID)    : {id_mascota}")
    print(f"Especialidad    : {especialidad}")
    print(f"Fecha / Hora    : {fecha} {hora}")
    print(f"Monto a pagar   : S/ {monto:.2f}")
    print("-------------------------------------------------")
    print("\nPresente este código en caja para completar su pago.")
    print("Su cita quedará confirmada una vez realizado el pago. ⚠️")

    input("\nPresione Enter para continuar...")

    # Se retorna el código generado para guardarlo en el registro de pago
    return codigo_pago
######################################

##############################

# ╔══════════════════════════════════════════════════════════╗
# ║          FIN FUNCIONES MENÚ DEL SISTEMA                  ║
# ╚══════════════════════════════════════════════════════════╝



# ╔══════════════════════════════════════════════════════════╗
# ║          INICIO DEL PROGRAMA                             ║
# ╚══════════════════════════════════════════════════════════╝

# Se inicia el programa llamando la función "menu_inicial"
menu_inicial()

# ╔══════════════════════════════════════════════════════════╗
# ║          FIN DEL PROGRAMA                                ║
# ╚══════════════════════════════════════════════════════════╝
          





 

        
      









               

         

    














        
               


    

        


      

        

       

     





                 
         




                








         

     
       


    
            
    
     

     
         

    
        



    


    








                    
