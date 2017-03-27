r = eval(input("Ingresa el valor del grado r: "))
x = list(eval(input("Ingrese los valores de X separados por comas: ")))
y = list(eval(input('Ingrese los valores de Y separados por comas : ')))
X = float(eval(input(' Ingrese el valor de px: ')))
print(x)
print(y)
print(X)
px = 0
for i in range(r + 1):
    l = y[i]
    for j in range(r + 1):
        if j != i:
            l = l * ((X - x[j]) / (x[i] - x[j]))
        px = px + l
print (px)