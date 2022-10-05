# Dado un archivo de texto mostrar la cantidad de vocales y consonantes que contiene. Usar las
# funciones utilizadas en el TP 1. 

def contar_vocales(X):
    C=0
    for i  in range(len(X)):
        if (X[i]=="a" or X[i]=="e" or X[i]=="i" or X[i]=="o" or X[i]=="u"
        or X[i]=="A" or X[i]=="E" or X[i]=="I" or X[i]=="O" or X[i]=="U"):
            C=C+1
    print("Tiene",C,"vocales")

def contar_consonantes(X):
    C=0         #inicio contador en 0 (C)
    for i in range (len(X)):
        if (X[i]!="a" and X[i]!="e" and X[i]!="i" and X[i]!="o" and X[i]!="u"
        and X[i]!="A" and X[i]!="E" and X[i]!="I" and X[i]!="O" and X[i]!="U"
        and X[i]!="." and X[i]!="," and X[i]!=":" and X[i]!="?" and X[i]!=" "):        #Si no es igual
           
            C=C+1                   #Sumo 1 a mi contador
    print("Tiene",C,"consonantes") 

#main
archivo=open("Teoria.txt","r")
texto=archivo.read()
archivo.close()
contar_vocales(texto)
contar_consonantes(texto)