from pandas import read_csv


ARQUIVO = './combinacoes/combinacoes.csv'


def obter_possibilidades(arq=ARQUIVO):
	"""
	Cria uma lista com todas as combinações possíveis da lotofácil
		
	:param arq: Arquivo CSV com as combinações
	
	:return: Uma lista com todas as combinações 
	"""

	df = read_csv(arq, sep=';', encoding='utf-8')
	
	df.drop(columns=['seq'], inplace=True)
	possibilidades = df.values.tolist()
	possibilidades.sort()
	return possibilidades
def ultimoCiclo(dadosSorteio, numeros,ultimaFrequencia=True,ultimoSorteio=1):
    contagem = dict()
    for i in range(1, len(numeros)+1):
        contagem[i] = 0
    for j in numeros:
        temp=0
        for i in range(len(dadosSorteio)-ultimoSorteio,0,-1):
            
            if (j in dadosSorteio[i])==ultimaFrequencia:
               #print(dadosSorteio[i])
               temp +=1
            else:
                #print(f'{temp} : {j}')
                contagem[j]=temp
                #temp=0
                if(temp!=0):    break
    return  contagem

