#Módulo Cambio de Contraseña - Luis Alberca

#Importar módulo os para crear la función "limpiar_pantalla"
import os

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

####LIMPIAR PANTALLA####
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
########################

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

            print("Ha seleccionado la opción 2")
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