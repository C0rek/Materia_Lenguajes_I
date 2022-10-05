#Crear un programa que cargue una o más oraciones y luego indique la suma total de vocales y 
#consonantes: 
#- Crear dos funciones, una para contar las vocales y otra para contar las consonantes que tiene 
#cada palabra. 
#- Cada función tomará como parámetro una palabra. 
#- En el programa principal mostrar la cantidad total de vocales y la cantidad total de consonantes 
#en el texto de entrada. 


#defino contar vocales
def contar_vocales(X):
    C=0
    for i  in range(len(X)):
        if (X[i]=="a" or X[i]=="e" or X[i]=="i" or X[i]=="o" or X[i]=="u"
        or X[i]=="A" or X[i]=="E" or X[i]=="I" or X[i]=="O" or X[i]=="U"):
            C=C+1
    print(X,": Tiene",C,"vocales")



#defino contar consonantes
def contar_consonantes(X):
    C=0         #inicio contador en 0 (C)
    for i in range (len(X)):
        if (X[i]!="a" and X[i]!="e" and X[i]!="i" and X[i]!="o" and X[i]!="u" 
        and X[i]!="." and X[i]!="," and X[i]!=":" and X[i]!="?"):        #Si no es igual
           
            C=C+1                   #Sumo 1 a mi contador

    print(X,": Tiene",C,"consonantes") 



#defino la carga de oraciones
def cargar_oraciones(V):
    V += [input("Ingrese una oracion: ")]         #cargo al vector una oracion
    while True:                                 #si carga algo
        print("Ingrese otra oracion: ")           
        R=input("Si o No: ")                    #Pregunto por otra oracion
        if R=="si" or R=="Si":                  
            V += [input("Ingrese otra oracion: ")]        #cargo otra oracion
        if R=="no" or R=="No":
            return(V)                                      #me quedo con la oracion principal



#Ej 4
V=[]
cargar_oraciones(V)
for i in range (len(V)):
    contar_vocales(V[i])
    contar_consonantes(V[i])  


