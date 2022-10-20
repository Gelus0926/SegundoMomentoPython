""" Codificar un programa en Python utilizando funciones lamba que
permita: recibir 2 números y devolver
1 → si el primer número es mayor que el segundo
-1→ si el primer número es menor que el segundo

Después una segunda función debe recibir el 1 o el -1 retornado por

la función 1 y mostrar un mensaje
Si recibe 1 → Debe indicar que el primer número es mayor
Si recibe -1 → Debe indicar que el segundo número es mayor """

mayorQue =lambda numero1, numero2: 1 if numero1 > numero2 else -1

numero=mayorQue(6,1)

funcionDos = lambda numero: print('El primer numero es mayor') if numero == 1 else print('El segundo numero es mayor')

funcionDos(numero)



