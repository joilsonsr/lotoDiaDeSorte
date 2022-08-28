from ast import And
from audioop import reverse
from dados.busca import  pesquisa_binaria_bisect
from itertools import combinations
from pandas import read_csv
from processamento.resultados import resultados_ordenados
from processamento.estatisticaSorteio import ultimoCiclo
from sorteios.sortear import sortear_numeros
import random
from collections import OrderedDict
from random import choices

dadosSorteio =  read_csv('./base/resultados.csv', sep=';', encoding='utf-8')
resultSorteio = resultados_ordenados(dadosSorteio)

dz = [i for i in range(1, 32)]
# combinacoes = list()
# for combinacao in combinations(dz,7):
#     combinacoes.append(set(combinacao))
#print( maxGap(resultSorteio,dz,False ))
#lista_frequencia = maxFrequenciaOratraso(resultSorteio,dz )
#lista_frequencia = sorted(lista_frequencia.items())
#print(dict(sorted(lista_frequencia.items(), key=lambda item: item[1])))
n_pesos = dict(sorted(ultimoCiclo(resultSorteio,dz,True,1 ).items(), key=lambda item: item[1]))
print(n_pesos)
sorteados = sortear_numeros(n_pesos,10)

rem = choices(sorteados, k=1)
print(n_pesos.pop(rem[-1]),end=' ')
print(rem)
rem = choices(sorteados, k=1)
print(n_pesos.pop(rem[-1]),end=' ')
print(rem)

print(n_pesos)
print(sorteados)
# contAcerto7=0
# contAcerto6=0
# contAcerto5=0
# contAcerto4=0
# contAcertoM4 = 0
# idxi=0

# while idxi < len(resultSorteio):
#     idxj=idxi+1
#     while idxj < len(resultSorteio):
               
#         conferido = confereSorteio(resultSorteio[idxi],resultSorteio[idxj])
#         if(len(conferido)== 7):
#             contAcerto7+=1
#             print(f'{resultSorteio[idxj]} acerto 7 pontos concIdxi: {idxi+1} concIdxj: {idxj+1}')
#         # elif(len(conferido)== 6):
#         #     contAcerto6+=1
#         #     print(f'{resultSorteio[idxj]} acerto 6 pontos concIdxi: {idxi+1} concIdxj: {idxj+1}')
#         # elif(len(conferido)== 5):
#         #     contAcerto5+=1
#         #     print(f'{resultSorteio[idxj]} acerto 5 pontos concIdxi: {idxi+1} concIdxj: {idxj+1}')
#         elif(len(conferido)== 4):
#             contAcerto4+=1
#             print(f'{resultSorteio[idxj]} acerto 4 pontos  concIdxi: {idxi+1} concIdxj: {idxj+1}')
#         # elif(len(conferido)< 4):
            
#         #     contAcertoM4+=1
#         #     print(f'{i} {j} acerto < 4 pontos idxi{idxi} idxi idxj{idxj}')
#         idxj+=1
#     idxi+=1
# print(f'total: {contAcertoM4+contAcerto4+contAcerto5+contAcerto6+contAcerto7} \n')