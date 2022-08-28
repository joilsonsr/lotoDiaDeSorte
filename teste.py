from dados.busca import  pesquisa_binaria_bisect
from itertools import combinations
from pandas import read_csv
from processamento.resultados import resultados_ordenados, confereSorteio
from sorteios.sortear import sortear_numeros
import random

dadosSorteio =  read_csv('./base/resultados.csv', sep=';', encoding='utf-8')
resultSorteio = resultados_ordenados(dadosSorteio)
dadosFechamento = read_csv('./wheel-15-7-6.csv', sep=';', encoding='utf-8')
fechamento = dadosFechamento.iloc[:].values.tolist()
fechamento = [sorted(numeros) for numeros in fechamento]
print(fechamento)
dz = [i for i in range(1, 12)]
combinacoes = list()

for combinacao in combinations(dz,7):
    combinacoes.append(list(combinacao))

contAcerto7=0
contAcerto6=0
contAcerto5=0
contAcerto4=0
contAcertoM4 = 0
idxi=0
for i in fechamento:
    idxj=0
    for j in combinacoes:
        idxj+=1
        conferido = confereSorteio(j,i)
        if(len(conferido)== 7):
            contAcerto7+=1
            print(f'{j} acerto 7 pontos')
        elif(len(conferido)== 6):
            contAcerto6+=1
            print(f'{j} acerto 6 pontos')
        elif(len(conferido)== 5):
            contAcerto5+=1
            print(f'{j} acerto 5 pontos')
        elif(len(conferido)== 4):
            contAcerto4+=1
            print(f'{j} acerto 4 pontos')
        elif(len(conferido)< 4):
            
            contAcertoM4+=1
            print(f'{i} {j} acerto < 4 pontos idxi{idxi} idxi idxj{idxj}')
    idxi+=1
    
       

print(f"total de < 4 acertos {contAcertoM4} total de 4 acertos {contAcerto4} total de 5 acertos: {contAcerto5} total de 6 acertos: {contAcerto6}, total 7 {contAcerto7} total: {contAcertoM4+contAcerto4+contAcerto5+contAcerto6+contAcerto7}")
print(f'qtd sorteios {len(resultSorteio)} qtd fechamento {len(fechamento)} combinacoes {len(combinacoes)}')
sorteados = sortear_numeros()
jogo = sorted(sorteados)
print(jogo)

