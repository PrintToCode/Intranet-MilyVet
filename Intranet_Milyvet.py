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

# ╔══════════════════════════════════════════════════════════╗
# ║                  FIN IMPORTAR LIBRERIAS                  ║
# ╚══════════════════════════════════════════════════════════╝



# ╔══════════════════════════════════════════════════════════╗
# ║                  CONSTRUCCION DE BD                      ║
# ╚══════════════════════════════════════════════════════════╝

#Se crea un diccionario que ayudará a crear el ID al registrar una mascota
contador_id = {
    "CAN": 1
}

#Se crea una lista de usuarios para simular una tabla de BD
tabla_usuarios = []

#Se crea una lista de mascotas para simular una tabla de BD
tabla_mascotas = []

#Se crea la clase usuario
class Usuario:
    def __init__(self, correo, contrasena, preguntas_respuestas, bloqueado, rol):
        self.correo = correo
        self.contrasena = contrasena
        self.preguntas_respuestas = preguntas_respuestas
        self.bloqueado = bloqueado
        self.rol = rol

#Se crea la clase mascota
class Mascota:
    def __init__(self, id, correo_dueno, nombre, sexo, especie, raza, fecha_nacimiento, peso_kg):
        self.id = id
        self.correo_dueno = correo_dueno
        self.nombre = nombre
        self.sexo = sexo
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso_kg

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
        
        # Se solicita al usuario que presione la tecla "Enter" para volver a intentarlo ó "X" para retornar al menú inicial
        opcion = input("\nPresione Enter para volver a interntarlo ó \"X\" para volver al menú inicial...\n ")

    # Si el usuario presiona la tecla "X"
    if opcion.lower() == "x":
        # Se retorna el string "inicial"
        return "inicial"
    else:
        # Caso contrario, se retorna el string "reintentar"
        return "reintentar"

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
                # Se espera que el usuario presione R para continuar o S para salir, elminan los espacios alrededor de la opción ingresada y se convierte a minúscula
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

    # Se evalua la especie ()
    match especie.lower():

        # Si es Perro
        case "perro":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["CAN"] = contador_id.get("CAN", 0) + 1
            # Se retorna el id generado
            return f"CAN-{contador_id["CAN"]:03d}"
        
        # Si es Gato
        case "gato":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["FEL"] = contador_id.get("FEL", 0) + 1
            # Se retorna el id generado
            return f"FEL-{contador_id["FEL"]:03d}"
        
        # Si es Ave
        case "ave":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["AVE"] = contador_id.get("AVE", 0) + 1
            # Se retorna el id generado
            return f"AVE-{contador_id["AVE"]:03d}"
        
        # Si es Conejo
        case "conejo":
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["CON"] = contador_id.get("CON", 0) + 1
            # Se retorna el id generado
            return f"CON-{contador_id["CON"]:03d}"
        
        # Si es Otro
        case _:
            # Se actualiza el número de la especie en el diccionario contador_id
            contador_id["OTR"] = contador_id.get("OTR", 0) + 1
            # Se retorna el id generado
            return f"OTR-{contador_id["OTR"]:03d}"
##################################

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

                # Se espera que el usuario presione enter para continuar
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

                        # Se espera que el usuario presione enter para continuar
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

                # Se espera que el usuario presione enter para continuar
                input("\nPresione cualquier tecla para continuar...")

                # Se retorna el Menú Inicial
                return

    # Si no se encuenra el correo ingresado, se imprime el mensaje correspondiente
    print("\n¡No se encontró el correo ingresado! ❌")

    # Se espera que el usuario presione enter para continuar
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

    # Se espera que el usuario presione enter para continuar
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
        print("4. Registrar Atención")
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

                print("Ha seleccionado la opción 2")

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

                print("Ha seleccionado la opción 4")

            # PAGAR CITA
            case 5:
                # Se limpia la pantalla
                limpiar_pantalla()

                print("Ha seleccionado la opción 5")

            # SALIR
            case _:
                # Se limpia la pantalla
                limpiar_pantalla()

                # Se imprime mensaje de despedida
                print("¡Sesión Cerrada con Éxito! ✅\n")

                # Se espera que el usuario presione enter para continuar
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


    while True:

        # Se ingresa el nombre de la mascota
        nombre = input("Ingrese nombre de la mascota: ")

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
        raza = input("Ingrese raza: ")

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

        # Se agrega la nueva mascota al arreglo tabla_mascotas
        tabla_mascotas.append(mascota_nueva)

        # Se imprime mensaje de confirmación
        print("\n¡Mascota registrada con éxito! ✅")

        # while de validación para variable "nuevo_registro"
        while True:

            # Se consulta al usuario si desea registrar otra mascota
            nuevo_registro = input("\n¿Registrar otra mascota? Si(S) No(N): ").strip().upper()

            # Se evalua el valor ingresado
            match nuevo_registro:

                # Si el valor ingresado es "S", se sale del while de validación y se vuelve a repetir el proceso
                case "S":
                    errores = 0
                    break
                
                # Si el valor ingresado es "N", se sale de la función registrar_mascota y se retorna el menú del sistema
                case "N":
                    errores = 0
                    return

                # Si el valor ingresado no es "S" ni "N", se muestra el mensaje de error respectivo y se vuelve a solicitar el valor
                case _:
                    print("Valor ingresado inválido ❌")

                    if validar_errores(): return
#################################

####2.2.FUNCION REGISTRAR CITA####

#Ángela y Manuel aquí su código :)

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

#Daniel y Luis aquí su código :)

######################################

####2.5.FUNCION PAGAR CITA####

#Daniela y Manuel aquí su código :)

######################################

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
          





 

        
      









               

         

    














        
               


    

        


      

        

       

     





                 
         




                








         

     
       


    
            
    
     

     
         

    
        



    


    








                    