def fechamento_Dez(dzFecha, Dz):
    jogos = list()
    fechamento = dzFecha.iloc[:].values.tolist()
    fechamento = [sorted(numeros) for numeros in fechamento]
    for i in fechamento:
        jogo = list()
        for j in i:
            jogo.append(Dz[j-1])
        jogos.append(jogo)
    return jogos