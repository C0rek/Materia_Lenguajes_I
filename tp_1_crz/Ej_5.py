#Crear un programa que contenga un menú con las siguientes opciones:
#- Calcular la potencia K de un número X. 
#- Obtener la cantidad de dígitos de un número X.
#- Determinar si un número es capicúa.
#Implementar funciones para cada opción del menú.


#defino menu
def menu():
    print("Marque una opcion")
    print("(1) - Calcular potencia de",num)
    print("(2) - Calcular cantidad de digitos de",num)
    print("(3) - Determinar si es capicua")
    print("(R) - Poner otro numero")
    print("(X) - Salir")


#Operaciones
#defino calcular potencia
def cal_potencia(num):
    X=int(input("Ingrese el exponente:"))
    print("El valor es:",num**X)

#defino cantidad de digitos
def cant_digitos(num):
    num=str(num)
    num=len(num)
    x=print("Tiene",num,"digitos") # len = cuenta digitos


#defino capicua
def capicua(num):
    X=num
    aux2=0

    while X%10 !=0 or X//10 !=0:
        aux=X%10
        aux2=aux+aux2*10
        X=X//10

    if aux2==num:
        print("Es capicua")
    else:
        print("No es capicua") 

#main
while True:
    num=int(input("Ingrese un numero:"))
    if True:
        menu()
        resp=input("Ingrese una opcion:")
        if resp=="R" or resp=="r":
            break
        if resp=="1":
            cal_potencia(num)
            break
        if resp=="2":
            cant_digitos(num)
            break
        if resp=="3":
            capicua(num)
            break
        if resp=="X" or resp=="x":
            break
         