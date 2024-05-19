from data import Data

class Record():
    """registro de las acciones del jugador"""
    def __init__(self):
        """constructor"""
        self.data_instance = Data()
        self.data = self.data_instance.new_game()
        self.productos = []
        self.best = {
            "nombre": '',
            "monedas": 0,
            "precio": 0,
            "cantidad": 0
        }

    def write(self, accion):
        """registra las acciones realizadas"""
        self.mejor(accion)
        
        if accion['nombre'] not in self.productos:
            self.data.append(accion)
            self.productos.append(accion['nombre'])
        else:
            self.data = self.lista(self.data, accion, self.productos.index(accion['nombre']))

        """se sobreescribe la informacion anterior con la actulizada"""
        self.data_instance.write_informe(self.data)

    def lista(self, data, newData, registerToUpdate):
        """actualiza los datos de las acciones del jugador"""
        data[registerToUpdate]['monedas'] += newData['monedas']
        data[registerToUpdate]['cantidad'] += newData['cantidad']

        """se calcula la media del precio venta por unidad"""        
        data[registerToUpdate]['precio'] = (newData['precio'] + data[registerToUpdate]['precio'])/2
        return data
    
    def mejor(self, newData):
        """si el beneficio ha sido mayor se registra como la mejor accion realizada"""
        if newData['monedas']> self.best['monedas']:
            self.best=newData
