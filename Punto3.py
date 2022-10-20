"""
El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:
Almacenar información de un cliente (nombre, apellido, cedula, ciudad)
Almacenar información de la cuenta (numeroCuenta, saldo)
Se debe permitir consultar saldo en cualquier momento
Se debe permitir ingresar o retirar dinero  cuando se desee
"""


from errno import ESTALE


opcion = 1
codigo=0
nombre=""
precio=0
ciudad=""
personas=[]
cuentas=[]

while(opcion!=0):
    print("Digitar 1 para almacenar información de un cliente (cedula, nombre, apellido, ciudad): ")
    print("Digitar 2 para almacenar información de la cuenta (numero de cuenta, saldo): ")
    print("Digitar 3 para permitir consultar saldo en cualquier momento: ")
    print("Digitar 4 para permitir ingresar o retirar dinero  cuando se desee: ")
    print("Digitar 0 para SALIR ")
    print("\n")
    opcion=int(input("Digita una opcion: "))
    if(opcion==0):
        print("Gracias por utilizar el servicio de Banco de Braavos")
        break
    elif(opcion==1):
        cedula=int(input("Digite la cedula de la persona: "))
        nombre=input("Digite el nombre de la persona: ")
        apellido=input("Digita el apellido de la persona: ")
        ciudad=input("Digite la cuidad de la persona: ")
        persona={'cedula':cedula,'nombre':nombre,'apellido':apellido, 'ciudad':ciudad}
        personas.append(persona)
        print("\n")
    elif(opcion==2):
        numeroCuenta=int(input("Digite el número de la cuenta: "))
        saldo=int(input("Digite el saldo de la cuenta: "))
        cuenta={'numeroCuenta':numeroCuenta, 'saldo':saldo}
        cuentas.append(cuenta)
        print("\n")
    elif(opcion==3):
        buscarCodigo=int(input("Digite el numero de la cuenta que desea buscar: "))
        for indice,cuenta in enumerate(cuentas):
            if(buscarCodigo==(cuenta['numeroCuenta'])):
                saldo=cuenta['saldo']
                print(f'El saldo de la cuenta {buscarCodigo} es: {saldo}')
                print("\n")
            else:
                print("El numero de cuenta no se encuentra ")
                print("\n")
    elif(opcion==4):
        eleccion=int(input("Digite 1 para ingresar, digite 2 para sacar: "))
        if(eleccion==1):
            buscarCodigo=int(input("Digite la cuenta que desea buscar: "))
            for indice,cuenta in enumerate(cuentas):
                if(buscarCodigo==(cuenta['numeroCuenta'])):
                    nuevosaldo=int(input("Digite cuanto quiere ingresar: "))

                    saldo=cuenta['saldo']
                    calculo=saldo+nuevosaldo
                    cuenta['saldo']=calculo
                    print(f'El nuevo saldo de la cuenta {buscarCodigo} es: {calculo}')
                    print("\n")
                else:
                    print("El numero de cuenta no se encuentra ")
                    print("\n")
        elif(eleccion==2):
            buscarCodigo=int(input("Digite la cuenta que desea buscar: "))
            for indice,cuenta in enumerate(cuentas):
                if(buscarCodigo==(cuenta['numeroCuenta'])):
                    nuevosaldo=int(input("Digite cuanto quiere retirar: "))

                    saldo=cuenta['saldo']

                    if (saldo < nuevosaldo):
                        print("No tienes suficiente saldo")
                    else:
                        calculo=saldo-nuevosaldo
                        cuenta['saldo']=calculo
                        print(f'El nuevo saldo de la cuenta {buscarCodigo} es: {calculo}')
                        print("\n")
                else:
                    print("El numero de cuenta no se encuentra ")
                    print("\n")
        else:
            print("Elección no válida")
            print("\n")
    else:
        print("Digite un numero valido")
        print("\n")