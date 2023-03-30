import unittest
from Ejercicios import Ejercicio3 as ej3
from Ejercicios import Ejercicio4 as ej4


class TestEjercicios(unittest.TestCase):

    def test_calificacion(self):
        self.assertEqual(ej3.Alumno("Juan", 7).calificacion(), "El alumno Juan ha aprobado")
        self.assertEqual(ej3.Alumno("Pedro", 4).calificacion(), "El alumno Pedro ha suspendido")
        self.assertEqual(ej3.Alumno("Maria", 6).calificacion(), "El alumno Maria ha aprobado")

    def test__str__(self):
        self.assertEqual(ej4.Alumno("Juan", 7).__str__(), "El alumno Juan tiene una nota de 7")
        self.assertEqual(ej4.Alumno("Pedro", 4).__str__(), "El alumno Pedro tiene una nota de 4")
        self.assertEqual(ej4.Alumno("Maria", 6).__str__(), "El alumno Maria tiene una nota de 6")


if __name__ == '__main__':
    unittest.main()