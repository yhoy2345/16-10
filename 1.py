import numpy as np
print(np.delete(np.array([input(f"Ingrese los numeros en la fila {i+1}: ").split() for i in range(4)], int), 2, axis=1))
