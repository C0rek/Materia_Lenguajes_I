#crear matriz
def cargar_matriz(matriz,fila,columna):
    for i in range (fila):
        for j in range (columna):
            matriz[i][j]=str(input("Ingrese numero para la posicion "+str(i)+" "+str(j)+": "))
            matriz[i][j]=int(matriz[i][j])


#suma de matriz
def suma_matriz(matriz1,fila1,columna1,matriz2,fila2,columna2,matrizR):
    if fila1==fila2 and columna1==columna2:
        matrizR=[["" for i in range (columna1)]for i in range (fila1)]
        for i in range (fila1):
            for j in range (columna1):
                matrizR[i][j]=matriz1[i][j]+matriz2[i][j]
        mostrar(matrizR,fila1)
        return matrizR
    else:
        print ("No se pueden sumar")


#mult de matriz
def prod_matriz(matriz1,fila1,columna1,matriz2,fila2,columna2,matrizR):
    if columna1==fila2:
        matrizR=[["" for i in range (columna2)]for i in range (fila1)]
        for i in range (fila1):
            for j in range (columna2):
                M1=0
                for k in range (fila2):
                    M1=M1+(matriz1[i][k]*matriz2[k][j])
                matrizR[i][j]=M1
        mostrar(matrizR,fila1)
        return matrizR
    else:
        print("No se puede realizar el producto de matrices")

                

#mostrar matriz
def mostrar (matriz,fila):
    for i in range(fila):
        print(matriz[i])


#menu
def menu():
    print("Que quiere hacer?")
    print("(1) Si quiere realizar una suma de matrices")
    print("(2) Si quiere realizar un producto de matrices")
    print("(3) Si quiere ver las matrices")
    print("(X) Salir")


#cuerpo
N=int(input("Cantidad de filas de la primera matriz:"))
M=int(input("Cantidad de columnas de la primera matriz:"))
A=[[0 for i in range (M)]for i in range (N)]
cargar_matriz(A,N,M)
X=int(input("Cantidad de filas de la segunda matriz:"))
Y=int(input("Cantidad de columnas de la segunda matriz:"))
B=[[0 for i in range (Y)]for i in range (X)]
cargar_matriz(B,X,Y)
S=[["" for i in range (Y)]for i in range (X)]
P=[["" for i in range (Y)]for i in range (N)]
while True:
    menu()
    R=input("Respuesta:")
    if R=="1":
        S=suma_matriz(A,N,M,B,X,Y,S)
    if R=="2":
        P=prod_matriz(A,N,M,B,X,Y,P)
    if R=="3":
        print ("Que matriz quiere ver?")
        R2=input("(A)/(B)/Suma (S)/Producto (P):")
        if R2=="A":
            print ("Matriz A")
            mostrar (A,N)
        if R2=="B":
            print ("Matriz B")
            mostrar (B,X)
        if R2=="S":
            if S==None:
                print("No tiene Matriz Suma")
            else:
                print ("Matriz Suma")
                mostrar (S,X)
        if R2=="P":
            if P==None:
                print("No tiene Mtriz Producto")
            else:
                print ("Matriz Producto")
                mostrar (P,N)
    if R=="x" or R=="X":
        break

            
