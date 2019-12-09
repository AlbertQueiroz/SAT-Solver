
def ler_arquivo():
    arquivo = open('arquivo_leitura.txt', 'r')
    linhas = arquivo.readlines()
    formulas = []
    for linha in linhas:
        if(linha[0] == 'c'):
            print("Comentario: ", linha[2:])
        elif(ord(linha[0]) > 57):
            dados_arquivo = linha.split()
        else:
            linha = ('').join(linha)
            linha = linha.split()
            for x in range(len(linha)):
                linha[x] = int(linha[x])
            formulas.append(linha[:-1])
    arquivo.close()
    return formulas, dados_arquivo

def mostrar_informacoes(formulas, dados_arquivo):
    linhas = []
    for clausula in formulas:
        linha = []
        for atomica in clausula:
            if(int(atomica) > 0):
                linha += [dados_arquivo[0] + atomica]
            else:
                linha += ['¬'+dados_arquivo[0] + atomica[1]]
        linhas.append(linha)
    return linhas