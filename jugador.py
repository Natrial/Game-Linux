from record import Record
from errores import Errores

class Jugador():
    """clase que maneja las acciones del jugador"""
    def __init__(self):
        """constructor con los datos iniciales"""
        #productos q se ofertan
        self.productos = {}
        self.monedas = 2000
        """inicia el registro de acciones"""
        self.record = Record()
        self.errores = Errores()
        self.best = None
    
    
    def comprar(self, nPrecio, nCantidad, nombre):
        """funcion de comprar"""

        """actualizar la cantidad de monedas"""
        self.monedas -= (nPrecio * nCantidad)

        """si el producto ya esta en el inventario del jugador se actualiza el precio a la media entre 
        el precio unitario anterior por el precio unitario nuevo. Teniendo en cuenta los volumenes de compra
        y se actualiza la cantidad"""
        if nombre in self.productos.keys():
            name = self.productos[nombre]
            name['precio'] = round((name['precio']*name['cantidad'] + nPrecio*nCantidad)/(nCantidad+name['cantidad']))
            name['cantidad'] += nCantidad

            """si el producto no es esta en el inventario se añade un nuevo diccionario"""
        else:
            self.productos[nombre]={}
            self.productos[nombre]['precio'] = nPrecio
            self.productos[nombre]['cantidad']= nCantidad
        return None

    

    def vender(self, precioV, cantidad, nombre):
        """funcion vender"""

        """si el nombre del pructo a vender no esta en el inventario no se hace nada"""
        if nombre not in self.productos.keys():
            return None
        
        """control de errores en cantidad"""
        cantidad = self.errores.error_venta(cantidad, self.productos[nombre]['cantidad'])

        """se recopila la información de la venta"""
        self.record.write({'nombre':nombre,'monedas':(precioV-self.productos[nombre]['precio'])*cantidad,
                           'precio':precioV-self.productos[nombre]['precio'],'cantidad':cantidad})
        
        """se actualiza la cantidad de monedas y la cantidad restante de ese producto"""
        self.monedas += precioV*cantidad
        self.productos[nombre]['cantidad'] -= cantidad

        """si no quedan unidades de ese producto se elimina de la lista"""
        if self.productos[nombre]['cantidad'] == 0:
            self.productos.pop(nombre)

        return None


    def inventario (self):
        """preparacion de los datos del inventario"""
        cosas = ['Inventario\t' + str(self.monedas)+'¢']
        for i in self.productos.keys():
            linea ='['+ i+']' + ' Precio compra:' +str(self.productos[i]['precio']) + '¢ Cantidad:'+str(self.productos[i]['cantidad'])
            cosas.append(linea)
        return cosas 
    
    
    def final (self):
        """finalizacion de la partida"""

        """se establece la mejor accion"""
        self.best = self.record.best
        print('Tu mejor venta ha sido la venta de: ',self.best['nombre'], ' por ', self.best['monedas'], '¢')

        """preparación de los datos del registro"""
        key = []
        for i in self.productos.keys():
            key.append(i)
        for i in key:
            self.vender(self.productos[i]['precio'],self.productos[i]['cantidad'],i)
        return None
      