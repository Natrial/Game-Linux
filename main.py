from producto import Producto
from ciudad import City
from read import Read
from jugador import Jugador
from pantalla import Pantalla
from errores import Errores
import random
import os


class Main():
    def __init__(self):
        self.turn = 0
        self.posicion = None
        self.ciudades = Read().ciudades
        self.ciudad= None
        self.eleccion = None
        self.jugador = Jugador()
        self.pantalla = Pantalla()
        self.error = Errores()
    
    def play (self):
        print(self.pantalla.__str__(0, None))
        eleccion = input('')
        while eleccion != '':
            print(self.pantalla.__str__(0, None))
            eleccion = input('')
        while self.turn < 30:
            print(self.pantalla.__str__(1, [self.ciudades, self.turn]))
            eleccion = self.error.ciudad(input('Numero: '))
            if eleccion != self.eleccion:
                self.eleccion = eleccion
                self.ciudad=self.ciudades[self.eleccion].turno()
                self.turn += 1
                choice = None
                while choice != 'pass':
                    if choice == 'v':
                        entrada=self.error.pro_cant(input('Producto: '),input('Cantidad: '),len(self.ciudad))
                        self.jugador.vender(self.ciudad[entrada[0]]['price'], entrada[1], self.ciudad[entrada[0]]['name'])
                    elif choice == 'c':
                        entrada=self.error.pro_cant(input('Producto: '),input('Cantidad: '),len(self.ciudad))
                        self.jugador.comprar(self.ciudad[entrada[0]]['price'], entrada[1], self.ciudad[entrada[0]]['name'])
                    print(self.pantalla.__str__(3,[str(self.ciudades[self.eleccion].name),self.jugador.inventario(),self.ciudad,self.turn]))
                    choice = input('¿Comprar [c]/ Vender [v]?: ').lower()
        

        self.jugador.final()
        print(self.pantalla.__str__(2,Read().informe))


        return self.jugador.monedas




print(Main().play())
