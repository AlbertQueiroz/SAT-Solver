
def ler_arquivo():
    arquivo = open('arquivo_leitura.txt', 'r')
    linhas = arquivo.readlines()
    formulas = []
    for linha in linhas:
        if(linha[0] == 'c'):
            print("\n Comentario: ", linha[2:])
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

def escrever_arquivo(valoracao):
    arquivo = open('arquivo_escrita.txt', 'w')
    if (valoracao == False):
        arquivo.write("UNSATISFIABLE")
    else:
        for literal in valoracao:
            if (valoracao[literal] == False):
                arquivo.write(str(literal*-1) + " ")
            elif (valoracao[literal] == True):
                arquivo.write(str(literal) + " ")
        arquivo.write("0")
    arquivo.close()
