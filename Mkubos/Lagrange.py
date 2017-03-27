#Metodo de interpolacion de Lagrange
#Estimar un valor teniendo otros dos
# -*- coding: utf-8 -*-
def treson():
	grado=eval(input("Ingresa el grado del polinomio: ")) #Grado del polinomio
	x=list(eval(input("Ingresa los valores en x separados por comas: "))) #Valores en x		
	y=list(eval(input("Ingresa los valores en f(x) separados por comas: "))) #Valores en y
	xint=eval(input("Ingresa el valor en x a interpolar: "))#Valor a interpolar

	pint=0
	i=0

	while i<=len(x)-1:
		L=1
		j=0
		while j<=len(x)-1:
			if i != j:
				L=L*((xint-x[j])/(x[i]-x[j]))
			j=j+1
		pint=pint+L*y[i]
		i=i+1
	print(pint)
	return 0

def dospuntos():

	grado=eval(input("Ingresa el grado del polinomio: ")) #Grado del polinomio
	x=list(eval(input("Ingresa los valores en x separados por comas: "))) #Valores en x		
	y=list(eval(input("Ingresa los valores en f(x) separados por comas: "))) #Valores en y
	xint=eval(input("Ingresa el valor en x a interpolar: "))#Valor a interpolar

	pint=0
	i=0

	while i<len(x)-1:
		L=1
		j=0
		while j<len(x)-1:
			if i != j:
				L=L*((xint-x[j])/(x[i]-x[j]))
			j=j+1
		pint=pint+L*y[i]
		i=i+1
	print(pint)
	return 0

def principal():

	print("\n\n\tInterpolación de Lagrange")
	print("\n1)Interpolar por dos puntos\n2)Interpolar por n puntos\n3)Salir")
	opcion=int(input("\n\t\t¿Elige la opción que deseas realizar?: "))

	if opcion==1:
		dospuntos()

	elif opcion==2:
		treson()

	elif opcion==3:
		print("\n\n\tHasta la vista baby")
		exit()
	else:
		principal()
principal()	

