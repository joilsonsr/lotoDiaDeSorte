def somarDezenas(dz):
    totalSoma=0
    for i in dz:
        totalSoma+=i
    return totalSoma
def isFaixa(dz):
    #   5%				19%			30%			25% 			16%  		 5%
    #de 28 à 78	de 79 à 95 	de 96 à 112 de 113 à 129	de 130 à 146   de 147 à 196
    #retorna palavra chave faixa das dezenas 
    # exemplo faixa28a78
    soma = somarDezenas(dz)
    if soma >= 28 and soma <= 78:
        return "faixa28a78"
    if soma >= 79 and soma <= 95:
        return "faixa79a95"
    if soma >= 96 and soma <= 112:
        return "faixa96a112"
    if soma >= 113 and soma <= 129:
        return "faixa113a129"
    if soma >= 130 and soma <= 146:
        return "faixa130a146"
    if soma >= 147 and soma <= 196:
        return "faixa147a196"

def removerFaixas(apostas, *args):
    listasRemover= list()
    for arg in args:
        for i in apostas:
            faixa= isFaixa(i)
            if faixa == arg:
                listasRemover.append(i)
    for i in listasRemover:
        if i in apostas:
            apostas.remove(i)
        