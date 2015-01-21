'''
Created on 19/01/2015

@authors:     Genessis Sanchez 11-10935
              Gustavo Gutierrez 11-10428
'''
import unittest
from Reserva import *
from datetime import MINYEAR
from datetime import MAXYEAR

class TestCalcularPrecio(unittest.TestCase):
        
    # Tests de frontera sobre la entrada  
    # Casos unica tarifa
    def testLimiteInferiorDiariaConNocturna(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,6,1),
                                        datetime.datetime(2015,1,19,8,15),
                                        Tarifa(50,60)), 150)
    def testLimiteSuperiorDiariaConNocturna(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,14,23),
                                        datetime.datetime(2015,1,19,17,59),
                                        Tarifa(50,60)), 200)
    def testLimiteInferiorNocturnaConDiaria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,18,1),
                                        datetime.datetime(2015,1,20,0,0),
                                        Tarifa(50,60)), 360)
    def testLimiteSuperiorNocturnaConDiaria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,0,0),
                                        datetime.datetime(2015,1,19,5,59),
                                        Tarifa(50,60)), 360)
    # Casos con uso de las dos tarifas (hibridos)
    def testLimiteInferiorDiurnaANocturna(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,6,1),
                                        datetime.datetime(2015,1,19,18,50),
                                        Tarifa(10,20)), 150)
    def testLimiteSuperiorDiurnaANocturna(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,17,59),
                                        datetime.datetime(2015,1,20,7,59),
                                        Tarifa(10,20)), 270)
    def testLimiteInferiorNocturnaADiaria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,18,1),
                                        datetime.datetime(2015,1,20,7,19),
                                        Tarifa(10,20)), 260)
    def testLimiteSuperiorNocturnaADiaria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,5,59),
                                        datetime.datetime(2015,1,19,16,47),
                                        Tarifa(10,20)), 120)
      # Casos limites de la libreria
    def testMinimoLibreria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(MINYEAR,1,1,0,0),
                                        datetime.datetime(MINYEAR,1,1,1,2),
                                        Tarifa(50,60)), 120)
    def testMaximoLibreria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(MAXYEAR,12,28,23,59),
                                        datetime.datetime(MAXYEAR,12,31,23,59),
                                        Tarifa(50,60)), 3990)
    # Caso tarifa unitaria
    def testTarifaDiariaUnitaria(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,6,10),
                                        datetime.datetime(2015,1,19,19,18),
                                        Tarifa(1,1)), 14)
        
    # Tests de frontera sobre la salida (maxima y minima)
    def testQuinceMinutosDia(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,14,0),
                                        datetime.datetime(2015,1,19,14,15),
                                        Tarifa(50,60)), 50)

    # Casos unica tarifa tocando las fronteras

    def testFronteraSuperiorDiaria(self):
    	self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,17,0),
    									datetime.datetime(2015,1,19,18,0),
    									Tarifa(50,70)), 50)

    def testFronteraInferiorDiaria(self):
    	self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,6,0),
    									datetime.datetime(2015,1,19,7,0),
    									Tarifa(50,70)), 50)

    def testFronteraInferiorNocturna(self):
    	self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,18,0),
    									datetime.datetime(2015,1,19,19,0),
    									Tarifa(70,50)), 50)

    def testFronteraSuperiorNocturna(self):
    	self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,5,0),
    									datetime.datetime(2015,1,19,6,0),
    									Tarifa(70,50)), 50)    


    # Validacion de entrada

    def testFechasInvalidas(self):
    	self.assertRaises(ValueError, calcularPrecio, 
    									 datetime.datetime(2015,1,20,12,0),
    									 datetime.datetime(2015,1,19,12,0),
    									 Tarifa(50,60))

    def testTiempoReservaMinimo(self):
    	self.assertRaises(ValueError, calcularPrecio, 
    									 datetime.datetime(2015,1,19,12,0),
    									 datetime.datetime(2015,1,19,12,1),
    									 Tarifa(50,60))

    def testTiempoReservaMaximo(self):
    	self.assertRaises(ValueError, calcularPrecio, 
    									 datetime.datetime(2015,1,19,12,0),
    									 datetime.datetime(2015,1,22,12,1),
    									 Tarifa(50,60))

    def testTarifasInvalidas(self):
    	self.assertRaises(ValueError, calcularPrecio, 
    									 datetime.datetime(2015,1,19,12,0),
    									 datetime.datetime(2015,1,19,12,20),
    									 Tarifa(-50,60))

    def testQuinceMinutosNoche(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,19,0),
                                        datetime.datetime(2015,1,19,19,15),
                                        Tarifa(50,60)), 60)
    def testMaximoSetentayDosHoras(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,10,17,55),
                                        datetime.datetime(2015,1,13,17,55),
                                        Tarifa(50,60)), 3990)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
