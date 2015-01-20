'''

Creado en 18/01/2015

Autores: Gustavo Gutierrez 11-10428
         Genessis Sanchez  11-10935
         
'''
import datetime
import decimal

class Tarifa(object):
	"""Objeto que maneja las tarifas de dia y de noche de una reserva"""
	def __init__(self, tarifaDia, tarifaNoche):
		self.dia = decimal.Decimal(tarifaDia)
		self.noche = decimal.Decimal(tarifaNoche)
	def __str__(self):
		return 'Dia: '+str(self.dia)+' Noche: '+str(self.noche)


def cualTarifa(hora,minuto):
	if (hora == 6 or hora == 18) and minuto == 0:
		return ''
	elif 6 <= hora and hora < 18:
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
	while horas > 0 or (horas == 0 and minutos > 0):
		if horas == 0:
			if (mActual + minutos) % 60 < mActual:
				hActual = (hActual + 1) % 24 
				mActual = (mActual + minutos) % 60
			else:
				mActual = mActual + minutos
			minutos = 0
		else:
			hActual = (hActual + 1) % 24
			horas -= 1
		tActual = cualTarifa(hActual,mActual)
		if tActual == tAnt or tActual == '':
			suma += getattr(tarifas,tAnt)
		elif tAnt == '':
			suma += getattr(tarifas,tActual)
		else:
			suma += max(tarifas.dia,tarifas.noche)
		tAnt = tActual
	return suma


if __name__ == '__main__':
	try:	
		anioi = int(input('Introduzca anyo de inicio de la reserva: '))
		mesi = int(input('Introduzca mes de inicio de la reserva: '))
		diai = int(input('Introduzca dia de inicio de la reserva: '))
		horai = int(input('Introduzca hora de inicio de la reserva: '))
		minutoi = int(input('Introduzca los minutos de la hora de inicio de la reserva: '))
		aniof = int(input('Introduzca anyo final de la reserva: '))
		mesf = int(input('Introduzca mes final de la reserva: '))
		diaf = int(input('Introduzca dia final de la reserva: '))
		horaf = int(input('Introduzca hora final de la reserva: '))
		minutof = int(input('Introduzca minuto final de la reserva: '))
		dia = int(input('Introduzca la tarifa diurna: '))
		noche = int(input('Introduzca la tarifa nocturna: '))
		t = Tarifa(dia,noche)
	except ValueError:
		print('El valor debe ser un entero.')
		raise SystemExit
	try:
		ini = datetime.datetime(anioi,mesi,diai,horai,minutoi)
	except ValueError as err:
		print('Error creando objeto datetime "inicio": ',err)
		raise SystemExit
	try:	
		fin = datetime.datetime(aniof,mesf,diaf,horaf,minutof)
	except ValueError as err:
		print('Error creando objeto datetime "fin": ',err)
		raise SystemExit


	print(calcularPrecio(ini,fin,t))


