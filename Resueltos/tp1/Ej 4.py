def ContarVoc(X):
    C=0
    for i in range (len(X)):
        if X[i]=="a" or X[i]=="e" or X[i]=="i" or X[i]=="o" or X[i]=="u":
            C=C+1
    print(X,"Tiene",C,"vocales")

def ContarCons(X):
    C=0
    for i in range (len(X)):
        if X[i]!="a" and X[i]!="e" and X[i]!="i" and X[i]!="o" and X[i]!="u" and X[i]!="," and X[i]!=" " and X[i]!="." and X[i]!="?":
            C=C+1
    print(X,"Tiene",C,"consonantes")

def CargOraciones(V):
    V+=[input("Ingrese una oracion:")]
    while True:
        print("Desea añadir otra oracion?")
        R=input("Si o No:")
        if R=="si" or R=="Si":
            V+=[input("Ingrese una oracion:")]
        if R=="No" or R=="no":
            return (V)


#Lo saque de Internet y edite el de consonantes
def contar_vocales(X):
    print (X,"tiene",(sum(c in {"a","A","e","E","i","I","o","O","u","U"} for c in X)),"vocales")

def contar_consonantes(X):
    print (X,"tiene",(len(X)-sum(p in {"a","A","e","E","i","I","o","O","u","U"," ",".",",","?"} for p in X)),"consonantes")


#EJ 4    
V=[]
CargOraciones(V)
for i in range (len(V)):
    contar_vocales(V[i])
    contar_consonantes(V[i])

    

