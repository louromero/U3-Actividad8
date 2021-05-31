from datetime import date
import csv
import numpy as np
from Empleado import Empleado
from EmpleadoPlanta import EmpleadoPlanta
from EmpleadoExterno import EmpleadoExterno
from EmpleadoContratado import EmpleadoContratado
from InterfazTesorero import ITesorero
from InterfazGerente import IGerente
from zope.interface import implementer

@implementer(IGerente)
@implementer(ITesorero)
class Coleccion:
    __arreglo=None
    __dimension=0
    __actual=0

    def __init__(self,dimension):
        self.__dimension=dimension
        self.__actual=0
        self.setArreglo(dimension)

    def setArreglo(self,dimension):
        self.__arreglo=np.empty(dimension,dtype=Empleado)

        with open("planta.csv","r") as archivo:
            reader=csv.reader(archivo,delimiter=",")
            for x in reader:
                empleado= EmpleadoPlanta(float(x[0]),int(x[1]),int(x[2]),x[3],x[4],int(x[5]))
                self.addArreglo(empleado)

        with open("contratado.csv","r") as archivo:
            reader=csv.reader(archivo,delimiter=",")
            for x in reader:
                empleado=EmpleadoContratado(x[0],x[1],int(x[2]),int(x[3]),x[4],x[5],int(x[6]))
                self.addArreglo(empleado)

        with open("externo.csv","r") as archivo:
            reader=csv.reader(archivo,delimiter=",")
            for x in reader:
                empleado=EmpleadoExterno(x[0],x[1],x[2],float(x[3]),float(x[4]),float(x[5]),int(x[6]),x[7],x[8],int(x[9]))
                self.addArreglo(empleado)

    def getEmpleado(self,dni):
        arreglo=self.getArreglo()
        band=False
        ind=0
        retorno=None
        while not band and ind<len(arreglo):
            empleado=arreglo[ind]
            if empleado.getDNI()==dni:
                band=True
                retorno=empleado
            else:
                ind+=1
        return retorno

    def getArreglo(self):
        return self.__arreglo

    def addArreglo(self,unEmpleado):
        actual=self.__actual
        dimension=self.__dimension
        arreglo=self.getArreglo()
        if actual < dimension:
            arreglo[actual]= unEmpleado
            self.__actual+=1
        else:
            print("\nArreglo lleno,no se puede agregar empleados.")

    def registrarHoras(self,dni,cantHoras):
        band=False
        ind=0
        arreglo=self.__arreglo
        while not band and ind<len(arreglo):
            empleado=arreglo[ind]
            if empleado.getDNI()==dni and type(empleado)==EmpleadoContratado:
                empleado.addHorasTrabajadas(cantHoras)
                print("\nLas horas fueron agregadas.")
                print("\nTotal de horas: {}".format(empleado.getHorasTrabajadas))
                band=True
            ind+=1
        if band==False:
            print("\nNo se encontro el empleado.")

    def totalTarea(self,tarea):
        total=0
        for empleado in self.__arreglo:
            if isinstance(empleado,EmpleadoExterno):
                if empleado.getTarea()==tarea and empleado.getFechaFinal()>date.today:
                    total+=empleado.getMonto()
        if total==0:
            print("\nNo hay tareas de ese tipo en curso.")
        else:
            print("\nEl monto total a pagar es de: ${:.2f}".format(total))

    def listarAyuda(self):
        arreglo=self.__arreglo
        ind=0
        while ind < len(arreglo):
            empleado=arreglo[ind]
            if isinstance(empleado,EmpleadoPlanta):
                if empleado.getSueldo()<25000:
                    print("\n--------------------------------------------------")
                    print("{}{}{}{}{}".format("DNI","Nombre","Direccion","Telefono","Sueldo"))
                    print("--------------------------------------------------")
                    print(empleado)
                    print("--------------------------------------------------")

    def listarEmpleados(self):
        arreglo=self.__arreglo
        ind=0
        elemento=arreglo[ind]
        print("\n--------------------------------------------------")
        print("{}{}{}{}{}".format("DNI","Nombre","Direccion","Telefono","Sueldo"))
        print("--------------------------------------------------")
        while elemento is not None:
            print (elemento)
            ind+=1
            elemento=arreglo[ind]
            print("--------------------------------------------------")

    def gastosSueldosPorEmpleado(self,dni):
        empleado=self.getEmpleado(dni)
        if empleado!=None:
            print("-----------DATOS DEL EMPLEADO--------------------")
            print("-----------------------------------------------------------------------------------------------------")
            print(" {:<25} {:<15} {:<25} {:<15} {:<15} ".format("Nombre", "DNI", "Direccion", "Telefono", "sueldo"))
            print("-----------------------------------------------------------------------------------------------------")
            print(empleado)
            print("-----------------------------------------------------------------------------------------------------")
        else:
            print("No encontrado")

    def modificarBasicoEPlanta(self,dni,nuevoBasico):
        empleado=self.getEmpleado(dni)
        if isinstance (empleado,EmpleadoPlanta):
            empleado.setSueldoBasico(nuevoBasico)
            print("Cambio exitoso. ")
        else:
            print("Empleado de planta no encontrado.")

    def modificarViaticoEExterno(self,dni,nuevoViatico):
        empleado=self.getEmpleado(dni)
        if isinstance (empleado,EmpleadoExterno):
            empleado.setMontoV(nuevoViatico)
            print("Cambio exitoso. ")
        else:
            print("Empleado Externono encontrado.")

    def modificarValorEPorHora(self,dni, nuevoValorHora):
        empleado = self.getEmpleado(dni)
        if isinstance(empleado, EmpleadoContratado):
            empleado.setValorH(nuevoValorHora)
            print("Cambio exitoso")
        else:
            print("Empleado Contratado no encontrado")