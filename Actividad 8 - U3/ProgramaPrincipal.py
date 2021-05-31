from Menu import Menu
from Coleccion import Coleccion
from InterfazGerente import IGerente
from InterfazTesorero import ITesorero

if __name__=='__main__':
    menu=Menu()
    salir=False
    dimension=int(input("\nIngrese dimension del arreglo: "))
    coleccion=Coleccion(dimension)
    while not salir:
        print("\n-------------------MENU------------------")
        print("1. Registrar horas.")
        print("2. Consultar total de tareas.")
        print("3. Ayuda.")
        print("4. Calcular sueldo.")
        print("5. Tesorero.")
        print("6. Cliente.")
        print("0. Salir.")
        print("--------------------------------------------\n")
        opcion=int(input("Ingrese opcion: "))
        if opcion in [1,2,3,4]:
            menu.opcion(opcion,coleccion)
        elif opcion ==5:
            menu.opcion(opcion,ITesorero(coleccion))
        elif opcion==6:
            menu.opcion(opcion,IGerente(coleccion))
        salir=opcion==0