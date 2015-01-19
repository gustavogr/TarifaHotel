'''

Creado en 18/01/2015

Autores: Gustavo Gutierrez 11-10428
         Genessis Sanchez  11-10935
         
'''
import datetime
from decimal import *

class Tarifa(object):
	"""Objeto que maneja las tarifas de dia y de noche de una reserva"""
	def __init__(self, tarifaDia, tarifaNoche):
		super(Tarifa, self).__init__()
		self.dia = Decimal(tarifaDia)
		self.noche = Decimal(tarifaNoche)
	def __str__(self):
		return 'Dia: '+str(self.dia)+' Noche: '+str(self.noche)


def calcularPrecio(Inicio, Fin, Tarifas):
	if not(isinstance(Inicio,datetime.datetime)):
		raise TypeError('Argumento Inicio debe ser objeto datetime.')
	if not(isinstance(Fin,datetime.datetime)):
		raise TypeError('Argumento Fin debe ser objeto datetime.')
	if not(isinstance(Tarifas,Tarifa)):
		raise TypeError('Argumento Tarifas debe ser objeto Tarifa.')
	delta = Fin - Inicio
	horas = int(delta.total_seconds()//3600)
	minutos = int(delta.total_seconds()%3600//60)
	if Inicio > Fin:
		raise ValueError('La fecha de inicio debe ser menor a la fecha final.')
	if horas > 72 or (horas == 72 and minutos > 0):
		raise ValueError('La reserva debe ser menor o igual a 72 horas.')
	if horas < 0 or (horas == 0 and minutos < 15):
		raise ValueError('La reserva debe ser mayor o igual a 15 minutos.')



if __name__ == '__main__':
	ini = datetime.datetime(2015,11,2,17)
	fin = datetime.datetime(2015,11,5,17,1)
	t = Tarifa(50,60)
	calcularPrecio(fin,ini,t)