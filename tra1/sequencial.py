

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


def multMatriz():
    A = createMatrz("tra1/entradas/A4x4.txt")
    B = createMatrz("tra1/entradas/B4x4.txt")
    printMatriz(4,A);
    


multMatriz()