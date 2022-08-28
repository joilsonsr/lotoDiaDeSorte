
def maxGap(dadosSorteio, numeros, maiorFrequencia=True):
    contagem = dict()#[0 for i in range(1, 32)]
    for i in range(1, 32):
        contagem[i] = 0
    for j in numeros:
        temp=0
      
        for i in dadosSorteio:
            if (j in i) == maiorFrequencia:
               temp +=1
            else:
                #print(f'{temp} : {j}')
                if contagem[j] < temp:
                    contagem[j]=temp
                temp=0
    return  contagem
def maxFrequenciaOratraso(dadosSorteio, numeros, maiorFrequencia=True):
    contagem = dict()#[0 for i in range(1, 32)]
    for i in range(1, 32):
        contagem[i] = 0
    for j in numeros:
        temp=0
      
        for i in dadosSorteio:
            if (j in i) == maiorFrequencia:
                temp +=1
        contagem[j]=temp
                
    return  contagem

def ultimoGap(dadosSorteio, numeros,ultimaFrequencia=True,ultimoSorteio=1):
    contagem = dict()
    for i in range(1, 32):
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
                break
    return  contagem
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