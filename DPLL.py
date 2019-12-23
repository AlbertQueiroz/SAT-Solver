from manipulacao_arquivo_cnf import ler_arquivo_cnf
from manipulacao_arquivo_cnf import escrever_resultado_cnf
from manipulacao_arquivo_cnf import mostrar_informacoes

import timeit

clausulas, dados_arquivo = ler_arquivo_cnf()


def tem_unitaria(clausulas):
    ret = False
    for clausula in clausulas:
        if(type(clausula) == int):
            return False
        if (len(clausula) == 1):
            ret = True
    return ret


def pega_literal_unitaria(clausulas):
    for clausula in clausulas:
        if (len(clausula) == 1):
            return clausula[0]


def pega_literal(clausulas):
    return clausulas[-1][-1]


def atualizar(clausulas, literal_unitaria):
    for clausula in clausulas[::-1]:
        if (literal_unitaria in clausula):
            clausulas.remove(clausula)
        if (literal_unitaria*-1 in clausula):
            clausula.remove(literal_unitaria*-1)
    return clausulas


def simplifica(clausulas):
    valoração = {}
    while (tem_unitaria(clausulas)):
        literal_unitaria = pega_literal_unitaria(clausulas)
        if (literal_unitaria < 0):
            valoração[(literal_unitaria*-1)] = False
        else:
            valoração[literal_unitaria] = True
        clausulas = atualizar(clausulas, literal_unitaria)
    return clausulas, valoração


def dpll(clausulas):
    return dpll_rec(clausulas, {})


def dpll_rec(clausulas, valoração):
    clausulas, valoração2 = simplifica(clausulas)
    valoração.update(valoração2)
    if ([] in clausulas):
        return False
    if (clausulas == []):
        return valoração
    literal = pega_literal(clausulas)
    clausulas1 = clausulas + [[literal]]
    clausulas2 = clausulas + [literal*-1]
    res = dpll_rec(clausulas1, valoração.copy())
    if (res != False):
        return res
    return dpll_rec(clausulas2, valoração.copy())


#mostrar_informacoes(clausulas, dados_arquivo)
escrever_resultado_cnf(dpll(clausulas))
time = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print("Executado em", round(time, 4), "milisegundos")
