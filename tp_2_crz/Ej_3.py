#Escribir un programa que dado un archivo de texto obtenga otro archivo equivalente que tenga, a lo
#sumo N columnas (N caracteres por línea). Donde N es un dato ingresado por el usuario. 

def n_lineas(X):
    N=int(input("Ingrese la cantidad de caracteres que desea por linea:"))
    for i in range(len(X)):
        for j in range(1):
            archivo_2.write(L[i][0:N])
            archivo_2.write("\n")



#main
archivo=open("Teoria.txt","r")
L = [ ]
L=archivo.readlines()
archivo_2=open("Copia.txt","w")
n_lineas(L)
archivo.close()
archivo_2.close()


#unico problema es que escribe un salto de linea de mas cuando se encuentra con una linea vacia