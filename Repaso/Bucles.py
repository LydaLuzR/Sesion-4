"""Esta es una forma rápida de hacer un minibucle, el problema es que es manual"""
"""
contador = 1
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

contador = 2
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

contador = 4
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

contador = 6
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

contador = 8
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

"""


def run():
    LIMITE = 1000000
    contador = 0
    pontencia_2 = 2**contador
    while pontencia_2 < LIMITE:
        print(f'2 elevado a la {contador} es igual a {pontencia_2}')
        contador = contador + 1
        pontencia_2 = 2**contador

if __name__ == "__main__":
    run()


#Bucle pero ahora con suma

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