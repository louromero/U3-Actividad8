import abc
from abc import ABC

class Empleado(ABC):
    __dni=0
    __nombre=''
    __direccion=''
    __telefono=0

    def __init__(self,dni,nombre,direccion,telefono):
        self.__dni=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono

    def getDNI(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    @abc.abstractmethod
    def getSueldo(self):
        pass

    def __str__(self):
        return "{}{}{}{}".format(self.getDNI(),self.getNombre(),self.getDireccion(),self.getTelefono())