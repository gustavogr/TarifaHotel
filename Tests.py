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
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()