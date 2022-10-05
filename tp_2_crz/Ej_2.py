#Dado un archivo de texto, mostrar en pantalla la línea más larga del archivo (la línea que contiene más
#caracteres) y la ubicación dentro del archivo (el número de la línea). 

def linea_mas_caracteres(X):
    M=-1                               #M=mayor -1 para que la linea de 0 cuente
    for i in range(len(X)):             #(todo el archivo) tiene 61 lineas 
        if (len(L[i]))>M:              #si el rango es mayor LM
            M=len(L[i])                #cambia LM por
            linea=i
    print("La linea mas larga es:\n",L[linea],"\nubicacion",linea+1)
        

#main
archivo=open("Teoria.txt","r")
L=[ ]
L=archivo.readlines()
archivo.close()
linea_mas_caracteres(L)
