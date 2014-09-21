#!/usr/bin/python

import numpy as np
import os
import math

ruta = raw_input("Ruta del archivo >> ")
print "La ruta dada fue >> ", ruta

archivo = open(ruta,"r")
datos = np.loadtxt(archivo)
media = datos.mean()
dmm = datos - media

def varianza(sec, prom):
	suma = 0
	for i in np.nditer(sec):
		suma += i**2
	return (suma - len(sec) * prom**2) / (len(sec) - 1)

var = varianza(datos, media)
desv = math.sqrt(var)

def nr1(sec, _media, _desv):
	print "Regla 1"
	suma_nr1 = []
	for i in np.nditer(sec):
		if ( (i > media + _desv*3) | (i < media - _desv*3) ): suma_nr1.append(i) 
	if ( len(suma_nr1) != 0 ): print "Regla 1. Valores >> " + str(suma_nr1)
	
def nr2(_sec,_dmm):
    print "Regla 2"
    grupos_neg = np.where( _dmm < 0 )[0]
    grupos_pos = np.where( _dmm > 0 )[0]
    consec_neg = np.array_split(grupos_neg, np.where(np.diff( grupos_neg )!=1)[0]+1)
    consec_pos = np.array_split(grupos_pos, np.where(np.diff( grupos_pos )!=1)[0]+1)
    imp_nr(consec_pos, _sec, 9)
    imp_nr(consec_neg, _sec, 9)


def imp_nr( _consec, _sec, puntos):
	for i in range(len(_consec)):
		if ( len(_consec[i] ) >= puntos ):
			for h in range( len( _consec[i] ) ):
				print str(_sec[_consec[i][h]])
				
def nr3(_sec):
    print "Regla 3"
    tendencia = [b - a for a, b in zip(_sec[::1], _sec[1::1])]
    grupos_pos = np.where( np.array(tendencia) > 0 )[0]
    consec_pos = np.array_split(grupos_pos, np.where(np.diff( grupos_pos )!=1)[0]+1)
    for i in range( len(consec_pos) ):
		if ( len(consec_pos[i]) >= 5 ):
			print "\n"
			for h in range( len(consec_pos[i]) ):
				print str( _sec[ consec_pos[i][h] ] )
			print _sec[ consec_pos[i][h] + 1 ]
			
def nr4(_sec, _dmm):
    print "Regla 4"
    posit = True
    arreglo = []
    resultado = []
    for i in range(len(_dmm)):
		if ( (_dmm[i] > 0) & (posit == True) ):
			arreglo.append(_sec[i])
			posit = False
		elif ( (_dmm[i] < 0) & (posit == False) ):
			arreglo.append( _sec[i] )
			posit = True 
		elif ( ( (_dmm[i] < 0) & (posit == True ) ) | ( (_dmm[i] > 0) & (posit == False ) ) ):
			if ( len(arreglo) >= 14 ): print "Relga 4 >> " + str(arreglo)
			#resultado.append(arreglo)
			#print resultado
			for h in arreglo[:]:
				arreglo.remove(h)	
			arreglo.append(_sec[i])
			#print arreglo
    if ( len(arreglo) >= 14 ): print "Relga 4 >> " + str(arreglo)
	#print "FINAL >> " + str(resultado)
	#resultado.append(arreglo)
	#print "FINAL >> " + str(resultado)

def nr5(_desv, _media, _sec):
    print "Regla 5"
    grupos_pos = np.where( _sec > _media + _desv*2 )[0]
    grupos_neg = np.where( _sec < _media + -2*_desv )[0]
    consec_pos = np.array_split(grupos_pos, np.where(np.diff( grupos_pos )!=1)[0]+1)
    consec_neg = np.array_split(grupos_neg, np.where(np.diff( grupos_neg )!=1)[0]+1)
    imp_nr5(consec_pos, _sec,2,3)
    imp_nr5(consec_neg, _sec,2,3)

def imp_nr5(_consec, _sec, punto1, punto2):
	for i in range(len(_consec)):
		if ( (len(_consec[i] ) == punto1) | ( len(_consec[i]) == punto2 ) ):
			for h in range( len( _consec[i] ) ):
				print str(float(_sec[_consec[i][h]]))

def nr6(_media, _sec, _desv):
    print "Regla 6"
    grupos_pos = np.where( _sec > (_media + _desv) )[0]
    grupos_neg = np.where( _sec <  (_media - _desv) )[0]
    consec_pos = np.array_split(grupos_pos, np.where(np.diff( grupos_pos )!=1)[0]+1)
    consec_neg = np.array_split(grupos_neg, np.where(np.diff( grupos_neg )!=1)[0]+1)
    imp_nr5(consec_pos, _sec, 4,5)
    imp_nr5(consec_neg, _sec, 4,5)

def nr7(_sec, _media, _desv):
    print "Regla 7"
    quince = np.array([])
    for i in range( len(_sec) ):
		if ( (_sec[i] > _media - _desv ) & ( _sec[i] < _media + _desv) ): quince = np.append(quince, i)
	
    consec = np.array_split(quince, np.where(np.diff( quince )!=1 )[0]+1)
    imp_nr(consec, _sec, 15)
	
def nr8(_dmm, _desv, _sec):
    print "Regla 8"
    ocho = np.array([])
    for i in range( len(_dmm) ):
		if ( (_dmm[i] > _desv) | ( _dmm[i] < -_desv) ): ocho = np.append(ocho, i)
    consec = np.array_split(ocho, np.where(np.diff( ocho )!=1)[0]+1)
    for h in range( len(consec) ):
		if ( len(consec[h]) == 8 ):
			print "Regla 8 >> "
			for k in range( len( consec[h] ) ):
				 print str( _sec[ consec[h][k] ] )
	

print "Secuencia leida >> " + str(datos) + "\nMedia >> " + str(media) + "\nSecuencia menos media >> " + str(dmm) \
	+ "\nVarianza >> " + str(var) + "\nDesviacion Estandar >> " + str(desv)
