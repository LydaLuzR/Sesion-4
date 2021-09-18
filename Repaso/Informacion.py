#Los objetos dentro de Python son los tipos de datos
"Números enteros" #Int
"Numeros de punto flotante" #Float
"Texto o cadenas de caracteres" #"" (los Strings)
"Boleanos" #True or False

#Concatenar
    #Significa unir dos o más "Strings" u otros tipos de valores (Usualmente suma)
V= "Concatenar "
C= "palabras"
print(V+C)

#Variables
    ##Son los lugares en donde se guardan los valores de todo tipo, ya sean caracteres, cadenas de caracteres, numeros, etc
V= "Esta chingadera es una variable de tipo String"

A=5
B=6
C=7
    ##Ahora aplico otra variable para la suma (se pueden usar otros tipos de combinaciones)
Total_V= A+B+C

#Strings
    ##Son los que están dentro de las comillas
print('String 1')
print("String 2")
print('"String 3"')

#Flotantes
    #Básicamente son los números no exactos
F=float(5.41)
    ##Salen todos los números

#Enteros
NE=int(5.8)
print(NE)
    ##Solo se muestra el entero


#Redondear
"Para redondear números es importante seguir la siguiente escritura"
R= round('Inserte variable', 2)
    #El número seguido de la coma dentro de dicho parentesis sirve para especificar cuántos decimales se quieren mostrar

#Booleanos
True
False

#Operdores lógicos
    ##Los operadores lógicos van de la mano con los Booleanos.
"and" #Devuelve Verdadero si las todas las variables que estoy comparando son Verdaderas.
"or"  #Devuelve verdadero si al menos una de las variables que estoy comparando es verdadera.
"not" #Invertir el valor boleano.

#Operadores de comparación

"=="   #Compara dos valores y te dice si son iguales o no.
"!="   #Compara dos valores y te dice sin son diferentes o no.
">"    #Mayor a
"<"    #Menor a
">="   #Igual o mayor que el valor a comparar.
"<="   #Igual o menor que el valor a comparar.

#Condicionales
"if"     #Sirve como vía hacia una acción.
"elif"   #Si no cumple la primera condición se puede poner más de una vez para que una o más condiciones cumplan otros "atajos"
"else"   #Es la otra vía por si no se cumple la primera condición.
" : "    #Debajo de los puntos debo dejar 4 espacios o el programa falla ya que funciona como un "entonces"
pass     #Esta palabra sirve como un "Aquí voy a escribir codigo pero lo dejo para después"


#Puntuaciones especiales
""""""   #Conocido como triple comilla doble, permite escribir mucho texto


#Funciones deferenciadas
"def"    #Sirve para definir una variable con la cual se podrá ahorrar código.

###LAS FUNCIONES DEFINIDAS SIEMPRE TIENEN QUE HACERSE AL EMPEZAR EL CÓDIGO, ES DECIR, EN LA PARTE SUPERRIOR O PODRÍA DAR ERROR

""" 
def mensaje():       #Con esto defino el nombre de dicha variable que usaré siempre con los parentesis y los puntos.
    print("Haré que se repita 3 veces")    #Lo que quiero que imprima

mensaje()            #Aquí repito el número de veces que quiero que el mensaje se repita nombrando la varible siempre con los parentesis y los puntos.
mensaje()
mensaje() 
"""  
        #Con este codigo puedo ser capaz de escribir un mensaje 3 veces o las veces que yo desee.

"def mensaje(Saludo):  "       #Cuando coloco un nombre dentro de los parentesis estos pasan a ser una variable que usaré.
                               #"def" será lo que define, "mensaje" el nombre del codigo y "Saludo" mi variable.
                            
#DEF ejemplo

def suma(a,b):  #Creé una variable que se llama suma y le asigne dos variables
    print("Se suman dos números")   #Imprimí lo que hará dicha acción
    resultado= a+b  #Creé otra variable la cuál ejecutará el proceso de la primera
    return resultado    #Con esto devolví el valor que no está impreso
sumatoria= suma(1,4)    #Asigné los valores que se suman
print("El resultado es ", sumatoria)    #Imprimí un mensaje y el resultado.


#Atajos con teclado
"Si comento CNTRL con }" #todos los valores se vuelven # 
"Windows + ."            #Permite la entrada de emojis


#Devolver un valor
"return" #sirve para que me arroje un dato especifico
"Ejemplo de return"


#Cosas que se pueden hacer con los str(texto)

