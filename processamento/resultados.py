from dados.busca import  pesquisa_binaria_bisect


def confereSorteio(resultSorteio, aposta):
	aposta = sorted(aposta)
	idxAcertos = [pesquisa_binaria_bisect(aposta, i  ) for i in resultSorteio]
	conferencia = list()
	for i in idxAcertos:	
		if i !=-1:
			conferencia.append(aposta[i])
	return conferencia
def resultados_ordenados(base_dados):
	"""
	Estrutura os resultados em ordem crescente.

	:param base_dados: DataFrame da base de dados.
	
	return: Retorna uma lista com todos os resultados da lotofácil
	em ordem crescente.
	"""
	dados = base_dados.copy()

	num_sorteados = dados.iloc[:, 2:9]
	num_ordenados = num_sorteados.values

	for numeros in num_ordenados:
		numeros.sort()
		
	return num_ordenados.tolist()
def resultados_ordem_sorteio(base_dados):
	"""
	Estrutura os resultados em ordem que foram sorteados.

	:param base_dados: DataFrame da base de dados.
	
	return: Retorna uma lista com todos os resultados da lotofácil
	em ordem em que foram sorteados.
	"""
	dados = base_dados.copy()

	num_sorteados = dados.iloc[:,11:18]
	num_ordenados_Sorteio = num_sorteados.values

	return num_ordenados_Sorteio.tolist()
