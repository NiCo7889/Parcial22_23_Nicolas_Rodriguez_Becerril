"""
Copia el ejercicio anterior y realicemos una modificación:

Junto al método init y calificación, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y 
debe tener el siguiente formato:

def __str__(self): return "Lo que quiero mostrar"

Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), 
Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

Experiemntación:
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
"""


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno {self.nombre} ha sido creado con éxito")

    def __str__(self):
        return f"El alumno {self.nombre} tiene una nota de {self.nota}"
    
    def calificacion(self):
        if self.nota >= 5:
            return f"El alumno {self.nombre} ha aprobado"
        else:
            return f"El alumno {self.nombre} ha suspendido"
        

import unittest

class TestEjercicios(unittest.TestCase):

    def test__str__(self):
        self.assertEqual(Alumno("Juan", 7).__str__(), "El alumno Juan tiene una nota de 7")
        self.assertEqual(Alumno("Pedro", 4).__str__(), "El alumno Pedro tiene una nota de 4")
        self.assertEqual(Alumno("Maria", 6).__str__(), "El alumno Maria tiene una nota de 6")


if __name__ == "__main__":

    unittest.main()
    alumno1 = Alumno("Juan", 7)
    print(alumno1)
    print(alumno1.calificacion(), "\n")

    alumno2 = Alumno("Pedro", 4)
    print(alumno2)
    print(alumno2.calificacion(), "\n")
    
    alumno3 = Alumno("Maria", 6)
    print(alumno3)
    print(alumno3.calificacion())