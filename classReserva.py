'''

Creado en 18/01/2015

Autores: Gustavo Gutierrez 11-10428
         Genessis Sanchez  11-10935
         
'''
import datetime

class Tarifa(object):
	"""Objeto que maneja las tarifas de dia y de noche de una reserva"""
	def __init__(self, tarifaDia, tarifaNoche):
		super(Tarifa, self).__init__()
		self.dia = tarifaDia
		self.noche = tarifaNoche
	def __str__(self):
		return 'Dia: '+str(self.dia)+' Noche: '+str(self.noche)
	

def calcularPrecio(Inicio, Fin, Tarifas):
	if not(isinstance(Inicio,datetime.datetime)):
		raise ValueError('Argumento Inicio debe ser objecto datetime.')
	if not(isinstance(Fin,datetime.datetime)):
		raise ValueError('Argumento Fin debe ser objecto datetime.')
	if not(isinstance(Tarifas,Tarifa)):
		raise ValueError('Argumento Tarifas debe ser objecto Tarifa.')
	print(Inicio,Fin,Tarifas)
	delta = Fin - Inicio
	print(type(delta),delta)




if __name__ == '__main__':
	ini = datetime.datetime(2015,11,4,16,59)
	fin = datetime.datetime(2015,11,2,17,13)
	t = Tarifa(50,60)
	calcularPrecio(ini,fin,t)