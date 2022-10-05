'''
Dado un archivo de texto que contiene información sobre facturación de una empresa. 
Los datos están separados por comas: fecha (formato aaaammdd), código de cliente, nombre de cliente y monto facturado

Crear un menú que llame a procedimientos y/o funciones para realizar lo siguiente:

a) Mostrar el listado de clientes (sin repetición) con sus respectivos códigos
b) Mostrar en pantalla los datos ordenados por fecha en forma ascendente. 
(recuerde que en formato aaaammdd se puede comparar y determinar si una fecha es menor que otra sin hacerninguna conversión)
c) Mostrar la cantidad de facturas realizadas en cada día
d) Generar un archivo que contenga las facturas que superen un monto elegido por el usuario (archivo separado por comas)
FUNCIONA CON FACTURAS.txt y FACTURAS2
'''
def mostrar(X):
    clientes=[]*len(texto)
    for i in range(len(texto)):
        clientes.append(texto[i][10:texto[i].find(",",20,-1)])
    orden=set(clientes)
    print(orden)
    return clientes


def datos_fecha(X):
    print(sorted(texto))


def facturas_dia(X):
    C=0
    print("Ingrese la fecha:")
    fecha = input("> ")
    for i in range(len(texto)):
        Fecha=texto[i][0:8]
        if fecha==Fecha:
            C=C+1
            print(texto[i])
    print("Se realizaron",C,"facturas")
    return fecha   


def facturas_monto(X):
    lista=[]
    print("Ingrese monto minimo")
    b=float(input("> "))
    for i in range(len(texto)):
        coma=texto[i].find(",",20,-1)
        Monto=(texto[i][coma+1:])
        a=int(Monto)
        if a>b:
            lista.append(texto[i])
    print(lista)
    return lista

def menu():
    print("(1) - Mostrar listado de clientes")
    print("(2) - Mostrar datos por fecha")
    print("(3) - Mostrar facturas en dia")
    print("(4) - Facturas que superen monto")
    print("(5) - Salir")


#main
archivo=open("facturas.txt","r")
texto=archivo.read()
print(texto)
archivo.close()
while True:
    menu()
    a =int (input("Ingrese una opcion:"))
    while( a>0 and a<6 ):
        if a == 1 :
            archivo=open("facturas.txt","r")
            texto=archivo.readlines()
            mostrar(texto)
            archivo.close()
            break
        if a == 2 :
            archivo=open("facturas.txt","r")
            texto=archivo.readlines()
            datos_fecha(texto)
            archivo.close()
            break
        if a == 3 :
            archivo=open("facturas.txt","r")
            texto=archivo.readlines()
            facturas_dia(texto)
            archivo.close()
            break
        if a == 4 :
            archivo=open("facturas.txt","r")
            texto=archivo.readlines()
            lista=facturas_monto(texto)
            archivo=open("facturas2.txt","w")
            archivo.writelines(lista)
            archivo.close()
            break
        if a == 5 : 
            quit()   
    else:
        print("Ingrese una opcion correcta")