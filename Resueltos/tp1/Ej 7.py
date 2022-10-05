#suma diagonal principal
def diagonal_p(matriz,M):
    suma=0
    for i in range (M):
        suma=suma+matriz[i][i]
    print ("La suma de la diagonal principal es:",suma)
    return suma


#factorial
def factorial(num):
    fact=1
    for i in range(num):
        fact=fact*(i+1)
    return fact

#borrar repetidos
def b_repetidos(lista):
    print("Set:",set(lista))
    lista=int(lista)
    print("La lista sin repetidos es:",lista)
    return lista

#borrar repetidos 2
def b2_repetidos(lista):
    j=0
    Y=len(lista)
    while j<Y:
        A=lista[j]
        i=j+1
        while i<Y and i!=j:
            if A==lista[i]:
                del(lista[i])
                Y=Y-1
            i=i+1
        j=j+1
    print("La lista sin repetidos es:",lista)
    return lista
    
    


#ordenar lista
def ordenar_lista(lista):
    lista.sort()
    print("La lista ordenada es:",lista)



#cargar matriz
def cargar_m(matriz,M):
    for i in range (M):
        for j in range (M):
            aux=str(input("Ingrese un numero entero en la posicon "+str(i)+" "+str(j)+" :"))
            matriz[i][j]=int(aux)
    for i in range(M):
        print(matriz[i])


#cuerpo

M=int(input("Ingrese el tamaño de la matriz MxM :"))
A=[[0 for i in range (M)]for i in range(M)]
cargar_m(A,M)
S=diagonal_p(A,M)
L=[]
for i in range(M):
    for j in range (M):
        F=factorial(A[i][j])
        if F>=S:
            L+=[A[i][j]]
print("La lista es:",L)
L=b2_repetidos(L)
ordenar_lista(L)
