# flake8: noqa
import bisect
def buscar(lista, elem_ini, elem_fin, valor_busca):
	
	"""
	Busca binária em uma lista.
	
	
	:param lista: lista que contém os elementos 
	:param elem_ini: Elemento inicial da lista ou sub-lista
	:param elem_fin: Elemento final da lista ou sub-lista
	:param valor_busca: Valor a ser encontrado
	
	return: O elemento buscado, caso ele esteja na lista.
	"""
	if elem_ini <= elem_fin:
		
		# Elemento do meio da lista
		meio = (elem_ini + elem_fin) // 2

		if valor_busca > lista[meio]:
			return buscar(lista, meio + 1, elem_fin, valor_busca)
		elif valor_busca < lista[meio]:
			return buscar(lista, elem_ini, meio -1, valor_busca)
		else:
			# Encontrou o elemento da busca
			#print(str(meio)+" teste")
			return meio
def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if A[meio] == item:
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif A[meio] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)

def pesquisa_binaria_bisect(A, item):
    """Implementa pesquisa binária usando bisect."""
    # Encontra o ponto onde o item deveria ser (ou está) inserido.
    i = bisect.bisect_left(A, item)
    # Testa se o item está na lista.
    return i if i < len(A) and A[i] == item else -1