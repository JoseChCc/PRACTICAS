##         PRACTICA NRO1
## ALUMNO:JOSE EMERSON CHURATA CCAMA

#4 Escribir un Hola mundo que se imprima en consola.

print("Hola mundo")


#5 Escribe un programa que salude con el nombre de entrada desde el teclado.

nombre=input("Introduce tu nombre: ")

print(f"Hola ,", nombre)


#6 Escribe un programa que pida tu edad y muestre si es mayor de edad o no lo es.

edad=int(input("Introduce tu edad: "))

if edad >=18:
    print(f"Usted tiene",edad,"años, es mayor de edad")
else:
    print(f"Usted tiene",edad,"años, es menor de edad")


#7 Escribe un programa que pida un numero entero y determine si es par o impar.

numero=int(input("Introduce un número entero: "))
numero_residuo = numero % 2

if numero_residuo == 1:
    print(f"El numero",numero,", es impar")
else:
    print(f"El numero",numero,", es par")


#8 Escribe un programa que pida un numero entero y calcule la suma de 1 hasta el numero ingresado.

numero_entero=int(input("Introduce un número entero cualquiera: "))
suma= (numero_entero/2)*(numero_entero + 1)

print(f"La suma de todos los numeros enteros existentes entre 1 y",numero_entero,"es",suma)