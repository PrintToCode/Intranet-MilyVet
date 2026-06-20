#Mensaje de bienvenida
print (f"Bienvenido a la intranet de MiliVet, expertos en mascotas!")

usuario = None
contraseña = None
pregunta_seguridad = None

#Menu principal
while True:
   
       print(f"\n===MENU PRINCIPAL====")
       print(f" 1. Inicio de sesion")
       print(f" 2. Crear cuenta")
   
#Elegir opcion
       opcion = int(input(f"Seleccione una opcion: "))

#opcion 1
       if opcion == 1:

           if usuario is None:

               print("Primero debe crear una cuenta.")

          
               print(f"\n===INICIO DE SESION===")

               print(f"Bienvenido, lo estabamos esperando ;D!")

               intentos = 0

               max_intentos = 3

#Inicio de sesion 

               while intentos < max_intentos:

                  tu_usuario = input(f"Ingrese su usuario: ")

                  tu_contraseña = input(f"Ingrese su contraseña: ")

                  if tu_usuario == usuario and tu_contraseña == contraseña:

                     print(f"Ha iniciado sesion correctamente, bienvenido {usuario} ;D!")

 #Menu de opciones

                     while True:
                        
                        print(f" 1. Actualizacion de datos")
                        print(f" 2. Registra tu mascota!")
                        print(f" 3. Programar nueva cita")
                        print(f" 4. Reprogramar cita existente")

                         

                  elif tu_usuario != usuario and tu_contraseña != contraseña:
                     
                     intentos += 1
                     print(f"Usuario y/o contraseña incorrectos!")
                     print(f"Le quedan {max_intentos - intentos} intentos!")
                     

               if intentos == max_intentos:

                print(f"3/3 intentos fallidos registrados!")
                print(f"Responda una pregunta de seguridad para acceder!")

                respuesta = input(f"Cual es su fecha de nacimiento: ")
                
                if respuesta == pregunta_seguridad:

                   nueva_contraseña = input(f"Actualize su contraseña: " )
                   contraseña = nueva_contraseña
                   print(f"Contraseña actualizada con exito: ")

                else:
                   print(f"Respuesta incorrecta!")
                   print(f"Su cuenta ha sido bloqueada temporalmente, contactar a soporte!")
                         
              
 #opcion 2      
       elif opcion == 2:
            
            print(f"\n===REGISTRO DE CUENTA===")

            print(f"Registrese, es gratis ;D!")

 #Registro de datos del usuario

            nombres = input(f"Ingrese sus nombres: ")

            nombre1,nombre2 = nombres.split()

            apellidos = input(f"Ingrese sus apellidos: ")

            apellido1,apellido2 = apellidos.split()

            edad = int(input(f"Ingrese su edad: "))

            departamento = input(f"Ingrese el departamento: ")
            
            provincia = input(f"Ingrese la provincia: ")

            distrito = input(f"Ingrese el distrito: ")

            direccion = input(f"Ingrese su direccion (Calle,avenida,Jiron): ")

            numero_domicilio = int(input(f"Ingrese su numero de domicilio: "))

            numero_dni = int(input(f"Ingrese su numero de DNI: "))

            marketing = input(f"Como se entero de nosotros?: ")

 #Confirmacion de datos ingresados

            print(f"Confirme su informacion antes de continuar!")

            print(f"Nombres: {nombre1} {nombre2}")
            print(f"Apellidos: {apellido1} {apellido2}")
            print(f"Edad: {edad}")
            print(f"Departamento: {departamento}")
            print(f"Provincia: {provincia}")
            print(f"Distrito: {distrito}")
            print(f"direccion: {direccion} {numero_domicilio}")
            print(f"Numero de DNI: {numero_dni} ")
            print(f"Como se entero de nosotros?: {marketing}")

            confirmacion = input(f"Toda su informacion esta correcta(escriba si/no?: ")

#Creacion de usuario y contraseña

            if confirmacion.lower() == "si":

               usuario = input(f"Crea tu usuario: ")

               contraseña = input(f"Crea tu contraseña: ")

               print(f"En caso olvide su contraseña, habilite una pregunta de seguridad!")

               pregunta_seguridad = input(f"Cual es su fecha de cumpleaños?: ")

               print(f"Cuenta creada con exito, bienvenid@ {usuario}!")
               

            elif confirmacion.lower() == "no":

 #Modificacion de datos ingresados

               while True:
                  
                   print(f"Nombres: {nombre1} {nombre2}")
                   print(f"Apellidos: {apellido1} {apellido2}")
                   print(f"Edad: {edad}")
                   print(f"Departamento: {departamento}")
                   print(f"Provincia: {provincia}")
                   print(f"Distrito: {distrito}")
                   print(f"direccion: {direccion} {numero_domicilio}")
                   print(f"Numero de DNI: {numero_dni} ")
                   print(f"Como se entero de nosotros?: {marketing}")

                   dato = input(f"Que dato/s desea modificar?: ")

                   if dato.lower() == "nombres":

                      nombres = input(f"Ingrese nuevamente sus nombres: ")

                      nombre1,nombre2 = nombres.split()

                   elif dato.lower() == "apellidos":

                       apellidos = input(f"Ingrese nuevamente sus apellidos: ")

                       apellido1,apellido2 = apellidos.split()

                   elif dato.lower() == "edad":

                       edad = int(input(f"Ingrese nuevamente su edad: "))

                   elif dato.lower() == "departamento":

                       departamento = input(f"Ingrese nuevamente el departamento: ")

                   elif dato.lower() == "provincia":

                        provincia = input(f"Ingrese nuevamente la provincia: ")

                   elif dato.lower() == "distrito":

                        distrito = input(f"Ingrese nuevamente el distrito: ")

                   elif dato.lower() == "direccion":

                        direccion = input(f"Ingrese nuevamente la direccion: ")

                   elif dato.lower() == "domicilio":

                        numero_domicilio = int(input(f"Ingrese nuevamente el numero de domicilio: "))

                   elif dato.lower() == "dni":

                        numero_dni = int(input(f"Ingrese nuevamente el DNI: "))

                   elif dato.lower() == "marketing":

                        marketing = input(f"¿Cómo se enteró de nosotros?: ")

                   else:

                        print("Dato no válido.")
                        continue

                   confirmar = input(f"\n¿Desea seguir modificando datos? (si/no): ")

                   if confirmar.lower() == "no":
                     break

                   elif confirmar.lower() != "si":
                     print(f"Respuesta inválida. Debe ingresar 'si' o 'no'.")
                  

                    

                       

                       

                      

                    

                

                 







            
          





 

        
      









               

         

    














        
               


    

        


      

        

       

     





                 
         




                








         

     
       


    
            
    
     

     
         

    
        



    


    








