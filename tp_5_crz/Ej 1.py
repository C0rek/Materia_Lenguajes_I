# Ejercicio 1. Realizar un programa Python que tenga una clase llamada Persona. 
# Sus atributos son: nombre, edad y domicilio. 
# Implementar los métodos necesarios para: 
# a) Inicializar los atributos 
# b) Mostrar los datos de una persona 
# c) Indicar si la persona es mayor de edad o no.

class Persona:
#atributos
    def desc(self, nombre, edad, domicilio):
        self.nombre = nombre
        self.edad = edad
        self.domicilio = domicilio

#main
persona = Persona()
persona.nombre=input("Ingrese el nombre de la persona: ")
persona.edad=int(input("Ingrese la edad de la persona: "))
persona.domicilio=(input("Ingrese el domicilio de las personas: "))

print(persona.edad)
print(persona.nombre)
print(persona.domicilio)