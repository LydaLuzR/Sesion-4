import math

ZonasA= int(input("Cantidad de zonas para analizar "))
area=float(input("Ingrese el area de instalación"))
antenasV=int(input("¿Cuántas antenas viejas hay? "))
tiponew=input("Digite el tipo de nueva antena ")


a=11400
b=12600
c=41100
d=14700
e=38000 

"""
Para ello, el sistema debe recibir como entrada un número mayor o igual a 0 de zonas a
analizar. Posteriormente, por cada zona se debe leer el área en la que se desean
instalar las nuevas antenas en m2
, así como la cantidad de antenas previamente
instaladas y el tipo de las nuevas antenas. Luego, se debe calcular la cantidad de
antenas a instalar del tipo deseado, si esta cantidad es negativa, se toma la cantidad a
instalar como 0 

Además, la cantidad de antenas previamente instaladas tiene que ser un número entero
mayor o igual a 0 y el tipo de las nuevas antenas tiene que estar entre los antes
mencionados, en caso contrario la cantidad de antenas a instalar se toma como 0.

Las antenas previamente instaladas tienen un rango de alcance de 4800 m2
 y las
nuevas antenas a instalar tienen un rango de 11400 m2
, 12600 m2
, 41100 m2
, 14700 m2
y 38000 m2
 para los tipos “a”, “b”, “c”, “d” y “e” respectivamente.
Finalmente se debe mostrar por pantalla, la cantidad total de nuevas antenas instaladas
independientemente del tipo. Luego, para cada uno de los tipos de nuevas antenas, en
líneas distintas, se debe mostrar su nombre seguido de su proporción porcentual
correspondiente respecto al total de nuevas antenas instaladas, formateado 2 cifras
decimales y separado por espacio. Si no se instalan nuevas antenas todas las
proporciones porcentuales antes mencionadas deben ser 0.00%"""