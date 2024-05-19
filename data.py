import json
from exception_management import AccessManagementException
from producto import Producto
from ciudad import City

class Data():
    """prepara los datos para trabajorlos"""
    def __init__(self):
        """constructor"""
        self.productos = self.producto(self.read("./data/productos.json"))
        self.productoName = []
        for i in self.productos:
            self.productoName.append(i.name)
        self.ciudades = self.ciudad(self.read("./data/ciudades.json"))
        self.informe_path = "./data/informe.json"
        
    def read(self, path):
        "Adds the data to the Json"
        try:
            with open(path, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
                return data
        except FileNotFoundError as ex:
            raise AccessManagementException("Wrong file or file path") from ex
        
    def new_game(self):
        """Elimina posible información previa y prepara un nuevo juego"""
        empty_data = []
        try:
            with open(self.informe_path, "w", encoding="utf-8", newline="") as file:
                json.dump(empty_data, file, indent=4)
        except FileNotFoundError as ex:
            raise AccessManagementException("Wrong file or file path") from ex
        return empty_data
    
    def producto (self, dictionary):
        """prepara los productos en una lista de tuplas con el nombre y los rangos de precios"""
        productos = []
        for i in dictionary:
            productos.append(Producto(i,dictionary[i]['up'],dictionary[i]['avg'],dictionary[i]['down']))
        return productos

    def ciudad (self, dictionary):
        """prepara las ciudades en una lista de tuplas con el nombre y los productos que pueden ofrecer"""
        ciudades = []
        for i in dictionary:
            ciudades.append(City(i,self.producto_ciudad(dictionary[i])))
        return(ciudades)
    
    def producto_ciudad (self, lista):
        """devuelve uan lista de los productos que puede ofrecer la ciudad"""
        listaProductos = []

        """añade a listaProductos el objeto Producto especifico"""
        for i in lista:
            listaProductos.append(self.productos[self.productoName.index(i)])
        return listaProductos
    
    def write_informe(self, data):
        """Escribe datos en el archivo informe"""
        with open(self.informe_path, "w", encoding="utf-8", newline="") as file:
            json.dump(data, file, indent=4)
    
    def read_informe(self):
        """Lee el archivo informe"""
        return self.read("./data/informe.json")