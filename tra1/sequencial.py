import numpy  as np
import sys

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


def multMatriz(size):
    
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




def main ():
    size,forma = sys.stdin.readline().split()
    print(size) 
    size = int(size)
    print(forma)
    multMatriz(size)
    

main()