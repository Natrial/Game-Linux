import json
from exception_management import AccessManagementException
from producto import Producto
from ciudad import City

class Read():
    def __init__(self):
        self.productos = self.producto(self.read("./data/productos.json"))
        self.productoName = []
        for i in self.productos:
            self.productoName.append(i.name)
        self.ciudades = self.ciudad(self.read("./data/ciudades.json"))
        self.informe = self.read("./data/informe.json")
        
    def read(self, path):
        "Adds the data to the Json"
        try:
            with open(path, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
                return data
        except FileNotFoundError as ex:
            raise AccessManagementException("Wrong file or file path") from ex
    
    def producto (self, dictionary):
        productos = []
        for i in dictionary:
            productos.append(Producto(i,dictionary[i]['up'],dictionary[i]['avg'],dictionary[i]['down']))
        return productos

    def ciudad (self, dictionary):
        ciudades = []
        for i in dictionary:
            ciudades.append(City(i,self.pro_ciy(dictionary[i])))
        return(ciudades)
    
    def pro_ciy (self, lista):
        listaProductos = []
        for i in lista:
            listaProductos.append(self.productos[self.productoName.index(i)])
        return listaProductos

        
