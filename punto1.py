# Codificar un programa en python utilizando funciones que permita recibir: nombre, edad, pais, equipo y tiempo en minutos de multiples ciclistas. El software está en la capacidad de calcular y mostrar en pantalla cual fue el ciclista más rapido

def ingresarCiclista ():
    i = True
    nombre = ""
    edad = 0
    pais = ""
    equipo = ""
    tiempoCiclista = 0
    tiempoFinal = 0

    while(i):
        print("***********************")
        print("******** Menu *********")
        print("***********************")
        print("1. Agregar un ciclista")
        print("2. Calcular ver resultados")
        print("3. Salir del programa")
        opcion = int(input("Ingrese la opcion: "))
        print("")

        if opcion == 1:
            j = 0
            while(j == 0):
                nombre = input("Porfavor ingrese el nombre del ciclista: ")
                edad = int(input("Que edad tiene el ciclista: "))
                pais = input("Ingrese el país del cilista: ")
                equipo = input("Ingrese el equipo del ciclista: ")
                tiempoCiclista = int(input("Ingrese el tiempo hecho por el ciclista: "))
                print("")

                if(tiempoCiclista < tiempoFinal or tiempoFinal == 0):
                    tiempoFinal = tiempoCiclista
                    nombreFinal = nombre
                
                j = int(input("Deseas salir del programa? (Digite 1 para salir, Digite 0 para seguir): "))
                print("")
        elif opcion == 2:
            if tiempoFinal == 0:
                print("No se ha ingresado ningun ciclista")
                print("")
            else:
                print(f'Este es el nombre del ciclista más rapido: {nombreFinal}')
                print(f'Tiempo del ciclista mas rapido: {tiempoFinal}')
                print("")
        elif opcion == 3:
            i = False
            print("***********************")
            print("Gracias por utilizar nuestro programa")

ingresarCiclista()
    
            
            
