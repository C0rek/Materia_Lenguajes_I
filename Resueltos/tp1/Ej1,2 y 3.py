def Vmax(N):
    V1=int(input("Ingrese un numero:"))
    for i in range (N-1):
        V2=int(input("Ingrese un numero:"))
        if V2>V1:
            V1=V2
    print(V1)

## EJ 1
## Lista de 3 numeros
#N=int(input("Ingrese el tamaño de la lista:"))
#Vmax(N)


## EJ 2
## Lista de 10 numeros
#N=int(input("Ingrese el tamaño de la lista:"))
#Vmax(N)

#3a
def CargV(Vector,Tamaño):       #carga vector
    for i in range (Tamaño):
        Vector[i]=int(input("Ingrese un valor:"))
    return (Vector)

def SumaV(Vector,Tamaño):           #suma vector
    S=0
    for i in range (Tamaño):
        S=S+Vector[i]
    print ("La suma es:",S)

def SumaDV(Vector1,N,Vector2,M,VectorR):   #suma de vectores
    VectorR=[]*(N+M)
    VectorR=Vector1
    for i in range (M):
        VectorR[i+N]=Vector2[i]
    return (VectorR)


#3c
def CompV(Vector1,N,Vector2,M):
    B=1
    i=0
    if M!=N:
        print("No son iguales")
    else:
        while B==1 and i<M:
            if Vector1[i]==Vector2[i]:
                i=i+1
            else:
                B==0
    if B==0:
        print("No son iguales")
    else:
        VectorR=Vector1
        print(VectorR)
        for i in range (M):
            VectorR+=[Vector2[i]]
        print(VectorR)
        
    
        


#EJ 3
N=int(input("Ingrese el tamaño del primer vector:"))
A=[""]*N
CargV(A,N)
print(SumaV(A,N))
M=int(input("Ingrese el tamaño del segundo vector:"))
B=[""]*M
CargV(B,M)
print(SumaV(B,M))
CompV(A,N,B,M)

        
