#Dado un archivo de texto llamado Prueba.txt, se necesita buscar una palabra X (a elección del usuario)
#y reemplazarla por una palabra Y (también a elección del usuario). 

def reemplazar(texto):
    print("Ingrese una palabra que quiere reemplazar:")       
    palabra=input("> ")
    print("Ingrese la palabra por la cual quiere reemplazar:") #R por Reemplazo
    reemplazo=input("> ")
    texto=texto.replace(palabra,reemplazo)
    return texto


#main
archivo=open("Prueba.txt","r")
texto=archivo.read()
print(texto)
texto=reemplazar(texto)
archivo=open("Pruebas.txt","w")
print(texto)
archivo.write(texto)
archivo.close()