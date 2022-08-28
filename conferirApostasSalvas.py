from tkinter import filedialog, messagebox
from pandas import read_csv
from dados.scrapping_resultados import atualizaConcursos
from processamento.resultados import confereSorteio,resultados_ordenados
from datetime import date

contAcerto7=0
contAcerto6=0
contAcerto5=0
contAcerto4=0
selecaoApostas = filedialog.askopenfilename()
if not selecaoApostas:  exit()
dadosSorteio =  read_csv('./base/resultados.csv', sep=';', encoding='utf-8')
resultSorteio = resultados_ordenados(dadosSorteio)
if not (dadosSorteio.iloc[-1,1:2].values[0]==date.today().strftime("%d/%m/%Y")):
    if  messagebox.askyesno("Atualizar concurso", "Gostaria de atualizar concurso?"):     
     atualizaConcursos()
print("data",)
apostasFeitas =  read_csv(selecaoApostas, sep=';', encoding='utf-8',header=None)

apostasFeitas = apostasFeitas.iloc[:].values.tolist()
for i in apostasFeitas:
    conferido=confereSorteio(i,resultSorteio[-1])
    if(len(conferido)== 7):
        contAcerto7+=1
        
    elif(len(conferido)== 6):
         contAcerto6+=1
      
    elif(len(conferido)== 5):
         contAcerto5+=1
         
    elif(len(conferido)== 4):
        contAcerto4+=1
print(f'Acertos 4 pontos: {contAcerto4} \nAcertos 5 pontos: {contAcerto5} \nAcertos 6 pontos: {contAcerto6} \nAcertos 7 pontos: {contAcerto7} \n')

messagebox.showinfo("Resultado conferância josogs",f'Acertos 4 pontos: {contAcerto4} \nAcertos 5 pontos: {contAcerto5} \nAcertos 6 pontos: {contAcerto6} \nAcertos 7 pontos: {contAcerto7} \n') 