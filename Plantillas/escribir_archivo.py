archivo.append()

archivo=open("agenda.txt","r")
            texto=archivo.readlines()
            print(texto)
            nueva_persona()
            archivo=open("agenda.txt","w")
            print(texto)
            archivo.writelines(texto)
            archivo.close()