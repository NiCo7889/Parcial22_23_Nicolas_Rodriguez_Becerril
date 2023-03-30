"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa.
"""


# FORMA RECURSIVA

import copy # Importamos la librería copy para poder hacer copias de objetos como diccionarios y listas. En este caso se hace uso del mismo para hacer copias de matrices 
# y poder trabajar con ellas sin modificar la matriz original.

class nodoPila(object):
    # Clase nodo pila
    def __init__(self, valor):
        self.info = valor
        self.sig = None

class Pila(object):
    # Clase pila
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo = nodoPila(valor)
        nuevo.sig = self.cima
        self.cima = nuevo

    def desapilar(self):
        valor = self.cima.info
        self.cima = self.cima.sig
        return valor

    def pila_vacia(self):
        return self.cima == None

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for i in range(self.filas):
            self.matriz.append([0] * self.columnas)

    def __str__(self):
        return str(self.matriz)

def determinante_manera_recursiva(Matriz, total=0):
    """
    Función para el cálculo recursivo del determinante de cualquier matriz cuadrada.
    """
    tamaño = list(range(len(Matriz))) # tamaño que tendrá la matriz

    if len(Matriz) == 2 and len(Matriz[0]) == 2: # Si la matriz es de 2x2
        val = Matriz[0][0] * Matriz[1][1] - Matriz[1][0] * Matriz[0][1] # Calculamos el determinante
        return val # Devolvemos el determinante

    for fc in tamaño: # Para cada columna de la matriz ...
        As = copy.deepcopy(Matriz)  # haz una copia, y ...
        As = As[1:] # ... elimina la primera fila
        height = len(As) # Altura de la matriz

        for i in range(height):  # Para cada fila de la submatriz ...
            As[i] = As[i][0:fc] + As[i][fc+1:] # elimina la columna de la matriz

        sign = (-1) ** (fc % 2)  # Alternar signos para el multiplicador de la submatriz
        sub_det = determinante_manera_recursiva(As)  # Pasar submatriz recursivamente
        total += sign * Matriz[0][fc] * sub_det # Total de todos los retornos de la recursión

    return total # Devolvemos el determinante

if __name__ == "__main__":
# Introductimos el tamaño de la matriz
    n = 5
    # Creamos una matriz cuadrada random de tamaño nxn
    Matriz = [[0] * n for i in range(n)]

    # Rellenamos la matriz con valores aleatorios
    import random

    for i in range(n):
        for j in range(n):
            Matriz[i][j] = random.randint(-10, 10)

    # Imprimimos la matriz
    print("Matriz: ")
    for i in range(n):
        for j in range(n):
            print(Matriz[i][j], end=" ")
        print()

    # Si quiero calcular una matriz concreta 5x5
    # Matriz = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    # Calculamos el determinante de la matriz
    determinante = determinante_manera_recursiva(Matriz)
    print("Resultado del determinante de la matriz 5x5 calculado de manera recursiva: ", determinante)