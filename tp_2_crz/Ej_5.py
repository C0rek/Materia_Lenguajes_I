# Ejercicio 5.
# Escribir un programa con las siguientes opciones de menú:
# a. cargar datos de alumnos (nombre y apellido, carrera, año de cursado, promedio de notas) y
# los almacene en un archivo.
# b. mostrar en pantalla el listado de alumnos contenidos en el archivo, ordenados por apellido.
# c. dada una carrera, buscar en el archivo los alumnos de esa carrera y mostrarlos ordenados por
# sus promedios
# d. dada una carrera, buscar en el archivo los alumnos de esa carrera y mostrarlos ordenados por
# año de cursado 

def cargar_datos_alumno(x):
    print("Ingrese apellido y nombre")
    nombre_completo=input("> ")
    print("Ingrese la carrera")
    carrera=input("> ")
    print("Ingrese año de cursado")
    año_de_cursado=input("> ")
    print("Ingrese promedio de notas")
    promedio=input("> ")
    datos = nombre_completo +", " +carrera+ ", " +año_de_cursado+ ", " +promedio
    print(datos)
    archivo.write(datos)


def ordenar_alfabeticamente(X):     #no los ordena con salto de linea
    for i in range(1):
        b=sorted(archivo)
    print(b)

#mas facil hacerlo con matrices
def buscar_carrera(X):
    c=0
    Carrera=[]
    alumnos=[]
    print("Ingrese la carrera a buscar(Primera con mayusc)")
    carrera=input("> ")
    for i in range(len(texto)):
        coma=texto[i].find(",")
        aux=texto[i][coma+1:len(texto[i])]
        coma_2=aux.find(",")
        Carrera.append(aux[1:coma_2])                #Carrera es el str encontrado
        if carrera==Carrera[i]:
            num=len(Carrera)-1
            c=c+1
            if c==0:
                print("No hay alumnos en esa carrera")
            else:
                alumnos.append(texto[num])
                Promedio=[]

                promedio=texto[i][-2:-1]
                Promedio.append(promedio)
                Promedio.sort()

            print(Promedio)
            print(alumnos)
    

        

            



    





def menu():
    print("(1) - Cargar datos del alumno:")
    print("(2) - Mostrar el listado de alumnos ordenados por apellidos:")
    print("(3) - Dada una carrera, mostrar alumnos por promedios:")
    print("(4) - Dada una carrera, mostrar alumnos por cursado:")
    print("(5) - Salir")

#main
archivo=open("Copia.txt","r")
texto=archivo.read()
print(texto)
print()
print("Menu:")
archivo.close()
while True:
    menu()
    a =int (input("Ingrese una opcion:"))
    while( a>0 and a<6):

        if a == 1 :
            archivo=open("Copia.txt","a")
            cargar_datos_alumno(archivo)
            archivo.close()
            break

        if a == 2 :
            archivo=open("Copia.txt","r")
            ordenar_alfabeticamente(archivo)
            archivo.close()
            break

        if a == 3 :
            archivo=open("Copia.txt", "r")
            texto=archivo.readlines()
            buscar_carrera(texto)
            archivo.close()
            break

        # if a == 4 :

        if a == 5 :    
            quit()
    else:
        print("Ingrese una opcion correcta")