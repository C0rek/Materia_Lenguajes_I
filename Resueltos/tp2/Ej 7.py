    #Ej 7
def total(lista):
    T=0
    for i in range (len(lista)):
        S=lista[i].split()
        S=" ".join(S)
        R=S.find("SI")
        if R!=-1:
            T=T+1
        print(S)
    print("Votaron ",T," personas con un porcentaje de ",T/(len(lista))*100,"%")

def menor(lista):
    si=0
    ET=0
    for i in range (len(texto)):
        S=lista[i].split()
        S=" ".join(S)
        coma=0
        for j in range (3):
            coma=S.find(";")
            S=S[coma+1:len(lista[i])]
        E=float(S[0:S.find(";")])
        if E<18:
            ET=ET+1
            aux=S.find("SI")
            if aux!=-1:
                si=si+1
    if si==0:
        print("No voto ningun menor de 18 años")
    else:
        print("Voto/Votaron ",si," persona/s menores de 18 sobre un total de" ,ET ,"persona, o sea un ",si/ET*100,"%")

def mayores(lista):
    si=0
    ET=0
    for i in range (len(lista)):
        S=lista[i].split()
        S=" ".join(S)
        coma=0
        for j in range (3):
            coma=S.find(";")
            S=S[coma+1:len(lista[i])]
        E=float(S[0:S.find(";")])
        if E>70:
            ET=ET+1
            aux=S.find("SI")
            if aux!=-1:
                si=si+1
    if si==0:
        print("No voto ningun mayor de 70 años")
    else:
        print("Voto/Votaron ",si," persona/s mayores de 70 sobre un total de" ,ET ,"persona, o sea un ",si/ET*100,"%")


    

#cuerpo
archivo=open("D:\TP2\Ej 7.txt","r")
lista=archivo.readlines()
archivo.close()
total(lista)
menor(lista)
mayores(lista)
