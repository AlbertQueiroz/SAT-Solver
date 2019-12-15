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
        for hora in range(horas+1):
            linha = []
            if (hora > 0):
                linha.append([curso, hora])
            restricoes += linha
    # os cursos que possuem alunos em comum devem acontecer em horas diferentes
    for comum in comuns[::2]:
        for hora in range(horas + 1):
            linha = []
            if (hora > 0):
                linha.append(
                    "-" + str(comum[0]) + str(hora) + " " + str(comum[1]) + str(hora))
        restricoes += linha
    print(restricoes)


arquivo = ler_arquivo()
formatar_arquivo(arquivo[0], arquivo[1], arquivo[2])
