from datetime import datetime
from secrets import choice
from tkinter import messagebox

from sorteios.sortear import sortear_numeros
from processamento.fechamento import fechamento_Dez
from processamento.estatisticaSorteio import  ultimoCiclo
from pandas import read_csv, DataFrame
n_dzFech=13 #numeros de dezenas para o fechamento
n_dzSorteio=7 #dezenas do sorteio dia de sorte
n_garantia=5 # numero de garantia para fechamento
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
        numerosSelecionados = sortear_numeros(n_peso,n_dz=n_dzFech)
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
           
    #print(n_peso)


base = DataFrame(apostas)
if messagebox.askyesno("Salvar Apostas", "Gostaria de Salvar as apostas?"):
    base.to_csv(f'./base/jogo_{n_dzFech}_dez-{datetime.today().strftime("%d-%m-%Y_ %Hh%Mmin")}.txt', sep=';',encoding='utf-8-sig', index=False,header=None)
    if messagebox.askyesno("Apostar online", "Gostaria de registar apostas online?"):
        apostarOnline(apostas)

