import random
class Producto():
    def __init__(self, name, up, avg, down):
        self.name=name
        self.up=up
        self.avg=avg
        self.down=down

    def get_price (self, rango):
        return random.randint(rango[0], rango[1])

    def price(self, tipo):
        if tipo == 0:
            return (self.get_price(self.up), ' UP')
        elif tipo == 3:
            return (self.get_price(self.down), ' DOWN')
        return (self.get_price(self.avg), None)
    

    
