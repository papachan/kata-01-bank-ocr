#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = {1: (
	(" ", " ", " "),
	(" ", " ", "|"),
	(" ", " ", "|")),
	 2: (
	(" ", "_", " "),
	(" ", "_", "|"),
	("|", "_", " ")),
	 3: (
	(" ", "_", " "),
	(" ", "_", "|"),
	(" ", "_", "|")),
	 4: (
	(" ", " ", " "),
	("|", "_", "|"),
	(" ", " ", "|")),
	 5: (
	(" ", "_", " "),
	("|", "_", " "),
	(" ", "_", "|")),
	 6: (
	(" ", "_", " "),
	("|", "_", " "),
	("|", "_", "|")),
	 7: (
	(" ", "_", " "),
	(" ", " ", "|"),
	(" ", " ", "|")),
	 8: (
	(" ", "_", " "),
	("|", "_", "|"),
	("|", "_", "|")),
	 9: (
	(" ", "_", " "),
	("|", "_", "|"),
	(" ", "_", "|")),
	 0: (
	(" ", "_", " "),
	("|", " ", "|"),
	("|", "_", "|"))}

def print_mat(m):
	print "%s%s%s"%(m[0])
	print "%s%s%s"%(m[1])
	print "%s%s%s"%(m[2])

def print_t():
	for k, l in t.iteritems():
		print k
		print_mat(l)

def construir_matriz_num((la, lb, lc)):
	matriz_num = tuple(la[0:3]),tuple(lb[0:3]),tuple(lc[0:3])
	nuevas_listas = (la[3:], lb[3:], lc[3:])	
	return matriz_num, nuevas_listas

DIGIT_ILL = -1


def parseMatriz(m):
	for n, value in t.iteritems():
		if m == value:
			return n
	return DIGIT_ILL

ERR_OK = "OK"
ERR_ILL = "ILL"
ERR_ERR = "ERR"

def parseCuenta(lineas):
	matrices = list()
	cuenta = list()
	error = ERR_OK
	while len(lineas[0]) > 0:
		matriz_num, lineas = construir_matriz_num(lineas)
		matrices.append(matriz_num)
	for m in matrices:
		n = parseMatriz(m)
		if n in (DIGIT_ILL,):
			error = ERR_ILL
		cuenta.append(n)
	
	if error == ERR_ILL:
		return cuenta, error

	if not checksum_cuenta(cuenta):
		error = ERR_ERR

	return cuenta, error


def checksum_cuenta(digitos):
	return sum([(i+1) * n \
		        for i, n in enumerate(reversed(digitos))]) \
	          % 11 == 0


def get_lineas(filename):
	with open(filename, 'r') as resource:
		lineaA = resource.readline()[:-1]
		lineaB = resource.readline()[:-1]
		lineaC = resource.readline()[:-1]
	return (lineaA, lineaB, lineaC)

def formatear_cuenta(digitos, error):
	sd = "".join([str(d) if d != DIGIT_ILL else '?'\
				 for d in digitos])	
	if error != ERR_OK:
		return "%s %s" % (sd, error)
	return "%s" % (sd, )


if __name__ == '__main__':
	print parseCuenta(get_lineas('resources.txt'))