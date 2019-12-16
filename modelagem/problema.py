def ler_arquivo():
    arquivo = open('cursos_evento.txt', 'r')
    linhas = arquivo.readlines()

    cursos = {}
    comuns = []
    horas = 3

    encontrou_chave = False
    for linha in linhas:
        linha = linha[:-1]
        linha_quebrada = linha.split(' ')
        if linha_quebrada[0] == '#':
            encontrou_chave = True
        elif encontrou_chave:
            comuns += [[linha_quebrada[0]] + [linha_quebrada[1]]]
        else:
            cursos[linha_quebrada[0]] = linha_quebrada[1]
    arquivo.close()
    return cursos, comuns, horas


def formatar_arquivo(cursos, comuns, horas):
    restricoes = []
    # cada curso deve acontecer em pelo menos uma hora
    for curso in cursos:
        linhacurso = []
        for hora in range(horas):
            linha = []
            hora += 1
            linha.append(curso + str(hora))
            linhacurso += linha
        restricoes.append(linhacurso)
    # os cursos que possuem alunos em comum devem acontecer em horas diferentes
    for comum in comuns[::2]:
        for hora in range(horas):
            linha = []
            hora += 1
            linha.append("-" + str(comum[0]) + str(hora))
            linha.append("-" + str(comum[1]) + str(hora))
            restricoes.append(linha)
    # cada curso deve acontecer em somente uma hora
    for curso in cursos:
        for h1 in range(horas):
            h1 += 1
            for h2 in range(horas):
                linha = []
                h2 += 1
                if (h2 != h1):
                    linha.append("-" + curso + str(h1))
                    linha.append("-" + curso + str(h2))
                    restricoes.append(linha)
    return restricoes


def escrever_arquivo(restricoes, cursos, horas):
    arquivo = open('../entrada_cnf.txt', 'w')
    arquivo.write("p cnf " + str(len(cursos) * horas) + " " +
                  str(len(restricoes)))
    for restricao in restricoes:
        arquivo.write("\n" + (' ').join(restricao) + " 0")
    arquivo.close()


arquivo = ler_arquivo()
arquivo_formatado = formatar_arquivo(arquivo[0], arquivo[1], arquivo[2])
escrever_arquivo(arquivo_formatado, arquivo[0], arquivo[2])
