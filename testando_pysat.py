from pysat.solvers import Glucose3
from manipulacao_arquivo_cnf import ler_arquivo_cnf
import time

g = Glucose3()

clausulas = ler_arquivo_cnf()[0]

for clausula in clausulas:
    print(clausula)
    g.add_clause(clausula)

t0 = time.time()
print(g.solve())
t1 = time.time()

print("Executado em {} milisegundos".format(t1-t0))
