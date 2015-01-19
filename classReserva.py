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


def cualTarifa(hora,minuto):
	if 6 < hora and hora < 18:
		return 'dia'
	elif (hora == 6 and minuto > 0) or (hora == 18 and minuto == 0):
		return 'dia'
	else:	
		return 'noche'


def calcularPrecio(inicio, fin, tarifas):
	if not(isinstance(inicio,datetime.datetime)):
		raise TypeError('Argumento inicio debe ser objeto datetime.')
	if not(isinstance(fin,datetime.datetime)):
		raise TypeError('Argumento fin debe ser objeto datetime.')
	if not(isinstance(tarifas,Tarifa)):
		raise TypeError('Argumento tarifas debe ser objeto Tarifa.')
	delta = fin - inicio
	horas = int(delta.total_seconds()//3600)
	minutos = int(delta.total_seconds()%3600//60)
	if inicio > fin:
		raise ValueError('La fecha de inicio debe ser menor a la fecha final.')
	if horas > 72 or (horas == 72 and minutos > 0):
		raise ValueError('La reserva debe ser menor o igual a 72 horas.')
	if horas < 0 or (horas == 0 and minutos < 15):
		raise ValueError('La reserva debe ser mayor o igual a 15 minutos.')
	if tarifas.dia <= 0 or tarifas.noche <= 0:
		raise ValueError('Las tarifas deben ser positivas.')

	hActual = inicio.hour
	mActual = inicio.minute
	suma = 0
	tAnt = cualTarifa(hActual,mActual)
	while horas > 0 or (horas = 0 and minutos > 0):
		if horas == 0:
			if (mActual + minutos) % 60 < mActual:
				hActual += 1
				mActual = (mActual + minutos) % 60
			else:
				mActual = mActual + minutos
				minutos = 0
		else:
			hActual += 1
			horas -= 1
		tActual = cualTarifa(hActual,mActual)
		if tActual != tAnt:
			suma += max(tarifas.dia,tarifas.noche)
			tAnt == tActual



if __name__ == '__main__':
	ini = datetime.datetime(2015,11,2,17)
	fin = datetime.datetime(2015,11,5,17,1)
	t = Tarifa(50,60)
	calcularPrecio(fin,ini,t)