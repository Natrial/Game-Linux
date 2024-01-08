from record import Record

class Jugador():
    def __init__(self):
        self.productos = {}
        self.monedas = 2000
        self.record = Record()
        self.best = None
        self.nombres = []
    
    def comprar(self, nPrecio, nCantidad, nombre):
        self.nombres.append(nombre)
        while nPrecio * nCantidad > self.monedas or nCantidad ==0:
            nCantidad = int(input('Introduzca cantidad valida: '))
        self.monedas -= (nPrecio * nCantidad)
        if nombre in self.productos.keys():
            name = self.productos[nombre]
            name['precio'] = round((name['precio']*name['cantidad'] + nPrecio*nCantidad)/(nCantidad+name['cantidad']))
            name['cantidad'] += nCantidad
        else:
            self.productos[nombre]={}
            self.productos[nombre]['precio'] = nPrecio
            self.productos[nombre]['cantidad']= nCantidad
        return None

    def vender(self, precioV, cantidad, nombre):
        if nombre not in self.nombres:
            return None
        while cantidad > self.productos[nombre]['cantidad']:
            cantidad = int(input('Introduzca cantidad valida: '))

        self.record.write({'nombre':nombre,'monedas':(precioV-self.productos[nombre]['precio'])*cantidad,'precio':precioV-self.productos[nombre]['precio'],'cantidad':cantidad})
        
        self.monedas += precioV*cantidad
        self.productos[nombre]['cantidad'] -= cantidad
        if self.productos[nombre]['cantidad'] == 0:
            self.productos.pop(nombre)

        return None

    def inventario (self):
        cosas = ['Inventario\t' + str(self.monedas)+'¢']
        for i in self.productos.keys():
            linea ='['+ i+']' + ' Precio compra:' +str(self.productos[i]['precio']) + '¢ Cantidad:'+str(self.productos[i]['cantidad'])
            cosas.append(linea)
        return cosas 
    
    def final (self):
        self.best = self.record.best
        print('Tu mejor venta ha sido la venta de: ',self.best['nombre'], ' por ', self.best['monedas'], '¢')
        key = []
        for i in self.productos.keys():
            key.append(i)
        for i in key:
            self.vender(self.productos[i]['precio'],self.productos[i]['cantidad'],i)
        return None



        