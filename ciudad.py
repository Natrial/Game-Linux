import random
class City():
    def __init__(self,name, productos):
        self.name = name
        self.productos = []
        for i in productos:
            self.productos.append(i)
    
    def turno(self):
        num = random.randint(3,5)
        turn = []
        names = []
        while len(turn)<num:
            rand = random.randint(0,4)
            price = self.productos[rand].price(random.randint(0,3))
            dictionary = {'name':self.productos[rand].name, 'price': price[0], 
            'range':price[1]}
            if dictionary['name'] not in names:
                turn.append(dictionary)
                names.append(dictionary['name'])
        return turn

