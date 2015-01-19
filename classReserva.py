'''

Creado en 18/01/2015

Autores: Gustavo Gutierrez 11-10428
         Genessis Sanchez  11-10935
         
'''
import datetime



def calcularPrecio(Inicio, Fin, Tarifas):
	if not(isinstance(Inicio,datetime.datetime)):
		raise ValueError('Argumento Inicio debe ser objecto datetime.')

calcularPrecio(hola,chao,jeje)