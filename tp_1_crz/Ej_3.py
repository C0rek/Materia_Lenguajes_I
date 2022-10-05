#Crear un programa que: 
#a) cargue dos vectores A y B, con N y M números enteros respectivamente 
#b) calcular la suma de los números cargados en cada vector. 
#c) si N y M son iguales, realice la suma de los vectores. Mostrar el vector resultante 
#¿Cuántas funciones y/o procedimientos son necesarios para resolver este problema? 


#parte A
#defino carga de dos vectores (A y B)
def carga_vector(vector,tamaño):
    for i in range(tamaño):
        vector[i]=int(input("Ingrese un valor:"))
    return (vector)

#parte B
#defino suma de los elementos en un vector
def suma_vector():
    SumaV=sum(A)
    sumaV_1=sum(B)
    print("La suma es del primer vector es :" ,SumaV)  
    print("La suma es del segundo vector es:",sumaV_1)       

#parte C
#defino comprobar vector con lo que pide la consigna
def comp_vector(Vector1,N,Vector2,M):
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



#main
N=int(input("Ingrese el tamaño del primer vector:"))
A=[""]*N
carga_vector(A,N)

M=int(input("Ingrese el tamaño del segundo vector:"))        #pregunto por el tamaño
B=[""]*M                                                    #Multiplico el vector por el tamaño
carga_vector(B,M)                                           #llamo a la definicion con parametros A y N
suma_vector()
comp_vector(A,N,B,M)
