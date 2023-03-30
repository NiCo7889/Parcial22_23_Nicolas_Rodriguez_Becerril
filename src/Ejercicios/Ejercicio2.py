"""
Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y -1 si 145 no está en la lista
"""


class Listanumeros:
    def __init__(self, lista):
        self.lista = lista

    def imprimir_multiplos(self):
        multiplos = []
        for numero in self.lista:
            if numero > 300:
                break
            if numero % 10 == 0 and numero < 200:
                multiplos.append(numero)
        return multiplos

    def ordenar_lista(self):
        self.lista = self.mergesort(self.lista)
        return self.lista

    def mergesort(self, lista):
        # Método de ordenamiento mergesort
        if (len(lista) <= 1):
            return lista
        else:
            medio = len(lista) // 2
            izquierda = []
            for i in range(0, medio):
                izquierda.append(lista[i])
            derecha = []
            for i in range(medio, len(lista)):
                derecha.append(lista[i])
            izquierda = self.mergesort(izquierda)
            derecha = self.mergesort(derecha)
            if (izquierda[medio-1] <= derecha[0]):
                izquierda += derecha
                return izquierda
            resultado = self.merge(izquierda, derecha)
            return resultado

    def merge(self, izquierda, derecha):
        # Función para ordenar listas
        lista_mezclada = []
        while (len(izquierda) > 0) and (len(derecha) > 0):
            if (izquierda[0] < derecha[0]):
                lista_mezclada.append(izquierda.pop(0))
            else:
                lista_mezclada.append(derecha.pop(0))
        if (len(izquierda) > 0):
            lista_mezclada += izquierda
        if (len(derecha) > 0):
            lista_mezclada += derecha
        return lista_mezclada

    def encontrar_indice(self, valor):
        if valor in self.lista:
            return self.lista.index(valor)
        else:
            return -1


if __name__ == "__main__":
    # Creamos una instancia de Listanumeros con una lista de números
    numeros = Listanumeros([18, 50, 210, 80, 145, 333, 70, 30])

    # Imprimimos los múltiplos de 10 menores a 200
    print(numeros.imprimir_multiplos())

    # Ordenamos la lista usando el método mergesort
    numeros.ordenar_lista()

    # Imprimimos la lista ordenada
    print(numeros.lista)

    # Buscamos el índice del número 145 en la lista
    indice = numeros.encontrar_indice(145)
    if indice != -1:
        print("El número 145 está en la posición", indice, "de la lista.")
    else:
        print("El número 145 no está en la lista.")