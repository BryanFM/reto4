import json
from time import sleep
from os import getcwd, makedirs, listdir
from shutil import copy

class Persona():
    def __init__(self, dni, nombre, edad,tipo):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def registrar_persona(self):
        print("""\n ¿Qué tipo de persona es usted?\n
                1) Docente
                2) Alumno\n""")
        tipo = input("> ")
        if tipo == "1":
            tipo = "Docente"
            self.crear_persona(tipo)
        elif tipo == "2":
            tipo = "Alumno"
            self.crear_persona(tipo)
        else:
            print("\nOpción inválida")

    def inputnumber(self,message):
        while True:
            try:
                nota = int(input(message))       
            except ValueError:
                print("El dato ingresado no es numérico")
                continue
            else:
                return nota
    
    def crear_persona(self, tipo):
        dni = input("\nIngresa su N° DNI > ")
        nombre = input("\nIngresa su nombre > ")
        edad = input("\nIngresa su edad > ")
        if(tipo == "Alumno"):
            count = 1
            list_notas = []
            while count <= 4:
                nota = self.inputnumber(f"Ingrese nota {count}: ")
                list_notas.append(nota)
                count = count + 1
            promedio = sum(list_notas) / len(list_notas)
            nota_mayor = max(list_notas)
            nota_menor = min(list_notas)
            nuevo_p = Alumno(dni, nombre, edad, tipo,list_notas,nota_mayor,nota_menor,promedio)
            datos = {
                "dni": nuevo_p.dni,
                "nombre": nuevo_p.nombre,
                "edad": nuevo_p.edad,
                "tipo": nuevo_p.tipo,
                "notas": nuevo_p.notas,
                "notamaxima": nuevo_p.notamaxima,
                "notaminima": nuevo_p.notaminima,
                "promedio": nuevo_p.notapromedio
            }
            self.guardar_alumno(nuevo_p)
        else:
            nuevo_p = Persona(dni, nombre, edad, tipo)
            datos = {
                "dni": nuevo_p.dni,
                "nombre": nuevo_p.nombre,
                "edad": nuevo_p.edad,
                "tipo": nuevo_p.tipo
            }
            self.guardar_persona(nuevo_p)
        print(f"\nUsted ha sido registrado exitosamente.")

    def guardar_persona(self, datos):
        try:
            file = open("docente.txt", mode='a') # Sobreescribir -> mode='w'
            persona = f"{datos.dni} - {datos.nombre} - {datos.edad}\n"
            file.write(persona)
        except Exception as e:  # IOError
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print("Docente añadido")

    def guardar_alumno(self, datos):
        try:
            file = open("alumno.txt", mode='a') # Sobreescribir -> mode='w'
            persona = f"{datos.dni} - {datos.nombre} - {datos.edad} - {datos.notas} - {datos.notamaxima} - {datos.notaminima} - {datos.notapromedio}\n"
            file.write(persona)
        except Exception as e:  # IOError
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print("Alumno añadido")

    def mostrar_personas(self):
        try:
            file = open("docente.txt", mode='r', encoding='utf-8')
            for linea in file.readlines():
                print(linea)
        except Exception as e: # IOError
            print(f'{str(e)}')
        finally: # Bloque que se ejecuta si esta todo bien o si esta todo mal
            if(file):
                file.close()
                print("Se visualiza el archivo")

    def mostrar_alumno(self):
        try:
            file = open("alumno.txt", mode='r', encoding='utf-8')
            for linea in file.readlines():
                print(linea)
        except Exception as e: # IOError
            print(f'{str(e)}')
        finally: # Bloque que se ejecuta si esta todo bien o si esta todo mal
            if(file):
                file.close()
                print("Se visualiza el archivo")

    def interfaz(self):
        while True:
            print("""\nBienvenido al sistema de registro de personas y alumnos
            ¿Qué operación desea realizar?
            1) Registrarme
            2) Ver a los docentes registrados
            3) Ver a los alumnos registrados
            4) Salir\n""")
            opcion = input("> ")
            if opcion == "1":
                self.registrar_persona()
            elif opcion == "2":
                self.mostrar_personas()
            elif opcion == "3":
                self.mostrar_alumno()
            elif opcion == "4":
                print("\nGracias por usar esta aplicación")
                sleep(2)
                quit()
            else:
                print("\nHas introducido una opción erronea")

class Alumno(Persona):
    def __init__(self, dni, nombre, edad,tipo,notas,notamaxima,notaminima,notapromedio):
        Persona.__init__(self, dni, nombre, edad,tipo)

        self.notas = notas
        self.notamaxima = notamaxima
        self.notaminima = notaminima
        self.notapromedio = notapromedio

class Iniciar(Persona):
    def __init__(self):
        self.interfaz()

Iniciar()