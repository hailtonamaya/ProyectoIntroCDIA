import os
import pickle
import msvcrt

#Definicion de la Clase
class niveles:
    def __init__(self):
        self.tipo = ""
        self.descripcion = ""
        self.precioPrimeraVez2 = 0 #El numero indica la cantidad de años
        self.precioPrimeraVez5 = 0
        self.precioRenovacion2 = 0
        self.precioRenovacion5 = 0
        self.activo = False

    def __init__(self, tipo, descripcion, precioPrimeraVez2, precioPrimeraVez5, precioRenovacion2, precioRenovacion5, activo):
        self.tipo = tipo
        self.descripcion = descripcion
        self.precioPrimeraVez2 = precioPrimeraVez2
        self.precioPrimeraVez5 = precioPrimeraVez5
        self.precioRenovacion2 = precioRenovacion2
        self.precioRenovacion5 = precioRenovacion5
        self.activo = activo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion
    
    def setPrecioPrimeraVez2(self, precioPrimeraVez2):
        self.precioPrimeraVez2 = precioPrimeraVez2

    def getPrecioPrimeraVez2(self):
        return self.precioPrimeraVez2
    
    def setPrecioPrimeraVez5(self, precioPrimeraVez5):
        self.precioPrimeraVez5 = precioPrimeraVez5

    def getPrecioPrimeraVez5(self):
        return self.precioPrimeraVez5
    
    def setPrecioRenovacion2(self, precioRenovacion2):
        self.precioRenovacion2 = precioRenovacion2

    def getPrecioRenovacion2(self):
        return self.precioRenovacion2
    
    def setPrecioRenovacion5(self, precioRenovacion5):
        self.precioRenovacion5 = precioRenovacion5

    def getPrecioRenovacion5(self):
        return self.precioRenovacion5
    
    def setActivo(self, activo):
        self.activo = activo

    def getActivo(self):
        return self.activo

    def Imprimir(self):
        print("Tipo: ", self.tipo)
        print("Descripcion: ", self.descripcion)
        print("Precio Primera Vez 2 años: L.", self.precioPrimeraVez2)
        print("Precio Primera Vez 5 años: L.", self.precioPrimeraVez5)
        print("Precio Renovacion 2 años: L.", self.precioRenovacion2)
        print("Precio Renovacion 5 años: L.", self.precioRenovacion5)

    def ImprimirActivo(self):
        if self.activo:
            print("Tipo: ", self.tipo)
            print("Descripcion: ", self.descripcion ,"\n")
   
class persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.DNI = ""
        self.esPrimeravez = True
        self.niveles = []

    def __init__(self, nombre, edad, DNI, esPrimeravez, niveles):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.esPrimeravez = esPrimeravez
        self.niveles = niveles

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad
        
    def setDNI(self, DNI):
        self.DNI = DNI

    def getDNI(self):
        return self.DNI
        
    def setEsPrimeravez(self, esPrimeravez):
        self.esPrimeravez = esPrimeravez

    def getEsPrimeravez(self):
        return self.esPrimeravez
        
    def setNiveles(self, niveles):
        self.niveles = niveles

    def getNiveles(self):
        return self.niveles
    
    def Imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.DNI)
        print("Es Primera Vez: ", self.esPrimeravez , "\n")
        print("Usted cuenta con las siguientes licencias: ")
        for nivel in self.niveles:
                nivel.ImprimirActivo()

