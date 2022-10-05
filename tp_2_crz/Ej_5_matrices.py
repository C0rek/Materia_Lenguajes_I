def cargar(lista):
    N=int(input("Ingrese la cantidad de alumnos que desea añadir: "))
    lista=[[0 for i in range (4)]for j in range (N)]
    for i in range (N):
        lista[i][0]=input("Ingrese el Apellido y Nombre del Alumno:")
        lista[i][1]=input("Ingrese la Carrera del Alumno:")
        lista[i][2]=input("Ingrese el Año de Cursado del Alumno:")
        lista[i][3]=input("Ingrese el Promdeio del Alumno:")
    print(lista)
    return lista
        
   
def mostrar_a(lista):
    print (sorted(lista,key=lambda x:x[0]))

def buscar_promedio(lista):
    carrera=input("Ingrese la carrera: ")
    c=0
    for i in range (len(lista)):
        if carrera==lista[i][1]:
            c=c+1
    if c==0:
        print("No hay ningun alumno en esa carrera")
        return
    if c==1:
        aux=[""]*2
        for j in range (len(lista)):
            if carrera==lista[j][1]:
                aux[0]=lista[j][0]
                aux[1]=lista[j][3]
                print(aux)
    else:
        aux=[[0 for i in range (c)]for j in range (2)]
        i=0
        for j in range (c):
            while i<(len(lista)):
                if carrera==lista[i][1]:
                    aux[j][0]=lista[i][0]
                    aux[j][1]=lista[i][3]
                    i=i+1
                    break
                i=i+1
        print(sorted(aux,key=lambda x:x[1]))


    
def buscar_año(lista):
    carrera=input("Ingrese la carrera: ")
    c=0
    for i in range (len(lista)):
        if carrera==lista[i][1]:
            c=c+1
    if c==0:
        print("No hay ningun alumno en esa carrera")
        return
    if c==1:
        aux=[""]*2
        for j in range (len(lista)):
            if carrera==lista[j][1]:
                aux[0]=lista[j][0]
                aux[1]=lista[j][2]
                print(aux)
    else:
        aux=[[0 for i in range (c)]for j in range (2)]
        i=0
        for j in range (c):
            while i<(len(lista)):
                if carrera==lista[i][1]:
                    aux[j][0]=lista[i][0]
                    aux[j][1]=lista[i][2]
                    i=i+1
                    break
                i=i+1
        print(sorted(aux,key=lambda x:x[1]))       
            
def transformar(lista,texto):
    texto=[""]*len(lista)
    for i in range (len(lista)):
        texto[i]=("Nombre: "+lista[i][0]+"/ Carrerra: "+lista[i][1]+"/ Año: "+lista[i][2]+"/ Promedio: "+lista[i][3]+"\n")
    print(texto)
    return texto

def menu():
    print("(1) Ingresar Alumnos")
    print("(2) Alumnos ordenados")
    print("(3) Alumnos ordenados por Promedio de una carrera")
    print("(4) Alumnos ordenados por Año de cursado de una carrera")
    print("(0) Salir")    

#cuerpo
lista=[]
texto=[]
while True:
    menu()
    R=input("Respuesta: ")
    if R=="1":
        lista=cargar(lista)
    if R=="2":
        mostrar_a(lista)
    if R=="3":
        buscar_promedio(lista)
    if R=="4":
        buscar_año(lista)
    if R=="0":
        print("Quiere Guardar lo siguiente en un archivo de texto? (si/no)")
        texto=transformar(lista,texto)
        r=input("Respuesta: ")
        if r=="si":
            archivo=open("D:\TP2\Ej 5.txt","w")
            archivo.writelines(texto)
            archivo.close()
            print("Hasta Pronto!!!")
            break
        if r=="no":
            print("(1) Regresar\n (0) Salir")
            R2=int(input("Respuesta: "))
            if R2==0:
                print("Hasta Pronto!!!")
                break
            