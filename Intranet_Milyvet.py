#Mensaje de bienvenida
print (f"Bienvenido a la intranet de MiliVet, expertos en mascotas!")

#Menu principal
while True:
   
       print(f"\n===MENU PRINCIPAL====")
       print(f" 1. Inicio de sesion")
       print(f" 2. Crear cuenta")
       print(f" 3. Actualizacion de datos")
       print(f" 4. Registra tu mascota!")
       print(f" 5. Programar nueva cita")
       print(f" 6. Reprogramar cita existente")
   
#Elegir opcion
       opcion = int(input(f"Seleccione una opcion: "))

#opcion 1
       if opcion == 1:
          
            print(f"\n===INICIO DE SESION===")

            print(f"Bienvenido, lo estabamos esperando ;D!")

            intentos = 0

            max_intentos = 3

            while intentos < max_intentos:

                  tu_usuario = input(f"Ingrese su usuario: ")

                  tu_contraseña = input(f"Ingrese su contraseña: ")

                         
              
 #opcion 2      
       elif opcion == 2:
            
            print(f"\n===REGISTRO DE CUENTA===")

            print(f"Registrese, es gratis ;D!")

#Registro de datos del usuario

            nombres = input(f"Ingrese sus nombres: ")

            nombre1,nombre2 = nombres.split()

            apellidos = input(f"Ingrese su apellido: ")

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

            confirmacion = input(f"Toda su informacion esta correcta?: ")

#Rectificacion de datos

            if confirmacion.lower() == "si":

               usuario = input(f"Crea tu usuario: ")

               contraseña = input(f"Crea tu contraseña: ")









            
          





 

        
      









               

         

    














        
               


    

        


      

        

       

     





                 
         




                








         

     
       


    
            
    
     

     
         

    
        



    


    








