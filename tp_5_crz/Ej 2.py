# Ejercicio 2.
# Se desea gestionar los datos de alumnos, profesores y personal administrativo de un instituto educativo.
# Además de los datos personales, a los alumnos se les asocia una carrera y año de cursado. Para los
# profesores se mantiene el título profesional (Lic., Ing., Prof., etc.), facultad en cual es docente y
# antigüedad en el cargo. Para el personal administrativo, se quiere registrar área de trabajo, cargo y
# antigüedad.
# a) Defina las clases Alumno, Profesor y Personal Administrativo. ¿Cuáles son los atributos de estas
# clases? ¿Cuáles son los métodos de cada clase?
# b) ¿Es posible utilizar la clase Persona del Ejercicio 1? En caso afirmativo, hágalo. 


	Registrar área de trabajo (String)
	Cargo (String)
	Antigüedad (Int)
Métodos:
	Organizar los datos de los alumnos
	Controlar que el alumno pague la cuota
	Asistir al instituto


class Persona:
    def __init__(self):
        self.nombre = nombre
        self.edad = edad


class Alumno:
    def __init__(self):
        self.carrera = carrera
        self.año_cursado = año_cursado
    def rendir_parciales(self):
        self.nota=(int(input("Ingrese la nota del examen: ")))


class Profesor:
    def __init__(self):
        self.titulo = titulo
        self.facultad = facultad
        self.antiguedad = antiguedad
    def tomar_examenes(self):
        self.tomar_examenes = print("El maestro toma el examen .. ")


class Personal:
    def organizar_datos(self):
        self.datos = print("Organiza los datos ..")

