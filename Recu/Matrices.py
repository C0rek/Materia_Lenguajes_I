'''
Dada una matriz (N filas, M columnas) de palabras, obtener otra matriz Nx3 que se completa de la siguiente manera:
Para cada fila i:
columna 1: la palabra de menor longitud de la fila i
columna 2: la palabra de mayor longitud de la fila i
columna 3: la suma de las longitudes de las palabras anteriores

Resuelva con funciones y/o procedimientos.
'''

matriz=['Rio', 'Palabra', 'Arco', 'Rama']
matriz2=['','','','']

menor=10
mayor=-1
suma=0 
for i in range(len(matriz)):
    for j in matriz:
        n=len(matriz[j][i])
        if n>mayor:
            mayor=n
            matriz2[i][1]=matriz[i][j] 
        if n<menor:
            menor=n
            matriz2[i][0]=matriz[i][j]
        suma=mayor+menor
        matriz2[i][0]=suma
print(matriz2)
return matriz2
