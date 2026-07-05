# Intranet MilivetV2

# Importar módulo os para crear la función "limpiar_pantalla"
import os

# Importar módulo getpass para ocultar las contraseñas ingresadas por los usuarios
import getpass

# Importar módulo re para usar regex
import re

# Importar la clase datetime (módulo datetime) para validar la fecha de nacimiento de las mascotas
from datetime import datetime

####CONSTRUCCION DE LA BASE DE DATOS####

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
    def __init__(self, correo, contrasena, preguntas_respuestas):
        self.correo = correo
        self.contrasena = contrasena
        self.preguntas_respuestas = preguntas_respuestas

        # nombres = input(f"Ingrese sus nombres: ")

        # nombre1,nombre2 = nombres.split()

        # apellidos = input(f"Ingrese sus apellidos: ")

        # apellido1,apellido2 = apellidos.split()

        # edad = int(input(f"Ingrese su edad: "))

        # departamento = input(f"Ingrese el departamento: ")
            
        # provincia = input(f"Ingrese la provincia: ")

        # distrito = input(f"Ingrese el distrito: ")

        # direccion = input(f"Ingrese su direccion (Calle,avenida,Jiron): ")

        # numero_domicilio = int(input(f"Ingrese su numero de domicilio: "))

        # numero_dni = int(input(f"Ingrese su numero de DNI: "))

        # marketing = input(f"Como se entero de nosotros?: ")

        # #Confirmacion de datos ingresados
        # print(f"Confirme su informacion antes de continuar!")

        # print(f"Nombres: {nombre1} {nombre2}")
        # print(f"Apellidos: {apellido1} {apellido2}")
        # print(f"Edad: {edad}")
        # print(f"Departamento: {departamento}")
        # print(f"Provincia: {provincia}")
        # print(f"Distrito: {distrito}")
        # print(f"direccion: {direccion} {numero_domicilio}")
        # print(f"Numero de DNI: {numero_dni} ")
        # print(f"Como se entero de nosotros?: {marketing}")

        # confirmacion = input(f"Toda su informacion esta correcta(escriba si/no?: ")

        # #Creacion de usuario y contraseña
        # if confirmacion.lower() == "si":

        #     usuario(correo) = input(f"Crea tu usuario: ")

        # print(f"Cuenta creada con exito, bienvenid@ {usuario}!")

        #    elif confirmacion.lower() == "no":

        #     #Modificacion de datos ingresados
        #     while True:
                  
        #         print(f"Nombres: {nombre1} {nombre2}")
        #         print(f"Apellidos: {apellido1} {apellido2}")
        #         print(f"Edad: {edad}")
        #         print(f"Departamento: {departamento}")
        #         print(f"Provincia: {provincia}")
        #         print(f"Distrito: {distrito}")
        #         print(f"direccion: {direccion} {numero_domicilio}")
        #         print(f"Numero de DNI: {numero_dni} ")
        #         print(f"Como se entero de nosotros?: {marketing}")

        #         dato = input(f"Que dato/s desea modificar?: ")

        #         if dato.lower() == "nombres":

        #    # nombres = input(f"Ingrese nuevamente sus nombres: ")

        #     nombre1,nombre2 = nombres.split()

        #     apellidos = input(f"Ingrese su apellido: ")

        #     apellido1,apellido2 = apellidos.split()

        #     edad = int(input(f"Ingrese su edad: "))

        #     departamento = input(f"Ingrese el departamento: ")
            
        #     provincia = input(f"Ingrese la provincia: ")

        #     distrito = input(f"Ingrese el distrito: ")

        #     direccion = input(f"Ingrese su direccion (Calle,avenida,Jiron): ")

        #     numero_domicilio = int(input(f"Ingrese su numero de domicilio: "))

        #     numero_dni = int(input(f"Ingrese su numero de DNI: "))

        #     marketing = input(f"Como se entero de nosotros?: ")



        #     print(f"Confirme su informacion antes de continuar!")

        #     print(f"Nombres: {nombre1} {nombre2}")
        #     print(f"Apellidos: {apellido1} {apellido2}")
        #     print(f"Edad: {edad}")
        #     print(f"Departamento: {departamento}")
        #     print(f"Provincia: {provincia}")
        #     print(f"Distrito: {distrito}")
        #     print(f"direccion: {direccion} {numero_domicilio}")
        #     print(f"Numero de DNI: {numero_dni} ")
        #     print(f"")


              
          





 

        
      









               

         

    














        
               


    

        


      

        

       

     





                 
         




                








         

     
       


    
            
    
     

     
         

    
        



    


    








                    