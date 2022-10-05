#Mostrar menu
def menu():
    print("Que desea hacer?")
    print("(1) Calcular la potencia de",num)
    print("(2) Contar la cantidad de digitos de", num)
    print("(3) Determinar si es capicua")
    print("(R) Ingresar otro numero")
    print("(X) Salir")

#Operaciones
def potencia(numero):
    X=int(input("Ingrese el exponente:"))
    print("La potencia es:",numero**X)

    
def cantidad_digitos(numero):
    numero=str(numero)
    print (numero,"tine",len(numero),"digitos")
    

def capicua(numero):
    X=numero
    aux2=0
    while X%10!=0 or X//10!=0:
        aux=X%10
        aux2=aux+aux2*10
        X=X//10
    if aux2==numero:
        print("Es Capicua")
    else:
        print("No es Capicua")



while True:
    num=int(input("Ingrese un numero:"))
    while True:
        menu()
        resp=input("Opcion:")
        if resp=="R" or resp=="r":
            break
        if resp=="1":
            potencia(num)
        if resp=="2":
            cantidad_digitos(num)        
        if resp=="3":
            capicua(num)
        if resp=="X" or resp=="x":
            break
    if resp=="X" or resp=="x":
            break
