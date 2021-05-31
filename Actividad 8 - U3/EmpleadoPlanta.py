from Empleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldoBasico=0
    __antiguedad=0

    def __init__(self,sueldoBasico,antiguedad,dni,nombre,direccion,telefono):
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad
        super().__init__(dni,nombre,direccion,telefono)

    def getSueldo(self):
        sueldoBasico=self.__sueldoBasico
        return sueldoBasico + ((sueldoBasico*0.01)*self.__antiguedad)

    def setSueldoBasico(self,nuevo):
        self.__sueldoBasico=nuevo

    def __str__(self):
        sueldo="{:.2f}".format(self.getSueldo)
        cadena=super().__str__
        cadena+="${:.2f}".format(sueldo)
        return cadena