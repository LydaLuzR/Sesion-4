# -*- coding: utf-8 -*-
"""Sesion 2_Variables_Algoritmos (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IdRMzAKnO8AM-J1Yfp4_NERXvUzT7RCX

# Fundamentos de Programación con Python

## Estructuras algorítmicas

Vamos a trabajar en modificar el algoritmo y pasarlo a Python.

Inicio

    a ⇐ 2 
    b ⇐ 3
    c ⇐ 1
    x1 ⇐ (-b + ((b^2)-(4*a*c))^(½))/(2*a)
    x2 ⇐ (-b - ((b^2)-(4*a*c))^(½))/(2*a)
    escribir x1
    escribir x2
Fin


Además de las operaciones matemáticas básicas que vimos en la sesión anterior, también podemos importar otras operaciones o funciones desde una "librería" (aunque la traducción correcta de library es biblioteca, en español se ha vuelto más común hablar de librerías).

Por ejemplo, podemos usar la función raíz cuadrada sqrt importando math. Escribe el código para imprimir la raíz cuadrada de un valor.
"""

import math
x= 100
math.sqrt(x)

"""Puedes ver todas las funciones que tiene esta librería y cómo se usan, con los siguientes comandos:"""

#dir(math)           # Lista de funciones
#help(math)          # Ayuda sobre la librería math

help(math.sqrt)     # Ayuda sobre la función sqrt

"""Volvamos al algoritmo entonces. En la prueba de escritorio, determinamos que (b^2)-(4*a*c) debe ser mayor a 0 para poder obtener la raiz cuadrada. Aquí vamos a modificar los valores para ejecutar el código. Mas adelante, con condicionales podremos evaluar los valores durante la ejecución e imprimir un mensaje en caso de error.                                                                                    """



"""### Actividad 1

Los tipos de datos son muy importantes en programación. Aunque Python no exige declarar un tipo de variable y permite cambiarlo (lo cual no ocurre en otros lenguajes de programación), cada variable si asume un tipo según el dato que tenga almacenado. Por ejemplo:

"""

a = 5     # Esto es un Entero (No tiene decimales)
b = 5.3   # Esto es un flotante (Un número que puede tener comas decimals)
c = '5'   # Esto es un texto, y por ende, no podemos hacer operaciones matemáticas con c

"""Usando la función type(), obten e imprime el tipo de dato de las variables a, b y c:"""

d= True
print (type (a),type (b), type (c), type (d))

"""### Actividad 2

Ahora, practiquemos nuevamente la estructura algorítmica y recordemos el uso de tipos de datos. 

Juan y Pedro acostumbran jugar un juego de adivinar un número. En el juego es permitido dar tres pistas p1 p2 p3. Después de muchos intentos Pedro descubre la fórmula con la que Juan crea el número con las pistas dadas, y es la siguiente:

    p1 + p3 ∗ p2 − (p1 + p2 ∗ 5 + 1) / (p2 + p1/2) + p3

Si la pista que da Juan es 2, 1 y 4, ¿cuál es el número que debería decir Pedro para ganar? Escribamos el código para recibir los valores y devolver el valor que Pedro debería decir.

"""

p1=float(input('Pista 1 '))
p2=float(input('Pista 2 '))
p3=float(input('Pista 3 '))
valor= p1 + p3 * p2 - (p1 + p2 * 5 + 1) / (p2 + p1/2) + p3
print("El número es", valor)



"""Calculo de la nota final

Un alumno desea saber cuál será su calificación 
final en la materia de Algoritmos. Dicha calificación
se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.

30% de la calificación del examen final.

15% de la calificación de un trabajo final.

"""

NotaP1=float(input('Digite la nota del parcial 1 '))
NotaP2=float(input('Digite la nota del parcial 2 '))
NotaP3=float(input('Digite la nota del parcial 3 '))
Examen=float(input('Digite la nota del examen final '))
Trabajo=float(input('Digite la nota del trabajo final '))

cal1= ((NotaP1+NotaP2+NotaP3)/3)*0.55
cal2= (Examen)*0.30
cal3= (Trabajo)*0.15
Definitiva_Total= cal1+cal2+cal3

print("Su calificación final es ", Definitiva_Total)

V1=float(input("Velocidad vehiculo 1 km/h: "))
V2=float(input("Velocidad vehiculo 2 km/h: "))
Distancia=float(input("Distancia entre vehiculos km: "))
tiempo=(Distancia/abs(V1-V2))*60
print("El vehiculo 2, alcanzará al vehiculo 1 en ",tiempo,"minutos")

"""Pedir el nombre y apellidos de una persona y mostrar solos las letras iniciales"""

Nombre=input("Digite su nombre ")
Apellido1=input("Digite su primer apellido ")
Apellido2=input("Digite su primer apellido ")
print((Nombre[0] + Apellido1[0] + Apellido2[0]).upper()) 
#los corchetes y los números representan la letra o caracter que quieres extraer, en Python se comienza desde 0
print(Nombre[:2]) #los puntos representan toda la cadena y el número son las primeras 2
print(Nombre[2:]) #cuando se pone al revés quiere decir que muestra los últimos caracteres
print(Nombre[::-1]) #Pone los caracteres al revés
#En el print debe ponerse los valores que queremos exponer para que los muestre (Nombre,Apellido,Apellido)

"""Ejercicio 4

Dado un número de dos cifras diseñe un algoritmo que permita obtener el número invertido

Ejemplo

Si se introduce 23 que muestre 32
"""

Numero=input("Digite el número ")
print((Numero[::-1]).upper())
#Este es como cadena

Numero=int(input("Digite el número de dos cifras "))
Descenas= Numero % 10
Unidades= (Numero//10) #con // saco el entero sin 0.
Unidades= int(Numero/10) #con Int saco el entero sin 0.
Invertido= Descenas*10+Unidades
print(Descenas)
print(Unidades)
print(Invertido)

"""Ejercicio 5

Un maestro desea saber qué porcentaje de hombres y qué 
porcentaje de mujeres hay en un grupo.
"""

Numero1=int(input("Digite el número de hombres "))
Numero2=int(input("Digite el número de mujeres "))
Total=int(Numero1+Numero2)
P1=int(Numero1*100/Total)
P2=int(Numero2*100/Total)

print("El porcentaje de hombres es de", P1, "% de un 100%")
print("El porcentaje de mujeres es de", P2, "% de un 100%")
print("Alumnos en total", Total,)

"""Ejercicio 6

Tres personas deciden invertir su dinero para fundar una empresa.

Cada una de ellas invierte una cantidad distinta.

Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.
"""

Valor1=int(input("Digite el valor invertido por el inversionista 1 "))
Valor2=int(input("Digite el valor invertido por el inversionista 2 "))
Valor3=int(input("Digite el valor invertido por el inversionista 3 "))
Total=round(Valor1+Valor2+Valor3)
P1=round((Valor1*100/Total),2)
P2=round((Valor2*100/Total),2)
P3=round((Valor3*100/Total),2)
#Para redondear un número se hace el siguiente procedimiento se pone el Round más el número 2 
#lo cual permite también que los valores dados en los porcentajes totales de 100%
print("El total de la inversión fue", Total, "lo invertido por el inversionista 1 fue de", P1, "%, por el inversionista 2", P2, "% y por el inversionista 3", P3, "%")

