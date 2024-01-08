import json
from exception_management import AccessManagementException


class Record():
    def __init__(self):
        self.myFile ='./data/informe.json'
        self.new_game()
        self.productos = []
        self.best = {
        "nombre": '',
        "monedas": 0,
        "precio": 0,
        "cantidad": 0
    }

    def new_game(self):
        try:
            with open(self.myFile, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException("Wrong file or file path") from ex

        data=[]
        with open(self.myFile, "w", encoding="utf-8", newline = "") as file:
            json.dump(data, file, indent=4)
        return None

    def write(self, accion):
        self.mejor(accion)
        try:
            with open(self.myFile, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException("Wrong file or file path") from ex
        
        "Si el diccionario no está en el json añadirlo"        
        if accion['nombre'] not in self.productos:
            data.append(accion)
            self.productos.append(accion['nombre'])
            with open(self.myFile, "w", encoding="utf-8", newline = "") as file:
                json.dump(data, file, indent=4)
                return None
        else:self.lista(data, accion, self.productos.index(accion['nombre']))
        return None

    def lista(self, lista, newData, indice):
        #{'monedas':precioV*cantidad,'precio':precioV,'cantidad':cantidad}
        lista[indice]['monedas'] += newData['monedas']
        lista[indice]['cantidad'] += newData['cantidad']
        lista[indice]['precio'] = (newData['precio'] + lista[indice]['precio'])/lista[indice]['cantidad']

        with open(self.myFile, "w", encoding="utf-8", newline = "") as file:
            json.dump(lista, file, indent=4)
        return None
    
    def mejor (self, newData):
        if newData['monedas']> self.best['monedas']:
            self.best=newData
        return None
