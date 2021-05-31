from EmpleadoTiempo import EmpleadoTiempo
from datetime import date

class EmpleadoExterno(EmpleadoTiempo):
    __tarea=""
    __montoViatico=0
    __costoObra=0
    __montoSeguro=0

    def __init__(self,fechaInicio,fechaFinal,tarea,montoViatico,costoObra,montoSeguro,dni,nombre,direccion,telefono):
        self.__tarea=tarea
        self.__montoViatico=montoViatico
        self.__costoObra=costoObra
        self.__montoSeguro=montoSeguro
        super().__init__(fechaInicio,fechaFinal,dni,nombre,direccion,telefono)

    def getTarea(self):
        return self.__tarea

    def getMontoViatico(self):
        return self.__montoViatico

    def getCostoObra(self):
        return self.__costoObra

    def getSueldo(self):
        return self.__costoObra-self.__montoViatico-self.__montoSeguro

    def getMonto(self):
        return self.__costoObra+self.__montoViatico+self.__montoSeguro

    def getFechaFinal(self):
        return super().getFechaFinal()

    def getFechaInicio(self):
        return super().getFechaInicio()

    def setMontoV(self,nuevo):
        self.__montoViatico=nuevo

    def __str__(self):
        sueldo="{:.2f}".format(self.getSueldo)
        cadena=super().__str__
        cadena+="${:.2f}".format(sueldo)
        return cadena