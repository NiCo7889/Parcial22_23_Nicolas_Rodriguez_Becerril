"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa
"""


# FORMA ITERATIVA


def determinante_manera_iterativa(Matriz1):
    aux = 0 # aux es la variable que almacena el resultado del determinante
    for o in range(0, size): # o es la variable que recorre las filas de la matriz
        temp = 1 # temp es la variable que almacena el resultado de la multiplicación de los elementos de la fila
        k = o # k es la variable que recorre las columnas de la matriz
        for i in range(0, size): # i es la variable que recorre las filas de la matriz
            temp *= Matriz1[i][k] # Multiplicar los elementos de la fila
            k += 1  # Incrementar k en 1
            if k == size: # Si k es igual al tamaño de la matriz
                k = 0 # k es igual a 0
        aux += temp # Sumar el resultado de la multiplicación de los elementos de la fila

    for o in range(size-1, -1, -1): # o es la variable que recorre las filas de la matriz
        temp = 1 # temp es la variable que almacena el resultado de la multiplicación de los elementos de la fila
        k = o # k es la variable que recorre las columnas de la matriz
        for i in range(0, size): # i es la variable que recorre las filas de la matriz
            temp *= Matriz1[i][k] # Multiplicar los elementos de la fila
            k -= 1 # Decrementar k en 1
            if k == -1: # Si k es igual a -1
                k = size - 1 # k es igual al tamaño de la matriz - 1
        aux -= temp # Restar el resultado de la multiplicación de los elementos de la fila
    return aux # Devolver el resultado del determinante

Matriz1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]] # Matriz1
size = len(Matriz1) # El tamaño de la Matriz1


if __name__ == "__main__":

    print("Matriz1: ", Matriz1)
    print("El determinante de la 5x5 calculado de manera iterativa es: ", determinante_manera_iterativa(Matriz1))