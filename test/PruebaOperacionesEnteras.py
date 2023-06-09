import unittest
from src.logica.OperacionesEnteras import OperacionesEnteras

class PruebaOperacionesEnteras(unittest.TestCase):
    def setUp(self):
        self.operacion = PruebaOperacionesEnteras()

    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

        def test_MCDRecursivo_dosNumerosPositivos_retornaMCD(self):

        # Arrange
        numero1 = 15
        numero2 = 20
        resultadoEsperado = 5
        # Do
        resultadoActual = self.operacion.MCD_recursivo(numero1, numero2)
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
    class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):

    # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
    def test_MCD_tresNumerosPositivos_retornaMCD(self):

        # Arrange
        numero1 = 24679
        numero2 = 20387
        numero3 = 16169
        resultadoEsperado = 37
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

