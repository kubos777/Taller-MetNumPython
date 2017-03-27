import math


def f(x):
    #Funcion a retornar, esta es la línea que estará cambiando para cualquier función
    #return  5 * x * math.e**(-2*x)
    #return x**3 - x**2
    
def main():
    print("Extrapolación de Richardson")
    #Obtenemos el valor correspondiente al punto a saber de la derivada
    x_1 = float(input("Dame el valor de x: "))
    #Valor de nuestro Delta_h
    h_1 = float(input("Dame un valor para h: "))

    h_2 = h_1/2
    #Calculamos el valor de la f_1
    f_1 = (f(x_1+h_1)-f(x_1-h_1)) /(2*h_1)
    print("El valor de f_1 es: %2.5f" %(f_1))


    #Calculamos el valor de la f_2
    f_2 = (f(x_1+h_2)-f(x_1-h_2)) /(2*h_2)
    print("El valor de f_2 es: %2.5f" %(f_2))

    f_t = f_2 + (f_2 - f_1) / 3

    print("El valor de la derivada en el punto %2.2f es: %2.5f " %(x_1,f_t))

if __name__ == '__main__':
        main()
