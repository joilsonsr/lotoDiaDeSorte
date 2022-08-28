import math
n = 11 # tamanho dos numeros da combinação
k = 7 #numeros sorteados, e do jogo
t = 6 #numero menores acertos
possibilidadeComb = math.comb(n,k)
totalCobertura = math.comb(k,t)*math.comb(n-k,k-t)
print("Total Combinações possiveis: ",possibilidadeComb)
print("Potencial de cobertura na primeira combinação: ",totalCobertura)

print("Possibilidade teorica de cobertura: ",possibilidadeComb/totalCobertura)