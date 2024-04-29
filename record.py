import json
from exception_management import AccessManagementException


class Record():
    """registro de las acciones del jugador"""
    def __init__(self):
        """constructor"""
        self.myFile ='./data/informe.json'
        self.data = self.new_game()
        self.productos = []
        self.best = {
            "nombre": '',
            "monedas": 0,
            "precio": 0,
            "cantidad": 0
        }

    def new_game(self):
        """elimina posible informacion previa"""

        """se asegura de que el json exista"""
        try:
            with open(self.myFile, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException("Wrong file or file path") from ex

        """crea una lista vacia para sobreescribir la información anterior"""
        data=[]
        with open(self.myFile, "w", encoding="utf-8", newline = "") as file:
            json.dump(data, file, indent=4)
        return data

    def write(self, accion):
        """registra las acciones realizadas"""

        """se comprueba si es la mejor accion realizada hasta el momento"""
        self.mejor(accion)
        
        """Si el producto no tiene registro previo no está en el json, añadirlo"""    
        if accion['nombre'] not in self.productos:
            self.data.append(accion)
            self.productos.append(accion['nombre'])
        else:
            """si y ahay un registro previo con este producto se invova la funcion lista"""
            self.data = self.lista(self.data, accion, self.productos.index(accion['nombre']))

        """se sobreescribe la informacion anterior con la actulizada"""
        with open(self.myFile, "w", encoding="utf-8", newline = "") as file:
            json.dump(self.data, file, indent=4)
            return None

    def lista(self, lista, newData, indice):
        """actualiza los datos de las acciones del jugador"""
        #lista son los datos ya recogidos
        #newData es la nueva accion realizada
        #indice es el indice de la posicion donde esta el registro a actualizar

        """se suman la nueva cantidad de monedas conseguidas y cantidad de procustos vendidos"""
        lista[indice]['monedas'] += newData['monedas']
        lista[indice]['cantidad'] += newData['cantidad']

        #precio es el beneficio por producto unitario
        """se calcula la media del precio venta por unidad"""        
        lista[indice]['precio'] = (newData['precio'] + lista[indice]['precio'])/2
        return lista
    
    def mejor (self, newData):
        """si el beneficio ha sido mayor se registra como la mejor accion realizada"""
        if newData['monedas']> self.best['monedas']:
            self.best=newData
        return None