#Poner todo en mayuscula
".upper()"    #Funciona de la siguiente forma, a la variable que lleve antes la va a volver toda mayuscula

nombre= input("Por favor escriba su nombre ")   
print(nombre.upper())   #Pondrá la variable "nombre" en mayuscula.
#Cuando no se trabaja en consola no se imprimen los valores en la variable al invocarlos por lo que es recomendable imprimir con un print
##Es importante colocar los ()


#Primera letra mayuscula
".capitalize()" #Coloca solo la primera letra como mayuscula

nombre= input("Por favor escriba su nombre ")
print(nombre.capitalize()) 


#Quitar espacios
".strip()"  #Elimina los espacios basura que están al inicio o final de la variable


#Minusculas
".lower()"  #Coloca en minusculas todo


#Reemplazar letras
".replace()"    #Sirve para reemplazar x o y variable/valor.

nombre= input("Por favor escriba su nombre ")       
print(nombre.replace("o", "a")) #Aquí le estoy diciendo que me reemplace las letras "O" por las letras "A"


#INDICES (corchetes)
"""Los indices son la forma de sacar una letra o caracter según su posición, es decir, seleccionar dicho caracter en especifico"""
nombre= input("Por favor escriba su nombre ")
print(nombre[0].upper())    #Estoy indicando que escriba el nombre y a su vez que devuelva la primera letra
                            ##Los caracteres se empiezan a contar desde 0

#Contabilizar los caracteres
"len()" #Con esto puedo contar la cantidad de caracteres

nombre= input("Por favor escriba su nombre ")
print(len(nombre))

##Para contabilizar un mensaje dentro de los parentesis
print(len("Esto es una prueba para contabilizar letras"))   #No se mostrará el mensaje sino la cantidad de caracteres


#SLICES o fragmentos
"""Las Slices o rebanadas son la forma de llamar los "cortes" de las cadenas de caracteres"""

nombre= "Lyda"  #A nombre le di el valor del mío
print(nombre[0])    #Como sabemos selecciona la primera letra así y la imprime.
##Pero para seleccionar por rebanadas se usa

nombre= "Lyda"
print(nombre[0:2])  #Le estoy indicando que me muestre la mitad de mi nombre ya que pasa por las dos letras.
##Se puede obviar el primer elemento y solo poner.

###Sepuede el caso contrario también
nombre= "Lyda"
print(nombre[:3]) 

#Mostrará de la mitad para el final.
nombre= "Lyda"
print(nombre[2:]) #Ya que se indica eso.

#Con pasos, es decir
nombre= "Mariafrancisca"
print(nombre[1:8:2])    #Se saltará en este caso dos ya que es lo que le indiqué

#Para ir de atrás hacia adelante
nombre= "Lyda"
print(nombre[::-1]) #Ya que es negativo Python entiende que va de adelante hacia atrás.

#IMPORTANTE

"""if __name__ == '__main__': """
#Esto identifica como la primera operación o algoritmo como la principal y de ahí toma que los otros son secundarios.

"""
En Ppython los archivos .py son módulos, y al módulo que se ejecuta cuando hacemos, por ejemplo: 
python3 programa.py, se le da el nombre (por defecto) de __main__ por ser el módulo (archivo) principal.
Entonces, ese código básicamente dice Si este es el archivo que se está ejecutando, haz lo que está 
dentro del if
"""

#Constantes
LIMITE= 1000    #Para definir una constante basta con ponerla en mayusculas y el contador lo cambia de color

#WHILE

def run():
    LIMITE = 1000000
    contador = 0
    pontencia_2 = 2**contador
    while pontencia_2 < LIMITE: #Un while tiene la misma estructura que un IF
        print(f'2 elevado a la {contador} es igual a {pontencia_2}')
        contador = contador + 1
        pontencia_2 = 2**contador

if __name__ == "__main__":
    run()

##Hecho imprimiendo un número del 1 a 1000

def run():
    LIMITE = 1000
    contador = 0
    suma = 1+contador
    while suma < LIMITE:
        print(f'Se imprime del 1 al {suma}')
        contador = contador + 1
        suma = 2+contador

if __name__ == "__main__":
    run()

#Para sumar con While contar de uno en uno o de número en número

"+="    #Funciona para añadir el número de veces que se suma algo

contador= 1
print(contador)
while contador<1000:
    contador=contador+1 #Esta sería la forma larga
    contador+=1     #Esta es la forma corta
    print(contador)