from record import Record

class Jugador():
    """clase que maneja las acciones del jugador"""
    def __init__(self):
        """constructor con los datos iniciales"""
        #productos q se ofertan
        self.productos = {}
        self.monedas = 2000
        """inicia el registro de acciones"""
        self.record = Record()
    
    
    def comprar(self, nPrecio, nCantidad, nombre):
        """funcion de comprar"""
        self.monedas -= (nPrecio * nCantidad)

        if nombre in self.productos.keys():
            name = self.productos[nombre]
            name['precio'] = round((name['precio']*name['cantidad'] + nPrecio*nCantidad)/(nCantidad+name['cantidad']))
            name['cantidad'] += nCantidad

        else:
            self.productos[nombre]={}
            self.productos[nombre]['precio'] = nPrecio
            self.productos[nombre]['cantidad']= nCantidad


    def vender(self, precioV, cantidad, nombre):
        """funcion vender"""
        self.record.write({'nombre':nombre,'monedas':(precioV-self.productos[nombre]['precio'])*cantidad,
                           'precio':precioV-self.productos[nombre]['precio'],'cantidad':cantidad})
        
        self.monedas += precioV*cantidad
        self.productos[nombre]['cantidad'] -= cantidad

        if self.productos[nombre]['cantidad'] == 0:
            self.productos.pop(nombre)

    def mejor_accion(self):
        return self.record.best


      