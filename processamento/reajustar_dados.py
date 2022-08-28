# flake8: noqa
from dados.busca import buscar,pesquisa_binaria_recursiva,pesquisa_binaria_bisect
from pandas import Series
def remover_resultado_concursos(possibilidades, resultado_concursos):
	"""
	Remove da lista de possibilidades os resultados já sorteados.
	
	:param possibilidades: Combinações possíveis da Lotofácil
	:param resultado_concursos: Resultado de todos os concursos
	
	return:	A lista de possibilidades sem os resultados já sorteados.
	"""
	

	elem_ini = 0
	elem_fin = len(possibilidades) - 1
	possibilidades.sort()
	indices = obter_indices(possibilidades, resultado_concursos)

	s_possibilidades = Series(possibilidades)
	removidos = s_possibilidades.drop(indices)

	lista_possibilidades_atualizada = removidos.values 
	
	return lista_possibilidades_atualizada.tolist()
def remover_apostas_repetidos(possibilidades):
	"""
	Remove da lista as apostas repetidas.
	
	:param possibilidades: Combinações possíveis da Lotofácil
	:param resultado_concursos: Resultado de todos os concursos
	
	return:	A lista de possibilidades sem os resultados já sorteados.
	"""
	
	indices = obter_indices_repetidos(possibilidades)

	s_possibilidades = Series(possibilidades)
	removidos = s_possibilidades.drop(indices)

	lista_possibilidades_atualizada = removidos.values 
	
	return lista_possibilidades_atualizada.tolist()

def obter_indices(possibilidades, resultado_concursos):
	"""
	Obtém os índices da lista de possibilidades dos resultados já sorteados.
	
	:param possibilidades: Combinações possíveis da Lotofácil
	:param resultado_concursos: Resultado de todos os concursos
	
	return:	Uma lista com os índice dos resultados já sorteados nos concursos.
	"""
	# elem_ini = 0
	# elem_fin = len(possibilidades) - 1
	#possibilidades.sort()
	indices = list()
	for i in resultado_concursos:
		indice = pesquisa_binaria_bisect(possibilidades,i)
		# indice = pesquisa_binaria_recursiva(possibilidades,elem_ini,elem_fin,i)
		# indice = buscar(
		# 		possibilidades,
		# 		elem_ini,
		# 		elem_fin,
		# 		i)
		if indice != -1: indices.append(indice)

	return indices

def obter_indices_repetidos(possibilidades):
	"""
	Obtém os índices da lista de possibilidades dos resultados já sorteados.
	
	:param possibilidades: Combinações possíveis da Lotofácil
	return:	Uma lista com os índice dos resultados já sorteados nos concursos.
	"""
	
	indices = list()
	for i in range(len(possibilidades)):
		for j in range(i,len(possibilidades)):
			if i==j:continue
			if possibilidades[i] == possibilidades[j]: indices.append(i)

	return indices