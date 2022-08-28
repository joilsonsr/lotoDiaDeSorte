from datetime import datetime
from secrets import choice
from tkinter import messagebox
from processamento.filtraSomaDezenas import  removerFaixas
from processamento.filtraParesImpares import removerFaixasParImpar
import time
from dados.scrapping_resultados import atualizaConcursos
from selenium import webdriver
from selenium.webdriver.common.by import By
from sorteios.sortear import sortear_numeros
from processamento.fechamento import fechamento_Dez
from processamento.estatisticaSorteio import  maxGap, ultimoCiclo,ultimoGap, maxFrequenciaOratraso
from pandas import read_csv
from processamento.resultados import confereSorteio
#atualizaConcursos()
n_dzFech=15 #numeros de dezenas para o fechamento
n_dzSorteio=7 #dezenas do sorteio dia de sorte
n_garantia=6 # numero de garantia para fechamento
#seleção do fechamento a ser feito de acordo com os dados do fechamento para selecionar o arquivo

dadosFechamento = read_csv(
    f'./base/wheel-{str(n_dzFech)}-{str(n_dzSorteio)}-{str(n_garantia)}.txt', sep=';', encoding='utf-8',header=None)

dados = read_csv('./base/resultados.csv', sep=';', encoding='utf-8')
dz = [i for i in range(1, 32)]
#lista os sorteios
resultSorteio = dados.iloc[:, 2:9].values
#seleciona as dezenas com seus pesos, quanto mais ela é sorteada maior e seu peso
n_peso = ultimoCiclo(resultSorteio, dz, True,2)
#sortea baseado no pesso maior
print()
#gera o fechamento de acordo com o fechamento selecionado das quantidade de dezenas
#a quantidade de jogos gerados e de acordo com o fechamento selecionado no arquivo txt selecionado
#quantidade de jogo para cada rodada de fechamento ou senha das dezenas maiores para o fechamento.
qtdRodadaFechamento=1
apostas=list()
#quantidades de numeros para retirar dos numeros ja soterado da aposta anterior
qtdDezRetirarSelecionado=5
for j in range(0,qtdRodadaFechamento):
    if len(n_peso)> n_dzFech:  
        numerosSelecionados = sortear_numeros(n_dz=n_dzFech)
        apostasTemp = fechamento_Dez(dadosFechamento,numerosSelecionados)
        #selecionar mais outro conjunto de numeros, retirando uma quantidade definidas de dezenas
        numerosRetirar = dict({i:1 for i in numerosSelecionados })
        numerosRetirar = sortear_numeros(numerosRetirar,n_dz=qtdDezRetirarSelecionado) 
              
        for i in numerosRetirar:
            n_peso.pop(i)
           
        for k in apostasTemp:
            apostas.append(k)
        
    else:
        print('quantidades de numeros para retirar da rodada e maior que os numeros do fechamento') 
        break


print(f'total apostas antes do filtro:{ len(apostas)}')
#   5%				19%		   30%			25% 			16%  		 5%
#"faixa28a78" "faixa79a95" "faixa96a112" "faixa113a129"	"faixa130a146"  "faixa147a196"
removerFaixas(apostas, "faixa28a78","faixa130a146","faixa147a196")
#exemplo faixa pares e impares "faixa1e6" "faixa7e0"
# Pares: 0 Ímpares: 7. 0,16% Pares: 1 Ímpares: 6 4,82% # Pares: 2 Ímpares: 5. 109. 16,95%
# Pares: 3. Ímpares: 4. 212. 32,97% Pares: 4. Ímpares: 3. 188. 29,24% # Pares: 5. • Ímpares: 2. 12,13%
# Pares: 6. • Ímpares: 1. 3,58% # Pares: 7. • Ímpares: 0. 0,16%
removerFaixasParImpar(apostas,"faixa0e7","faixa1e6","faixa5e2","faixa6e1","faixa7e0")
contAcerto7=0
contAcerto6=0
contAcerto5=0
contAcerto4=0
print(resultSorteio[-1])
#for j in resultSorteio:
for i in apostas:
    conferido=confereSorteio(i,resultSorteio[-1])
    if(len(conferido)== 7):
        contAcerto7+=1
        
    elif(len(conferido)== 6):
        contAcerto6+=1
    
    elif(len(conferido)== 5):
        contAcerto5+=1
        
    elif(len(conferido)== 4):
        contAcerto4+=1
print(f'Acertos 4 pontos: {contAcerto4} \nAcertos 5 pontos: {contAcerto5} \nAcertos 6 pontos: {contAcerto6} \nAcertos 7 pontos: {contAcerto7} \ntotal de apostas: {len(apostas)}')

# messagebox.showinfo("Resultado conferância josogs",f'Acertos 4 pontos: {contAcerto4} \nAcertos 5 pontos: {contAcerto5} \nAcertos 6 pontos: {contAcerto6} \nAcertos 7 pontos: {contAcerto7} \n') 
 

