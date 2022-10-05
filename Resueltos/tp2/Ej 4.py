#Ej 4
def reemplazar(texto):
    palabra=input("Ingrese la palabra a buscar: ")
    reemplazar=input("Ingrese la palabra que la reemplazara: ")
    texto=texto.replace(palabra,reemplazar)
    return texto

archivo=open("D:\TP2\Ej 4.txt","r")
texto=archivo.read()
print(texto)
texto=reemplazar(texto)
archivo=open("D:\TP2\Ej 4.txt","w")
print(texto)
archivo.write(texto)
archivo.close()
