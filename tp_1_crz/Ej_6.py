#Ejercicio 6.
#Escriba un programa que para dos matrices A y B de números enteros de dimensiones MxN, realice la 
#suma o el producto de las matrices (a elección del usuario) y las cargue en otra matriz C. 
#Utilizar funciones y/o procedimientos para: 
#- cargar las matrices 
#- realizar la suma 
#- realizar el producto 
#- mostrar en pantalla una matriz 
#Invóquelas adecuadamente. 


#defino cargar matriz
def cargar_matriz(matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j]=str(input("Ingrese un numero para" +str(i) " "+str(j) ": "))   #casteo string
            matriz[i][j]=int(matriz[i][j])          #convierto todo en int



def menu()
        print("(1) - Suma de las matrices")
        print("(2) - Producto de las matrices")
        print("(3) - Mostrar la matriz")
        print("(R) - Cargar matrices nuevamente")
        print("(X) - Salir")


#main

X=int(input("Ingrese cantidad de filas para la matriz 1:"))
Y=int(input("Ingrese cantidad de columnas para la matriz 1:"))
A=[]
cargar_matriz(A,X,Y)

M=int(input("Ingrese cantidad de filas para la matriz 2:"))
N=int(input("Ingres cantidad de columnas para la matriz 2:"))
B=[]
cargar_matriz(B,M,N)

while True:
    menu()
        resp=(int)input("Ingrese una opcion: ")

        if(resp==1 or resp==2 or resp==3 or resp=="R" or resp=="X" or resp=="x" or resp=="r"):
            if (resp==1):
                suma_matrices()
                break
            if (resp==2):
                produc_matrices()
                break
            if (resp==3)
                mostrar_matriz()
                break
            if (resp=="r" or resp=="R")
                break
            if (resp=="x" or resp=="X")
                break
        else:
            print(resp,"Es una dato incorrecto\n" "Ingrese un valor correcto")    
