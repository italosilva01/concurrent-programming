
print('Olá mundo')

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
    print(len(size))
    return matriz

def printMatriz(size):
     for a in range(len(size)-1):          #mostra quedrando em linhas
        print(matriz[a])  


def multMatriz():
    A = createMatrz("entradas/A4x4.txt")
    B= createMatrz("entradas/B4x4.txt")

    print(A)
    print("")
    print(B)


multMatriz()