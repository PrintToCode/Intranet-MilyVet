#Módulo Cambio de Contraseña - Luis Alberca

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

    # Se retorna la tupla contrasena_valida, errores
    return contrasena_valida, errores
########################

####FUNCION NUEVO USUARIO####
def nuevo_usuario():

    # Se solicita al usuario ingresar su correo
    correo = input("Ingresar correo: ")

    # La validación de la contraseña se realiza mediante un bucle while
    while True:

        # Se solicita al usuario ingresar su contraseña
        contrasena = getpass.getpass("Ingresar contraseña: ")

        # Se envía la contraseña introducida por el usuario a la función validar_contrasena para evaluar su complejidad.
        # la tupla de salida se almacena en las variables valida y lista_errores
        valida, lista_errores = validar_contrasena(contrasena)

        # Si la contraseña cumple con la complejidad
        if valida == True:
            # Se imprime el mensaje de éxito correspondiente
            print("Contraseña válida ✅\n")
            # Se sale del while
            break
        # Si la contraseña NO cumple con la complejidad
        else:
            # Se imprime el mensaje de error correspondiente
            print("Contraseña inválida ❌. Errores encontarados:\n")
            # Se listan los errores encontrados en la complejidad de la contraseña
            for error in lista_errores:
                print(f"- {error}")
            
            # Se solicita al usuario que presione la tecla "Enter" para volver a intentarlo ó "X" para retornar al menú principal
            opcion = input("\nPresione Enter para volver a interntarlo ó \"X\" para volver al menú principal...\n ")

        # Si el usuario presiona la tecla "X", se regreda al menú principal
        if opcion.lower() == "x":
            return

    # Se define un arreglo para ingresar las tuplas: pregunta, respuesta del usuario
    preguntas_respuestas = []

    # Se utiliza un for para que el usuario pueda ingresar las 3 tuplas de pregunta, respuesta
    for i in range(3):
        # Se solicita al usuario que ingrese una pregunta de seguridad
        pregunta = input(f"Escriba pregunta de seguridad {i + 1}: ")
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
    print("\n¡Usuario creado de manera exitosa!\n")

    # Se espera que el usuario presione enter para continuar
    input("\nPresione Enter para continuar...")
####################################

####FUNCION RECUPERAR CONTRASEÑA####
def recuperar_contrasena():
    #Se pide al usuario que introduzca su correo
    correo_ingresado = input("Ingrese su correo: ")

    #Se busca el correo ingresado en la "tabla_usuarios"
    for user in tabla_usuarios:
        if user.correo == correo_ingresado:

            print("\nUsuario encontrado\n")
            
            for pregunta, respuesta in user.preguntas_respuestas:
                respuesta_usuario = input(f"{pregunta}\n")
                if respuesta_usuario != respuesta:
                    print("Respuesta Incorreta\n")
                    input("Presione Enter para continuar...")
                    return
            
            print("\nHa contestado de manera correcta todas las preguntas\n")

            password_nueva = input("Ingrese una contraseña nueva: ")

            user.contrasena = password_nueva

            print(f"\n¡Contraseña actualizada!")

            input("\nPresione Enter para continuar...")


            return

        else:
            print("No se encontró el usuario\n")
            input("Presione Enter para continuar...")
####################################

#################

#Menu Principal
while True:

    #Se limpia la pantalla
    limpiar_pantalla()
    
    #Se muestra el menú principal
    print("====MENU PRINCIPAL====")
    print("1. Iniciar Sesion")
    print("2. Nuevo Usuario")
    print("3. Recuperar Contraseña")
    print("4. Salir")

    #Se pide al usuario que ingrese una opción
    main_option = int(input("Ingrese una opción: "))

    #Se evalúa la opción ingresada en el menú principal
    match main_option:

        #INICIAR SESION
        case 1:
            #Se limpia la pantalla
            limpiar_pantalla()

            print("Ha seleccionado la opción 1")

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
            print("Hasta luego...\n")

            #Se sale del bucle
            break