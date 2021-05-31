class Menu:
    __switcher:None

    def __init__(self):
        self.__switcher={1:self.opcion1,
                        2: self.opcion2,
                        3: self.opcion3,
                        4: self.opcion4,
                        5: self.opcion5,
                        6: self.opcion6,
                        0: self.salir}

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,opcion,coleccion):
        funcion=self.__switcher.get(opcion,lambda:print("\nOpcion no valida."))
        funcion(coleccion)

    #---------------------------------------------------------OPCION 1
    def opcion1(self,coleccion):
        dni=int(input("\nIngrese DNI: "))
        cantHoras=int(input("\nIngrese cantidad de horas: "))
        coleccion.registrarHoras(dni,cantHoras)

    #---------------------------------------------------------OPCION 2
    def opcion2(self,coleccion):
        tarea=input("\nIngrese tarea: ")
        tarea=tarea.lower()
        if tarea not in ['carpinteria','plomeria','electricidad']:
            print("\nTarea no encontrada.\nLas tareas son: carpinteria, plomeria, electricidad")
        else:
            coleccion.totalTarea(tarea)

    #---------------------------------------------------------OPCION 3
    def opcion3(self,coleccion):
        coleccion.listarAyuda()

    #---------------------------------------------------------OPCION 4
    def opcion4(self,coleccion):
        coleccion.listarEmpleados()

    #---------------------------------------------------------OPCION 5
    def opcion5(self,coleccion):
        usuario=input("Usuario: ")
        password=input("Contrasenia: ")
        if usuario=='uTesorero' and password=='ag@74ck':
            band=False
            while not band:
                try:
                    dni=int(input("DNI: "))
                    if dni<0:
                        raise ValueError
                except ValueError:
                    print("DNI incorrecto,intente de nuevo.")
                else:
                    coleccion.gastosSueldoPorEmpleado(dni)
                    band=True
        else:
            print("Usuario o contrasenia incorrecto.")

    #---------------------------------------------------------OPCION 6
    def opcion6(self,coleccion):
        usuario=input("Usuario: ")
        password=input("Contrasenia: ")
        band=False
        if usuario=='uGerente' and password=='ufc77':
            print("Inicio de secion correcto.")
            while not band:
                try:
                    print("\n---------------------------------------------")
                    print("1. Modificar sueldo basico de un empleado de planta")
                    print("2. Modificar valor que se paga por hora de un empleado extrerno.")
                    print("3. Modificar el valor que se paga por viatico de un empleado contratado.")
                    print("--------------------------------------------------------------")
                    op=int(input("\nIngrese opcion: "))
                    if op not in [1,2,3]:
                        raise ValueError
                except ValueError:
                    print("Error")
                else:
                    band=True
            band=False
            while not band:
                try:
                    dni=int(input("DNI: "))
                    if dni<0:
                        raise ValueError
                    if op==1:
                        nuevoSueldo:float(input("Nuevo sueldo: "))
                        coleccion.modificarBasicoEPlanta(dni,nuevoSueldo)
                    elif op==2:
                        nuevoViatico=float(input("Nuevo viatico: "))
                        coleccion.modificarViaticoEExterno(dni,nuevoViatico)
                    elif op==3:
                        nuevoValor=float(input("Nuevo valor por hora: "))
                        coleccion.modificarValorEPorHora(dni,nuevoValor)
                except ValueError:
                    print("Incorrecto, intente de nuevo.")
                else:
                    band=True
        else:
            print("Usuario o contrasenia invalido.")

    #---------------------------------------------------------SALIR
    def salir(self,coleccion):
        print("\nChau :)")