
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

#Ejemplos con While 

contador= 1
print(contador)
while contador<1000:
    contador=contador+1
    contador+=1
    print(contador)
