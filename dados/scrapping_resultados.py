from pandas import read_html,read_csv,DataFrame
from numpy.lib.function_base import append
from numpy import uint32, random
#from requests import get
import json
from pandas import read_html, read_csv 
from os.path import exists
import time
import urllib3

#URL = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/' 
base_url = './base/resultados.csv'
urlTodosConcurso = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofacil'
urlConcAtual = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/diadesorte/'

# Cria uma lista a partir da variável (html)


def buscaConcursoInternet(concAtual='', url=urlConcAtual):
    # Busca sorteio na internet.
    # :param string: quando vazia busca o concurso atual se digitar o número do concurso
    # buscara o numero possivel do concurso
    url += str(concAtual)
    pagina = urllib3.PoolManager().request('GET', url)  #get(url,verify=False)
    #print("status da solicitação",pagina.status)
    if pagina.status !=200:
        print("não achou resultado")
        return list([])
    pagina = json.loads(pagina.data.decode('utf-8'))
 
    concurso = pagina
    listaSorteio = list()
    listaSorteio.append(concurso['numero'])
    listaSorteio.append(concurso['dataApuracao'])
    listaSorteio.extend(list(map(int, concurso['listaDezenas'])))
    listaPremio = concurso['listaRateioPremio']
    listaSorteio.append(listaPremio[0]['numeroDeGanhadores'])
    listaSorteio.extend(
        list(map(int, concurso['dezenasSorteadasOrdemSorteio'])))

    return listaSorteio


def atualizaConcursos():
   
    if not exists(base_url):
        criaCabecalho()
    
    dados = read_csv(base_url, sep=';', encoding='utf-8')
        
   
    #resultados = dados.iloc[:, 2:17].values
   
    concAtual = buscaConcursoInternet()
    if concAtual == []: return False
    concDaLista =0 ;
    if len(dados) != 0: concDaLista = uint32(dados.iloc[len(dados)-1, 0:1].values).item()
    numConcAtual = concAtual[0:1][0]
    # print(concDaLista)

    time.sleep(0.5)
    if numConcAtual != concDaLista:
        for i in range(concDaLista+1, numConcAtual):
            concursoSalvo = buscaConcursoInternet(i)
            if not concursoSalvo:
                return False
            dados.loc[len(dados)] = concursoSalvo
            time.sleep(0.7)
        dados.loc[len(dados)] = buscaConcursoInternet()
        dados.to_csv(base_url, sep=';', encoding='utf-8-sig', index=False)
    if __name__ == '__main__':
        # Informações
        concurso = dados['Concurso'].max()
        data = dados['Data_Sorteio'][concurso-1]

        print(
            f'\n\033[1;32mTODOS OS RESULTADOS DOS CONCURSOS DO DIA DE SORTE FORAM BAIXADOS COM SUCESSO!\033[m')
        print(
            f'\n\n\033[1;36mÚltimo sorteio:\033[m {data}\n\033[1;36mConcurso:\033[m {concurso}')

        print(
            f'\n\n\033[1;35mArquivo salvo em:\033[m \033[1;33m./base/resultados.csv\033[m')
    return True

def criaCabecalho():
    colunas = ['Concurso','Data_Sorteio','B1','B2','B3','B4','B5','B6','B7','Ganhadores_7_Números','OS1','OS2','OS3','OS4','OS5','OS6','OS7']
    base = DataFrame(columns = colunas)
    base.to_csv('./base/resultados.csv', sep=';',
                encoding='utf-8-sig', index=False)
    

if __name__ == "__main__":
    atualizaConcursos()
