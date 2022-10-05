# En un archivo de texto, Cliente.txt, se tiene apellido y nombres de clientes y sus correspondientes
# direcciones, donde los primeros 30 caracteres corresponden al apellido y nombre, y los restantes 40
# caracteres al domicilio. En otro archivo de texto, Carta.txt, se tiene escrita una carta de presentación
# de un producto. Escribir un programa para enviar cartas personalizadas a cada cliente. El nombre de
# cada archivo generado debe ser el apellido del cliente y extensión txt. 

archivo=open("Cliente.txt","r")
lista=archivo.readlines()
archivo.close()
nombre=[""]*len(lista)
domicilio=[""]*len(lista)        
for i in range(len(lista)):
    nombre[i]=lista[i][0:29]
    nombre[i]=nombre[i].split()           #split devuelve una cadena de elementos
    nombre[i]=" ".join(nombre[i])+"\n"
    domicilio[i]=lista[i][30:len(lista[i])]
for i in range(len(nombre)):
    archivo=open(nombre[i][0:len(nombre[i])-1]+".txt","w")
    archivo.write("Sr./a " +nombre[i]+domicilio[i]+ "Tenemos el agrado de de invitarlo/a la presentacion de ")
    archivo.close()