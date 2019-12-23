from pysat.solvers import Glucose3
from manipulacao_arquivo_cnf import ler_arquivo_cnf
import timeit

g = Glucose3()

clausulas = ler_arquivo_cnf()[0]

for clausula in clausulas:
    print(clausula)
    g.add_clause(clausula)

start = time.time()
print(g.solve())
end = time.time()
print(end - start)
time = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print("Executado em", round(time, 4), "milisegundos")
