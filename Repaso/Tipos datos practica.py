#Concatenar Strings
N1= "Pepito "
N2= "Mendez "
N3= "Fernandez"
N4= N1+N2+N3
print("N1", ",", "N2")

#Concatenar Floats
N5= 3.1
print(N5)

#Concatenar Booleanos
ES= True
print(ES)


#Operadores lógicos

#AND
Estudiante= True
Trabaja= False
V= Estudiante and Trabaja
print(V)
    #Me va a arrojar Falso ya que se supone que para dar verdadero todas las variables deben ser verdaeras.

Estudiante= True
Trabaja= True
V= Estudiante and Trabaja
print(V)
    #Arroja verdadero ya que todas lo son.

#OR
Estudiante= True
Trabaja= False
V= Estudiante or Trabaja
print(V)
    #Arroja verdadero ya que tiene una variable la cual lo es, solo arrojará Falso cuando todas sean Falsas.

Estudiante= False
Trabaja= False
V= Estudiante or Trabaja
print(V)
    #Arroja Falso ya que todas tienen Falso.

"Si usamos" and "y si un valor es falso, el resultado será falso. Para que de verdadero, ambos deben ser verdaderos."

"Si usamos" or "y si un valor es verdadero, el resultado será verdadero."
"En" or "basta que una de las dos condiciones (o premisas) se cumpla para que de verdadero."

#NOT

Estudiante= False
Trabaja= True
V= not Estudiante 
V2= not Trabaja
print(V,",",V2)
    #Invierte los valores, solo aplica con un dato dentro de una variable.

Estudiante= True
Trabaja= True
V= not Estudiante 
V2= not Trabaja
print(V,",",V2)
    #Caso con doble True

Estudiante= False
Trabaja= False
V= not Estudiante 
V2= not Trabaja
print(V,",",V2)
    #Caso con doble False

#Operadores de Comparación

#==

V1= 5
V2= 5
VT= V1==V2
print(VT)
    #Dará que es verdadero ya que ambos números son iguales.

V1= 5
V2= 7
VT= V1==V2
print(VT)
    #Dará que es Falso ya que ambos números son diferentes.

#!=

V1= 5
V2= 7
VT= V1!=V2
print(VT)
    #Dará verdadero ya que ambos valores son distintos.

V1= 5
V2= 5
VT= V1!=V2
print(VT)
    #Dará Falso ya que ambos son iguales.

#>
V1= 5
V2= 5
VT= V1>V2
print(VT)   
    #Dará Falso ya que son iguales.

V1= 5
V2= 7
VT= V1>V2
print(VT)   
    #Dará falso ya que 5 es menor que 7.

V1= 7
V2= 2
VT= V1>V2
print(VT)   
    #Dará verdadero ya que 7 efectivamente es mayor que 2.

#<

V1= 5
V2= 7
VT= V1<V2
print(VT)   
    #Dará verdadero ya que 7 es mayor que 5.

V1= 7
V2= 7
VT= V1<V2
print(VT)   
    #Dará Falso ya que son iguales.

V1= 7
V2= 2
VT= V1<V2
print(VT)
    #Dará falso ya que son 2 no puede ser mayor que 7.


#>=

V1= 7
V2= 2
VT= V1>=V2
print(VT) 
    #Dará verdadero debido a que 7 sí es mayor que 2, pero no igual a 2.

V1= 7
V2= 7
VT= V1>=V2
print(VT)
    #Dará verdadero ya que 7 es igual a 7

V1= 7
V2= 8
VT= V1>=V2
print(VT)
    #Dará Falso ya que 7 no es mayor o igual a 8.

#<=

V1= 5
V2= 7
VT= V1<=V2
print(VT)   
    #Dará verdadero ya que 7 es mayor que 5 y no es igual.

V1= 7
V2= 7
VT= V1<=V2
print(VT)   
    #Dará Verdadero ya que son iguales.

V1= 7
V2= 2
VT= V1<=V2
print(VT)
    #Dará falso ya que son 2 no puede ser mayor que 7 y tampoco es igual.
