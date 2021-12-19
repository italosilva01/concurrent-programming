import numpy  as np
import sys
from threading import Thread
import timeit
import pandas as pd

def createMatrz(file):
    row = 0
    matriz=[]
    file = open(file,"r")  
    size = file.readlines()

    for i in range(len(size)):
        if(i ==0):
            row = size[i][0]
        else:     
            matriz.append(size[i].split())
    return matriz

def printMatriz(size,matriz):
     for a in range(size):          #mostra quedrando em linhas
        print(matriz[a])  

def writeResult (size,ResultMatriz):
    nameFileResult = "C"+str(size)+"x"+str(size)+".txt"
    
    with open(nameFileResult,'wb') as f:      
        np.savetxt(f,ResultMatriz, fmt="%d")

def multMatrizSequencial(size):
    A = createMatrz("tra1/entradas/A"+str(size)+"x"+str(size)+".txt")
    B = createMatrz("tra1/entradas/B"+str(size)+"x"+str(size)+".txt")
   
    C = np.zeros((size,size), dtype=np.float64)

   
    i = 0
    j =0
    k = 0

    for i in range(size):
        for j in range(size):
            soma= 0
            for k in range(size):
                soma +=  (int(A[i][k]) * int(B[k][j]));

            C[i][j] = soma
            
    writeResult(size,C)



def multMatrizConcorrente(size):

    A = createMatrz("tra1/entradas/A"+str(size)+"x"+str(size)+".txt")
    B = createMatrz("tra1/entradas/B"+str(size)+"x"+str(size)+".txt")   
    C = np.zeros((size,size), dtype=np.float64)
    threads = []
    id = 0
    #faço um for de 0 até o tamanho do size
        #Cada execução irá lancar uma thred;
        #cada thred irá ser responsável por uma linha da matriz resposta (C)
        #a thred irá calcular a linha da matriz A
        # Logo antes da thread começar a ler a matriz, dar um stop (condição de corrida)
        # Thred ler linha da matriz A
        # thred ler as colunas da Matriz B e faz os calculos
        #assim que a última coluna B for calcaulada com o ultimo elemento da linha do Matriz A, a thred irá salvar a linha na MAtriz C
      
    def doTask(row):
        #funcionando
        j = 0;
        k= 0;
       
        
        for j in range(size):
            soma = 0;
            for k in range(size):
                soma += int(A[row][k])*int(B[k][j])
            C[row][j] = soma
        
         
    for id in range(size):
        t = Thread(target=doTask,args=(id,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
         
    writeResult(size,C)         
    


def main ():
    size,forma = sys.stdin.readline().split()
    size = int(size)
    print('--------------------\n')
    
    if forma =='S':
       
        t = timeit.Timer(lambda:multMatrizSequencial(size))
        listTime = t.repeat(20,1)
        print( str(max(listTime)))
        print( str(min(listTime)))
        print( str(sum(listTime)/len(listTime)))
        
        df = pd.DataFrame(listTime)       
        df.to_csv(str(size)+"x"+str(size)+"S.csv",index=False)

        
    elif forma == 'C':
       
        t = timeit.Timer(lambda:multMatrizConcorrente(size))
        listTime = t.repeat(20,1)
        print( str(max(listTime)))
        print( str(min(listTime)))
        print( str(sum(listTime)/len(listTime)))

        df = pd.DataFrame(listTime)
       
        df.to_csv(str(size)+"x"+str(size)+"C.csv",index=False)

main()