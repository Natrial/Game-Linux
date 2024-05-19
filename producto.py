import random

class Producto():
    def __init__(self, name, up, avg, down):
        """construstor de producto"""
        self.name=name
        self.up=up
        self.avg=avg
        self.down=down

    def get_price (self, rango):
        """devuelve el numero random dentro del rango establecido"""
        return random.randint(rango[0], rango[1])

    def price(self, tipo:int):
        """devuelve si el producto está en oferta (down), demanda (up) o si esta a precio normal (None)"""
        if tipo == 0:
            return (self.get_price(self.up), ' UP')
        elif tipo == 3:
            return (self.get_price(self.down), ' DOWN')
        return (self.get_price(self.avg), None)
    

    
