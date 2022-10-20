'''
Codificar un programa en Python utilizando funciones que permita
recibir: Nombre, edad, país, equipo y tiempo en minutos de
múltiples ciclistas. El software estará en la capacidad de calcular y
mostrar en pantalla cual fue el ciclista más rápido
'''

opcion=100
nombre=""
edad=0
pais=""
equipo=""
tiempo=0

ciclistas=[]

def agregarCiclista():
    nombre=input("Digite el nombre del ciclista: ")
    edad=int(input("Digite la edad del ciclista: "))
    pais=input("Digite el país del ciclista: ")
    equipo=input("Digite el nombre del equipo del ciclista: ")
    tiempo=int(input("Digite el tiempo del ciclista: "))
    ciclista = {'nombre': nombre, 'edad':edad, 'pais':pais, 'equipo':equipo, 'tiempo':tiempo}
    ciclistas.append(ciclista)
agregarCiclista()




while(opcion!=0):
    print("\n")
    print("|****************************|")
    print("|**|      Bienvenidos     |**|")
    print("|**|         Menu         |**|")
    print("|****************************|")
    print("")
    print("Digite 1 para agregar ciclista: ")
    print("Digite 2 para ver resultados: ")
    opcion=int(input("Digita una opcion: "))
    if(opcion==1):
        agregarCiclista()

