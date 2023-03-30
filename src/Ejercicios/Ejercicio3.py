"""
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota

Experiemntación:
Crea algunos alumnos
Prueba a ejecutar el método calificación de cada objeto que has creado
"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno {self.nombre} ha sido creado con éxito")
    
    def calificacion(self):
        if self.nota >= 5:
            return f"El alumno {self.nombre} ha aprobado"
        else:
            return f"El alumno {self.nombre} ha suspendido"


import unittest

class TestEjercicios(unittest.TestCase):

    def test_calificacion(self):
        self.assertEqual(Alumno("Juan", 7).calificacion(), "El alumno Juan ha aprobado")
        self.assertEqual(Alumno("Pedro", 4).calificacion(), "El alumno Pedro ha suspendido")
        self.assertEqual(Alumno("Maria", 6).calificacion(), "El alumno Maria ha aprobado")

if __name__ == "__main__":

    unittest.main()
    alumno1 = Alumno("Juan", 7)
    print(alumno1.calificacion(), "\n")

    alumno2 = Alumno("Pedro", 4)
    print(alumno2.calificacion(), "\n")

    alumno3 = Alumno("Maria", 6)
    print(alumno3.calificacion())