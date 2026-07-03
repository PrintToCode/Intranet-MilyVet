#MilivetV2

#Importar módulo os para crear la función "limpiar_pantalla"
import os

#Importar módulo getpass para ocultar las contraseñas ingresadas por los usuarios
import getpass

#Importar módulo re para usar regex
import re

####CONSTRUCCION DE LA BASE DE DATOS####

#Se crea una lista de usuarios para simular una tabla de BD
tabla_usuarios = []

#Se crea la clase usuario
class Usuario:
    def __init__(self, correo, contrasena, preguntas_respuestas):
        self.correo = correo
        self.contrasena = contrasena
        self.preguntas_respuestas = preguntas_respuestas

#Se crea un usuario de prueba
usuario1 = Usuario(
    correo="luis.alberca.munive@gmail.com",
    contrasena="clave123",
    preguntas_respuestas=[
        ("¿Nombre de tu mascota?", "firulais"),
        ("¿Ciudad donde naciste?", "lima"),
        ("¿Película favorita?", "matrix")
    ]
)

#Se agrega el usuario creado a la "tabla_usuarios"
tabla_usuarios.append(usuario1)

########################################

####FUNCIONES####

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

####FUNCION MENU DEL SISTEMA####
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
                #Se limpia la pantalla
                limpiar_pantalla()

                print("Ha seleccionado la opción 1")

            # REGISTRAR CITA
            case 2:
                #Se limpia la pantalla
                limpiar_pantalla()

                print("Ha seleccionado la opción 2")

            # CAMBIAR CONTRASEÑA
            case 3:
                #Se limpia la pantalla
                limpiar_pantalla()

                #Se ejecuta función cambiar_contrasena
                cambiar_contrasena(correo_usuario)

            # REGISTRAR ATENCIÓN
            case 4:
                #Se limpia la pantalla
                limpiar_pantalla()

                print("Ha seleccionado la opción 4")

            # PAGAR CITA
            case 5:
                #Se limpia la pantalla
                limpiar_pantalla()

                print("Ha seleccionado la opción 5")

            #SALIR
            case _:
                #Se limpia la pantalla
                limpiar_pantalla()

                #Se imprime mensaje de despedida
                print("¡Sesión Cerrada con Éxito! ✅\n")

                # Se espera que el usuario presione enter para continuar
                input("Presione Enter para continuar...")

                #Se sale del bucle
                break

################################



#====FUNCIONES MENU DEL SISTEMA====#

####FUNCION CAMBIAR CONTRASEÑA####
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
            input("\nPresione Enter para continuar...")

            # Se retorna al menú del sistema
            return

##################################

#==================================#



####FUNCION INICIAR SESION####
def iniciar_sesion():

    # Se solicita al usuario ingresar su correo
    correo = input("Ingresar correo: ")

    # Se solicita al usuario ingresar su contraseña
    contrasena = getpass.getpass("Ingresar contraseña: ")

    # Se itera sobre los objetos user del arreglo tabla_usuarios
    for user in tabla_usuarios:
        # Si el correo y la contaseña del objeto user coincide con las ingresadas
        if user.correo == correo and user.contrasena == contrasena:
            # Se muestra el mensaje de éxito respectivo
            print("\nInicio de Sesión Correcto ✅")

            # Se espera que el usuario presione enter para continuar
            input("\nPresione Enter para continuar...")

            # Se ejecuta la función menu_sistema y se envía como parámetro el correo ingresado
            menu_sistema(correo)

            # Se retorna el Menú Inicial
            return

    # Si no se encuentra un objeto user cuyo correo y contraseña coincida con los ingresados, se muestra el mensaje de error respectivo
    print("\nCorreo ó Contraseña incorrecta ❌")

    # Se espera que el usuario presione enter para continuar, luego de ello se retorna al Menú Inicial
    input("\nPresione Enter para continuar...")

##############################

####FUNCION NUEVO USUARIO####
def nuevo_usuario():

    # Se solicita al usuario ingresar su correo
    correo = input("Ingresar correo: ")

    # Se verifica si el correo ingresado ya se encuentra registrado
    for user in tabla_usuarios:
        # Si el correo ingresado por el usuario ya se encuentra registrado, entonces se retorna al menú inicial
        if (user.correo).lower() == correo.lower():
            print("\nEl correo ingresado ya se encuentra registrado ❌\n")
            input("Presione Enter para continuar...")
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
        preguntas_respuestas = preguntas_respuestas
    )

    # Se agrega el nuevo objeto de usuario al arreglo tabla_usuarios
    tabla_usuarios.append(usuario_nuevo)

    # Se imprime mensaje de confirmación
    print("\n¡Usuario creado de manera exitosa! ✅")

    # Se espera que el usuario presione enter para continuar
    input("\nPresione Enter para continuar...")
####################################

####FUNCION RECUPERAR CONTRASEÑA####
def recuperar_contrasena():
    #Se pide al usuario que introduzca su correo
    correo_ingresado = input("Ingrese su correo: ")

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
                    input("Presione Enter para continuar...")
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
            input("\nPresione Enter para continuar...")

            # Se retorna al menú inicial
            return

    # Si no se encuentra al usuario en el arreglo "tabla_usuarios"
    print("\nNo se encontró el usuario ❌\n")

    # Se imprime el mensaje de error correspondiente
    input("Presione Enter para continuar...")
####################################

#################

#Menu Inicial
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