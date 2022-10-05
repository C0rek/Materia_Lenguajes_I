#Crear un programa que determine el valor máximo entre tres números. ¿Cuántas funciones y/o 
#procedimientos son necesarios para resolver este problema? ¿Cuántos parámetros? 


#defino maximo entre 2 numeros
def max(X,Y):
    if (X>Y):
        M=X
    else:
        M=Y
    return M 

#variables solicitadas
A = int(input("Ingrese el primer numero: "))
B = int(input("Ingrese el segundo numero: "))
C = int(input("Ingrese el tercer numero: "))

#comparacion
Mayor=max(A,B)
Mayor=max(Mayor,C)

#imprimo
print("El mayor es : ",Mayor )
