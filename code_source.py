t = {"uno": (
	(" ", " ", " "),
	(" ", " ", "|"),
	(" ", " ", "|")),
	 "dos": (
	(" ", "_", " "),
	(" ", "_", "|"),
	("|", "_", " ")),
	"tres": (
	(" ", "_", " "),
	(" ", "_", "|"),
	(" ", "_", "|")),
	"cuatro": (
	(" ", " ", " "),
	("|", "_", "|"),
	(" ", " ", "|")),
	"cinco": (
	(" ", "_", " "),
	("|", "_", " "),
	(" ", "_", "|")),
	"seis": (
	(" ", "_", " "),
	("|", "_", " "),
	("|", "_", "|")),
	"siete": (
	(" ", "_", " "),
	(" ", " ", "|"),
	(" ", " ", "|")),
	"ocho": (
	(" ", "_", " "),
	("|", "_", "|"),
	("|", "_", "|")),
	"nueve": (
	(" ", "_", " "),
	("|", "_", "|"),
	(" ", "_", "|")),
	"cero": (
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


resource = open('resources.txt', 'r')


def construir_matriz_num((la, lb, lc)):
	matriz_num = tuple(la[0:3]),tuple(lb[0:3]),tuple(lc[0:3])
	nuevas_listas = (la[3:], lb[3:], lc[3:])
	print matriz_num	
	return matriz_num, nuevas_listas



lineaA = resource.readline()[:-1]
lineaB = resource.readline()[:-1]
lineaC = resource.readline()[:-1]

print len(lineaA)
print len(lineaB)
print len(lineaC)

lineas = (lineaA, lineaB, lineaC)
matrices = list()
while len(lineas[0]) > 0:
	matriz_num, lineas = construir_matriz_num(lineas)
	matrices.append(matriz_num)

for m in matrices:
	print_mat(m)

print lineaA, lineaB, lineaC

