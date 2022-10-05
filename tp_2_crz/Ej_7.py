# En las últimas elecciones cada presidente de mesa envió al Tribunal Electoral un archivo (elecciones.txt)
# con un informe de asistencia de los ciudadanos empadronados en la mesa que presidió. El archivo
# almacena los siguientes datos separados por punto y coma: nombre y apellido, número de documento,
# sexo, edad, voto (si o no)
# Escribir un programa que realice lo siguiente:
# a) Mostrar cuantas personas votaron y el porcentaje de asistencia
# b) Mostrar cuántos jóvenes menores de 18 años votaron y porcentaje sobre el total de jóvenes que no
# tenían obligación de votar
# c) Mostrar cuántos adultos mayores de 70 años votaron y porcentaje sobre el total de adultos que no
# tenían obligación de votar. 

def votos_asistencia(lista):
    T=0
    for i in range (len(lista)):
        S=lista[i].split()
        S=" ".join(S)
        R=S.find("SI")
        if R!=-1:
            T=T+1
        print(S)
    print("Votaron ",T," personas con un porcentaje de ",T/(len(lista))*100,"%")

def menores(lista):
    si=0
    ET=0
    for i in range (len(lista)):
        S=lista[i].split()
        S=" ".join(S)
        for j in range (3):
            coma=S.find(";")
            S=S[coma+1:len(lista[i])]
        for k in range(1):
            E=S[0:S.find(";")]
            print(E)
            if E==" 17" or E==" 16":
                ET=ET+1
                aux=S.find("SI")
                if aux!=-1:
                    si=si+1

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


#main
archivo=open("elecciones.txt","r")
lista=archivo.readlines()
archivo.close()
votos_asistencia(lista)
menores(lista)
mayores(lista)
