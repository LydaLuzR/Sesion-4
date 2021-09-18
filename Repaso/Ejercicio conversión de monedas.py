
P= input("Inserte la cantidad de pesos colombianos ")
P= float(P)
Valor_dolar= 3685
PxD= P/Valor_dolar
PxD= round(PxD, 2)
PxD= str(PxD)
print("Usted tiene ", PxD, " dolares")

D= float(input("Inserte la cantidad de dolares "))
Valor_peso_Colombiano= 0.00027
PxD= D/Valor_peso_Colombiano
PxD= round(PxD,2) 
PxD= str(PxD)
print("Usted tiene ", PxD, " pesos colombianos")

#Conversor más juerte

menu= """
Bienvenido al conversor de monedas 😊

1 Pesos Colombianos
2 Pesos mexicanos
3 Pesos argentinos

Elige una opción: """

opcion= input(menu)
if opcion == "1":
    opcion= float(input("Inserte la cantidad de pesos colombianos "))
    Valor_dolar= 3685
    PxD= opcion/Valor_dolar
    PxD= round(PxD, 2)
    PxD= str(PxD)
    print("Usted tiene ", PxD, " dolares")
elif opcion == "2":
    opcion= input("Inserte la cantidad de pesos mexicanos ")
    opcion= float(opcion)
    Valor_dolar= 19,90
    PxD= opcion/Valor_dolar
    PxD= round(PxD, 2)
    PxD= str(PxD)
    print("Usted tiene ", PxD, " dolares")
elif opcion == "3":
    opcion= input("Inserte la cantidad de pesos argentinos ")
    opcion= float(opcion)
    Valor_dolar= 94,20
    PxD= opcion/Valor_dolar
    PxD= round(PxD, 2)
    PxD= str(PxD)
    print("Usted tiene ", PxD, " dolares")
else: 
    print("Por favor ingrese un valor válido ")


#Conversor con Def

def conversor(tipo_pesos, valor_dolar):
    pesos= input("Inserte la cantidad de pesos " +  tipo_pesos + " que tienes: ")
    pesos= float(pesos)
    valor_dolar= 3685
    PxD= pesos/valor_dolar
    PxD= round(PxD, 2)
    PxD= str(PxD)
    print("Usted tiene ", PxD, " dolares")

menu="""
Bienvenido al conversor de monedas 😊

1 Pesos Colombianos
2 Pesos mexicanos
3 Pesos argentinos

Elige una opción: """

    
opcion= int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3685)
elif opcion == 2:
    conversor("Mexicanos", 19,90)
elif opcion == 3:
    conversor("Argentinos", 94,20)
else:
    print("Ingrese una opción válida")