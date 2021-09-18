menu= """
Bienvenido al conversor de monedas 😊

1 Pesos Colombianos
2 Pesos mexicanos
3 Pesos argentinos

Elige una opción del 1 al 3: """

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
    Valor_dolar= 20
    PxD= opcion/Valor_dolar
    PxD= round(PxD, 2)
    PxD= str(PxD)
    print("Usted tiene ", PxD, " dolares")
elif opcion == "3":
    opcion= input("Inserte la cantidad de pesos argentinos ")
    opcion= float(opcion)
    Valor_dolar= 95
    PxD= opcion/Valor_dolar
    PxD= round(PxD, 2)
    PxD= str(PxD)
    print("Usted tiene ", PxD, " dolares")
else: 
    print("Por favor ingrese un valor válido ")