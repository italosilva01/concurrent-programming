# import numpy

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


def multMatriz(m,n,p):
    # In [2]:a =  np.zeros((4,4), dtype=np.float64)
    A = createMatrz("tra1/entradas/A4x4.txt")
    B = createMatrz("tra1/entradas/B4x4.txt")
    row = [0]*4
    colum = [0]*4;
    C = [row]*4;

    printMatriz(4,a);
    print("==========")
    printMatriz(4,B);
    i = 0;
    j =0;
    k = 0;

    for i in range(m):
        for j in range(n):
            soma= 0;
            for k in range(p):
                soma +=  (int(A[i][k]) * int(B[k][j]));

            C[i][j] = soma;
            
            

    print();
    printMatriz(len(C),C);



multMatriz(4,4,4)

