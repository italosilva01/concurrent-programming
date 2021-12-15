import numpy  as np
import sys
from threading import Thread

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


def multMatrizSequencial(size):
    
    A = createMatrz("tra1/entradas/A"+str(size)+"x"+str(size)+".txt")
    B = createMatrz("tra1/entradas/B"+str(size)+"x"+str(size)+".txt")
   
    C = np.zeros((size,size), dtype=np.float64)

   
    i = 0;
    j =0;
    k = 0;

    for i in range(size):
        for j in range(size):
            soma= 0;
            for k in range(size):
                soma +=  (int(A[i][k]) * int(B[k][j]));

            C[i][j] = soma;
            
    printMatriz(len(C),C);



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
        rowA = A[row];
        j = 0;
        k= 0;
       
        
        for j in range(size):
            soma = 0;
            for k in range(size):
                soma += int(rowA[k])*int(B[k][j]);
            C[row][j] = soma
        
         
    for id in range(size):
        t = Thread(target=doTask,args=(id,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
         
    printMatriz(size,C)           
    


def main ():
    size,forma = sys.stdin.readline().split()
    size = int(size)
    print(forma)
    multMatrizConcorrente(size)
    print('==================')
    multMatrizSequencial(size)
    

main()