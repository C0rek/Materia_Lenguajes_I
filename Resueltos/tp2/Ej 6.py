archivo=open("D:\TP2\Cliente.txt","r")
lista=archivo.readlines()
archivo.close()
nom=[""]*len(lista)
dom=[""]*len(lista)
for i in range(len(lista)):
    nom[i]=lista[i][0:29]
    nom[i]=nom[i].split()
    nom[i]=" ".join(nom[i])+"\n"
    dom[i]=lista[i][30:len(lista[i])]
for i in range (len(nom)):
    archivo=open("D:/TP2/"+nom[i][0:len(nom[i])-1]+".txt","w")
    archivo.write("Sr./a.:"+nom[i]+dom[i]+"\n"+"Tenemos el agrado de invitarlo/a a la presentacion de......")
    archivo.close()

