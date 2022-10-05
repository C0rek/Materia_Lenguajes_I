def menu():
    print("(1) - ")
    print("(2) - ")
    print("(3) - ")
    print("(4) -")
    print("(5) - Salir")




#main
archivo=open("Copia.txt","a")
texto=archivo.read()
print(texto)
archivo.close()
while True:
    menu()
    a =int (input("Ingrese una opcion:"))
    while( a>0 and a<6 ):
        if a == 1 :

            break
        if a == 2 :

            break
        if a == 3 :

            break
        if a == 4 :

            break
        if a == 5 : 
            quit()   
    else:
        print("Ingrese una opcion correcta")