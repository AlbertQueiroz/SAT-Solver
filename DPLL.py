clausulas = [[1],[-1,2,3]]

def tem_unitaria(clausulas):
    ret = False
    for clausula in clausulas:
        if (len(clausula) == 1):
            ret = True
    return ret

def pega_literal_unitaria(clausulas):
    for clausula in clausulas:
        if (len(clausula) == 1):
            return clausula
            break

def atualizar(clausulas, literal_unitaria):
    for clausula in clausulas:
        if (literal_unitaria in clausula):
            clausula.remove(literal_unitaria)
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

print(atualizar(clausulas, 1))