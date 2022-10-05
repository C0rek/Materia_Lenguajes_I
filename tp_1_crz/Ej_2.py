
#Crear un programa que determine el valor máximo entre 10 números utilizando las 
#funciones/procedimientos del ejercicio anterior. 

#defino cargar vector
def carga_vector(vector):       
    for i in range(10):
        vector[i]=int(input("Ingrese un valor :"))
    return (vector)

#defino el valor maximo de los 10 numeros
def max_vector():
    max_v10= max(A)
    print("El valor maximo es :",max_v10)

#main
A=[""]*10
carga_vector(A)
max_vector()