#Programa Princiapl
class Main:
    def press():
        print("Presione cualquier tecla para continuar...")
        msvcrt.getch()

    os.system('clear')
        
    Niveles = []
    with open('Niveles.nv', 'rb') as file:
        Niveles = pickle.load(file)
    file.close() 

    Personas = []   
    with open("Personas.pr", "rb") as file:
        Personas = pickle.load(file)
    file.close()        
    
    #Niveles[0].setActivo(True)
    #Niveles[1].setActivo(True)
    #Personas.append(persona("Hailton Amaya", "18", "0501200500100", False, Niveles))

    TiposAplica = []
    Menu = Opcion = str("")
    personaActual = None
    nivel = None
    licenciaAObtener = None
    esValido = False
    print("****Bienvenido al DNVT para la Solicitud de la Licencia de Conducir****")

    while Menu != "C":
        Menu = input("A.-> Ingresar Datos o Solicitar Nueva Licencia\nB.-> Ver mi informacion\nC.-> Salir\nSeleccion una opcion: ").capitalize()
        os.system('clear')

        if Menu == "A":
            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            DNI = input("Ingrese su DNI(Sin guiones): ")
            os.system('clear')
            
            # Verificar si ya existe la persona en la base de datos
            for p in Personas:
                if p.getDNI() == DNI:
                    personaActual = p
                    break

            if edad < 18:
                print("Usted no puede solicitar una licencia de conducir porque es menor de edad!!!")
                press()
            elif personaActual == None:
                personaActual = persona(nombre, edad, DNI, True, Niveles)
                Personas.append(personaActual)
                nivel = personaActual.getNiveles()

                print("Usted aplica a las siguientes opciones:")
                if personaActual.getEsPrimeravez():
                    Niveles[0].Imprimir()
                    print("")

                    Niveles[1].Imprimir()
                    print("")

                    TiposAplica.append(Niveles[0].getTipo())
                    TiposAplica.append(Niveles[1].getTipo())

                    opcion = input("Seleccione una opcion(A/B): ").capitalize()
                    os.system('clear')

                    for t in TiposAplica:
                        if t == opcion:
                            esValido = True
                            break
                    
                    #Cargar tipo de licencia a obtener
                    for i in range(len(nivel)):
                        if nivel[i].getTipo() == opcion:
                            licenciaAObtener = nivel[i]
                            break
                    if esValido:
                        print("A.-> Primera Vez 2 años L.", licenciaAObtener.getPrecioPrimeraVez2()) 
                        print("B.-> Primera Vez 5 años L.", licenciaAObtener.getPrecioPrimeraVez5())
                        opcion = input("Seleccione una opcion(A/B): ").capitalize()
                        os.system('clear')

                        if opcion == "A":
                            print("Estamos verficando su informacion...")
                            for nivel in personaActual.getNiveles():
                                if nivel.getTipo() == licenciaAObtener.getTipo():
                                    nivel.setActivo(True)
                                    break
                            for P in Personas:
                                if P.getDNI() == DNI:
                                    P = personaActual
                                    break
                            print("Felicidades, usted ha obtenido su licencia Tipo " , licenciaAObtener.getTipo(), " por 2 años!!!")
                            press()
                            #Cargar nueva informacion en el archivo    
                            with open("Personas.pr", "wb") as file:
                                pickle.dump(Personas, file)
                            file.close()
                        elif opcion == "B":
                            print("Estamos verficando su informacion...")
                            for nivel in personaActual.getNiveles():
                                if nivel.getTipo() == licenciaAObtener.getTipo():
                                    nivel.setActivo(True)
                                    break
                            for P in Personas:
                                if P.getDNI() == DNI:
                                    P = personaActual
                                    break
                            print("Felicidades, usted ha obtenido su licencia Tipo ", licenciaAObtener.getTipo(), " por 5 años!!!")
                            press()
                            #Cargar nueva informacion en el archivo    
                            with open("Personas.pr", "wb") as file:
                                pickle.dump(Personas, file)
                            file.close()
                        else:
                            print("Opcion no valida!!!")
                            press()
                    else:
                        print("Usted seleccion un tipo de licencia invalida!!!")
                        press()
            else:
                #Cargar informacion de los tipos de licencia que tiene la persona
                nivel = personaActual.getNiveles()
                for i in range(len(nivel)):
                    if nivel[i].getActivo() == False:
                        TiposAplica.append(nivel[i].getTipo())
                        nivel[i].Imprimir()
                        print("")

                if len(TiposAplica) == 0:
                    print("No aplica a ningun nivel")
                    press()
                else:
                    print("Seleccione una opcion(" , end="")
                    for i in range(len(TiposAplica)):
                        print(TiposAplica[i], end="")
                        if i < len(TiposAplica) - 1:
                            print("/" , end="")
                    opcion = input("): ").capitalize()
                    os.system('clear')

                    for t in TiposAplica:
                        if t == opcion:
                            esValido = True
                            break
                    
                    #Cargar tipo de licencia a obtener
                    for i in range(len(nivel)):
                        if nivel[i].getTipo() == opcion:
                            licenciaAObtener = nivel[i]
                            break
                    if esValido:
                        print("A.-> Primera Vez 2 años L.", licenciaAObtener.getPrecioPrimeraVez2()) 
                        print("B.-> Primera Vez 5 años L.", licenciaAObtener.getPrecioPrimeraVez5())
                        opcion = input("Seleccione una opcion(A/B): ").capitalize()
                        os.system('clear')

                        if opcion == "A":
                            print("Estamos verficando su informacion...")
                            for nivel in personaActual.getNiveles():
                                if nivel.getTipo() == licenciaAObtener.getTipo():
                                    nivel.setActivo(True)
                                    break
                            for P in Personas:
                                if P.getDNI() == DNI:
                                    P = personaActual
                                    break
                            print("Felicidades, usted ha obtenido su licencia Tipo " , licenciaAObtener.getTipo(), " por 2 años!!!")
                            press()
                            #Cargar nueva informacion en el archivo    
                            with open("Personas.pr", "wb") as file:
                                pickle.dump(Personas, file)
                            file.close()
                        elif opcion == "B":
                            print("Estamos verficando su informacion...")
                            for nivel in personaActual.getNiveles():
                                if nivel.getTipo() == licenciaAObtener.getTipo():
                                    nivel.setActivo(True)
                                    break
                            for P in Personas:
                                if P.getDNI() == DNI:
                                    P = personaActual
                                    break
                            print("Felicidades, usted ha obtenido su licencia Tipo ", licenciaAObtener.getTipo(), " por 5 años!!!")
                            press()
                            #Cargar nueva informacion en el archivo    
                            with open("Personas.pr", "wb") as file:
                                pickle.dump(Personas, file)
                            file.close()
                        else:
                            print("Opcion no valida!!!")
                            press()
                    else:
                        print("Usted seleccion un tipo de licencia invalida!!!")
                        press()

        elif Menu == "B":

            DNI = input("Ingrese su DNI(Sin guiones): ")
            os.system('clear')

            # Verificar si ya existe la persona en la base de datos
            for p in Personas:
                if p.getDNI() == DNI:
                    personaActual = p
                    break

            if personaActual != None:
                print("****Informacion de la Persona****")
                personaActual.Imprimir()
            else:
                print("Usted ha ingresado un DNI invalido o es la primera vez que solicita una licencia!")
            press()


            #Reiniciar valores y Limpiar Pantalla
        
        
        TiposAplica = []
        personaActual = None
        nivel = None
        esValido = False
        os.system('clear')
                                