import numpy as np

a = np.array([list(map(int, input("Ingrese la fila {} de la primera matriz: ".format(i+1)).split())) for i in range(3)])
b = np.array([list(map(int, input("Ingrese la fila {} de la segunda matriz: ".format(i+1)).split())) for i in range(3)])

print("Primera matriz:\n", a)
print("Segunda matriz:\n", b)
resultado = a * b
print("Resultado de la multiplicación:\n", resultado)


