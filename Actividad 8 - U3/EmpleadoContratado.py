from datetime import date
from EmpleadoTiempo import EmpleadoTiempo

class EmpleadoContratado(EmpleadoTiempo):
    valorHora=260
    __horasTrabajadas=0

    def __init__(self,fechaInicio,FechaFinal,horasTrabajadas,dni,nombre,direccion,telefono):
        super().__init__(fechaInicio,FechaFinal,dni,nombre,direccion,telefono)
        self.__horasTrabajadas=horasTrabajadas

    def getHorasTrabajadas(self):
        return self.__horasTrabajadas

    def getSueldo(self):
        return self.__horasTrabajadas*self.getValorHora()

    @classmethod
    def getValorHora(cls):
        return cls.valorHora

    @classmethod
    def setValorH(cls,nuevoValor):
        cls.valorHora=nuevoValor

    def addHoras(self,hora):
        self.__horasTrabajadas+=hora

    def __str__(self):
        sueldo="{:.2f}".format(self.getSueldo)
        cadena=super().__str__
        cadena+="${:.2f}".format(sueldo)
        return cadena