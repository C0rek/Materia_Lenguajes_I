#Ej 8
def menu():
    print("(1) Registrar nuevas facturas en el archivo")
    print("(2) Dado un cliente, obtener el total de las compras realizadas por el mismo")
    print("(3) Obtener el monto total de facturas agrupadas por tipo en un mes dado")
    print("(4) Listar las compras realizadas durante un mes determinado por un cliente dado.")
    print("(5) Generar una planilla Excel que contenga una hoja con las columnas correctamente identificadas y los datos del archivo")
    print("(6) Generar un gráfico de las ventas mensuales")
    print("(X) Salir")

def uno(archivo):
    N=int(input("Ingrese la cantidad de nuevas facturas a ingresar: "))
    for i in range (N):
        fecha=input("Ingrese la Fecha: ")
        nom=input("Ingrese el Nombre: ")
        tipo=""
        while tipo!="A" and tipo!="B":
            tipo=input("Ingrese el Tipo de factura (A/B): ")
        num=input("Ingrese el Numero de la factura: ")
        mont=input("Ingrese el monto de la factura")
        datos=fecha+", "+nom+", "+tipo+", "+num+", "+mont+"\n"
        print(datos)
        archivo.write(datos)

def dos(lista):
    nom=input("Ingrese el Nombre a buscar: ")
    aux=0
    for i in range (len(lista)):
        B=lista[i].find(nom)
        if B!=-1:
            B=lista[i].rfind(",")
            aux=aux+int(lista[i][B+1:len(lista[i])])
    print("El total de las compras realizadas por ",nom," es de ",aux)

def tres(lista):
    sumA=0
    sumB=0
    fecha=input("Ingrese el mes a buscar (En Numeors): ")
    for i in range(len(lista)):
        linea=lista[i][lista[i].find("/")+1:5]
        R=linea.find(fecha)

        if R!=-1:
            linea=lista[i]
            for i in range (2):
                coma=linea.find(",")
                linea=linea[coma+1:len(linea)]
            A=linea.find("A")
            if A!=-1:
                coma=linea.rfind(",")
                a=int(linea[coma+1:len(linea)])
                sumA=sumA+a
            else:
                coma=linea.rfind(",")
                b=int(linea[coma+1:len(linea)])
                sumB=sumB+b
    print("Para el mes ",fecha," los montos fueron:\nFactura A: ",sumA,"\nFactura B: ",sumB)

def cuatro(lista):
    nombre=input("Ingrese el nombre del cliente: ")
    fecha=input("Ingrese el mes a buscar (En Numeors): ")
    print("Las lista de compras realizadas en el mes ",fecha," por ",nombre,":")
    for i in range(len(lista)):
        linea=lista[i][lista[i].find("/")+1:5]
        R=linea.find(fecha)
        R2=lista[i].find(nombre)
        if fecha!=-1 and R2!=-1:
            aux=lista[i]
            fecha2=aux[0:aux.find(",")]#
            for i in range (2):
                coma=aux.find(",")
                aux=aux[coma+1:len(aux)]
            tipo=aux[0:aux.find(",")]#
            coma=aux.find(",")
            aux=aux[coma+1:len(aux)]
            num=aux[0:aux.find(",")]#
            coma=aux.find(",")
            aux=aux[coma+1:len(aux)]
            mont=aux[0:aux.find(",")]#
            print(fecha2,", Factura",tipo," Nro.",num," $",mont)

archivo=open("D:\TP2\Ej 8.txt","r")
texto=archivo.read()
print(texto)
archivo.close()
while True:
    menu()
    resp=input("Respuesta: ")
    if resp=="1":
        archivo=open("D:\TP2\Ej 8.txt","a")
        uno(archivo)
        archivo.close()
    if resp=="2":
        archivo=open("D:\TP2\Ej 8.txt","r")
        lista=archivo.readlines()
        archivo.close()
        dos(lista)
    if resp=="3":
        archivo=open("D:\TP2\Ej 8.txt","r")
        lista=archivo.readlines()
        archivo.close()
        tres(lista)
    if resp=="4":
        archivo=open("D:\TP2\Ej 8.txt","r")
        lista=archivo.readlines()
        archivo.close()
        cuatro(lista)
    if resp=="5":
        print("Error")
    if resp=="6":
        print("Error")
    if resp=="X" or resp=="x":
        print("Adioss!!!")
        break

