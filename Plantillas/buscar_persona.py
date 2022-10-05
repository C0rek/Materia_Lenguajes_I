def buscar_persona():
    print("Ingrese el nombre y apellido de la persona")
    nombre=input("> ")
    B=0
    for i in range(len(texto)):
        R=texto[i][0:20].find(nombre)
        if R!=-1:
            print(texto[i])
            B=1
    if B==0:
        print("La persona no esta agendada")