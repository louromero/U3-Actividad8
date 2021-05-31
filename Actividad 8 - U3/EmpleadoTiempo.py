from Empleado import Empleado
from datetime import date

class EmpleadoTiempo(Empleado):
    __fechaInicio=None
    __fechaFinal=None

    def __init__ (self,fechaInicio,fechaFinal,dni,nombre,direccion,telefono):
        self.setFecha(fechaInicio,fechaFinal)
        super().__init__(dni,nombre,direccion,telefono)

    def setFecha(self,fechaInicio,fechaFinal):
        fechaInicio=fechaInicio.split("-")
        fechaFinal=fechaFinal.split("-")

        self.__fechaInicio=date(int(fechaInicio[0]),int(fechaInicio[1]),int(fechaInicio[2]))
        self.__fechaFinal=date(int(fechaFinal[0]),int(fechaFinal[1]),int(fechaFinal[2]))


    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFinal(self):
        return self.__fechaFinal