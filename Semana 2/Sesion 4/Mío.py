"""Las personas adscritas a la jubilación por
antiguedad adulta deben tener 60 años o más
y una antiguedad en su empleo de 25 años o más.
Determinar en qué tipo de jubilación, quedará
adscrita una persona."""

edad= int(input("Ingrese su edad: "))
empleo= int(input("¿Cuántos años de antiguedad tiene su empresa? "))

if edad>=60 and empleo< 25:
	print("Usted quedará inscrito en la jubilación por edad")
elif edad <60 and empleo>=25:
	print("Usted quedará inscrito a la jubilación por antiguedad joven")
elif edad>=60 and empleo>=25:
	print("Usted quedaráinscrito a la jubilación por antiguedad adulta")
else:
	print("Usted aún no se jubila")