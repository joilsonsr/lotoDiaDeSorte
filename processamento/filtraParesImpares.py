def paresIpares(dz):
    totalPares=0
    totalImpares=0
    for i in dz:
        if i%2==0: totalPares+=1
        else: totalImpares+=1
    return totalPares,totalImpares

def isFaixaParImpar(dz):
# Pares: 0. • Ímpares: 7. 0,16% Pares: 1. • Ímpares: 6. 4,82% # Pares: 2. • Ímpares: 5. 109. 16,95%
# Pares: 3. • Ímpares: 4. 212. 32,97% Pares: 4. • Ímpares: 3. 188. 29,24% # Pares: 5. • Ímpares: 2. 12,13%
# Pares: 6. • Ímpares: 1. 3,58% # Pares: 7. • Ímpares: 0. 0,16%

    parA0 = 0; imparA7=7
    parB1 = 1; imparB6=6
    parC2 = 2; imparC5=5
    parD3 = 3; imparD4=4
    parE4 = 4; imparE3=3
    parF5 = 5; imparF2=2
    parG6 = 6; imparG1=1
    parH7 = 7; imparH0=0

    pares,impares = paresIpares(dz)
    #print(f"par {pares} impar {impares}")
    if pares == parA0 and impares == imparA7:
        return "faixa0e7"
    if pares == parB1 and impares ==  imparB6:
        return "faixa1e6"
    if pares == parC2 and impares ==  imparC5:
        return "faixa2e5"
    if pares == parD3 and impares == imparD4:
        return "faixa3e4"
    if pares == parE4 and impares == imparE3:
        return "faixa4e3"
    if pares == parF5 and impares == imparF2:
        return "faixa5e2"
    if pares == parG6 and impares == imparG1:
        return "faixa6e1"
    if pares == parH7 and impares == imparH0:
        return "faixa7e0"
 

def removerFaixasParImpar(apostas, *args):
    listasRemover= list()
    for arg in args:
        for i in apostas:
            faixa= isFaixaParImpar(i)
            if faixa == arg:
                listasRemover.append(i)
    for i in listasRemover:
        if i in apostas:
            apostas.remove(i)
        