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

def parseMatriz(m):
	for n, value in t.iteritems():
		if m == value:
			return n

def parseCuenta(lineas):
	matrices = list()
	cuenta = list()
	while len(lineas[0]) > 0:
		matriz_num, lineas = construir_matriz_num(lineas)
		matrices.append(matriz_num)
	for m in matrices:
		cuenta.append(parseMatriz(m))
	return cuenta	    

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


if __name__ == '__main__':
	print parseCuenta(get_lineas('resources.txt'))