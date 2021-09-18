Entrada="""
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para
erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como parte
de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de acción por
el clima y una de sus metas busca mejorar la educación, la sensibilización y la
capacidad humana e institucional respecto de la mitigación del cambio climático, la
adaptación a él, la reducción de sus efectos y la alerta temprana.

Debido a esto, el Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM)
desea que usted construya un sistema para el cálculo del Índice de Calidad del Aire (ICA)
generado por el agente contaminante NO2 1h obtenida mediante la medición de un
sensor, para así generar una alerta temprana a las zonas más vulnerables en pos del
mejoramiento de la calidad de vida de los ciudadanos.

Para ello, el sistema debe recibir como entrada el valor de la concentración de NO2 1h en
ppm y mostrar por pantalla el ICA truncado a 2 cifras decimales y la alerta
correspondiente separados por un espacio.

La fórmula para calcular el ICA es la siguiente:

"""
c=float(input("Digite el valor de la concentración: "))


# C Il
# I h BPl BPh
# [0 – 0.054) 0 50 0 0.053
# [0.054 – 0.101) 51 100 0.054 0.100
# [0.101 – 0.361) 101 150 0.101 0.360
# [0.361 – 0.650) 151 200 0.361 0.649
# [0.650 – 1.250) 201 300 0.650 1.249
# [1.250 – 1.650) 301 400 1.250 1.649
# [1.650 – 2.050) 401 500 1.650 2.049

if c>=0 and c<=0.054:
    ii=0 
    ih=50 
    bpi=0  
    bph=0.053
elif c>=0.054 and c<=0.101:
    ii=51 
    ih=100
    bpi=0.054
    bph=0.100
elif c>=0.101 and c<=0.361:
    ii=101  
    ih=150  
    bpi=0.101 
    bph=0.360
if c>=0.361 and c<=0.650:
    ii=151  
    ih=200  
    bpi=0.361 
    bph=0.649
if c>=0.650 and c<=1.250:
    ii=201 
    ih=300 
    bpi=0.650 
    bph=1.249
if c>=1.250 and c<=1.650:
    ii=301 
    ih=400 
    bpi=1.250 
    bph=1.649
if c>=1.650 and c<=2.050:
    ii=401 
    ih=500 
    bpi=1.650 
    bph=2.049

ica=(((ih-ii)/(bph-bpi))*(c-bpi)+ii)

if (ica>=0) and (ica<=50):
    print(f"{ica:.2f}", "Verde")
elif (ica>=50) and (ica<=100):
    print(f"{ica:.2f}","Amarillo")
elif (ica>=100) and (ica<=150):
    print(f"{ica:.2f}""Naranja")
elif (ica>=150) and (ica<=200):
    print(f"{ica:.2f}","Rojo")
elif (ica>=200) and (ica<=300):
    print(f"{ica:.2f}","Morado")
elif (ica>=300):
    print(f"{ica:.2f}","Marron")
else: 
    print("-1 error en los datos ingrese valores correctos")

#Valores maximos de tabla

# ICA Alerta
# [0 – 50] verde
# (50 – 100] amarillo
# (100 – 150] naranja
# (150 – 200] rojo
# (200 – 300] morado
# > 300 marron