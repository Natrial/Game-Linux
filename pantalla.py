import os
from ciudad import City
from jugador import Jugador

class Pantalla():
    def __init__(self):
        self.impresion = ''

    def __str__(self, opcion = 0, datos = None):
        self.impresion = ''
        if opcion == 0:
            self.impresion=self.menu()
        elif opcion == 1:
            self.impresion= self.ciudades(datos[0],datos[1])
        elif opcion == 2:
            self.impresion=self.informe(datos)
        else:
            self.impresion= self.compre_venta(datos[0],datos[1], datos[2], datos[3])
        return self.impresion

    def menu(self):
        os.system('clear')
        menu = 'Presiona Enter para continuar.\n\n'
        menu += 'Para seleccionar una ciudad elija el número que se indique a su izquierda y presione Enter. Tenga en cuenta que no se podra elegir la misma ciudad dos veces seguidas.\n\n'
        menu += 'Para comprar cualquier producto introduzca "c" y luego elija el número del producto y la cantidad a comprar.\n\n'
        menu += 'Para vender cualquier producto introduzca "v", elija el número del producto que se oferta en la ciudad e indique la cantidad a vender.\n\n'
        menu += 'Para salir de la ciudad escriba "pass".'
        return menu
        
        

    def ciudades(self, datos, turno):
        string = 'TURNO ' + str(turno)
        contador =  1
        for i in datos:
            string += '\n' +'['+str(contador)+']'+ str(i.name)
            contador += 1
        os.system('clear')
        return string
    
    def compre_venta(self, ciudadNombre, jugadorInv, dataCiudad, turno):
        os.system('clear')
        contador = 1
        ciudadNombre = 'TURNO ' + str(turno)

        while len(ciudadNombre) < 39:
                ciudadNombre += ' '
        ciudadNombre += jugadorInv[0]
        line = ''
        for i in dataCiudad:
            line += '\n' +'['+str(contador)+']'+ i['name'] + ' ' + str(i['price'])+'¢'
            if i['range'] != None:
                line += str(i['range'])
            while len(line) < 40:
                line += ' '
            if contador < len(jugadorInv):
                line += jugadorInv[contador]
            contador +=1
            ciudadNombre += line
            line = ''
        line = ''
        while contador < len(jugadorInv):
            while len(line) < 39:
                line += ' '
            line += jugadorInv[contador]
            contador +=1
            ciudadNombre += '\n' + line
            line = ''
        return ciudadNombre
    
    def informe(self, data):
        informe = ''
        for i in data:
            informe += 'De la venta de '+ i['nombre'] + ' se han obtenido ' + str(i['monedas']) + ' por el precio medio ' + str(round(i['precio']))+ ' y se han vendido ' + str(i['cantidad']) + ' en total.\n'
        return informe
