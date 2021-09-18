def mensaje():
    #Def sirve para no repetir una serie de pasos varias veces
    print("Imprime este mensaje")
    print("Para que se repita 3 veces")

mensaje()
mensaje()
mensaje()

#Parametros

#Ejemplo largo sin pasos comunes

opcion=input("Elige una opción (1,2,3) ")
if opcion=="1":
    print("Hola")
    print("¿Cómo estás?")
    print("Espero que te encuentres bien")
    print("Elegiste opción 1")
elif opcion=="2":
    print("Hola")
    print("¿Cómo estás?")
    print("Espero que te encuentres bien")
    print("Elegiste opción 2")
elif opcion=="3":
    print("Hola")
    print("¿Cómo estás?")
    print("Espero que te encuentres bien")
    print("Elegiste opción 3")
else:
    print("Elige una opción válida")

#Ejemplo largo con pasos comunes

def texto(mensaje):
    print("Hola")
    print("¿Cómo estás?")
    print("Espero que te encuentres bien")
    print(mensaje)

opcion=str(input("Elija un número del 1 al 3 "))
if opcion=="1":
    texto("Elegiste la opción 1")
elif opcion=="2":
    texto("Elegiste la opción 2")
elif opcion=="3":
    texto("Elegiste la opción 3")
else:
    print("Elija una opción válida")

def suma(a,b):  #Creé una variable que se llama suma y le asigne dos variables
    print("Se suman dos números")   #Imprimí lo que hará dicha acción
    resultado= a+b  #Creé otra variable la cuál ejecutará el proceso de la primera
    return resultado    #Con esto devolví el valor que no está impreso
sumatoria= suma(1,4)    #Asigné los valores que se suman
print(sumatoria)    #Imprimí el resultado

