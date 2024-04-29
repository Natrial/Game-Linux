import random
class City():
    def __init__(self,name, productos):
        """constructor de ciudad"""
        self.name = name
        self.productos = []
        for i in productos:
            self.productos.append(i)
    
    def turno(self):
        #numProducts es el numero de productos que se van a mostrar, productsPerTurn es la lista de productos y 
        #names la lista de lo nombres de los productos que ya han sido seleccionados para mostrarse
        numProducts = random.randint(3,5)
        productsPerTurn = []
        names = []
        """se añade el numero de productos a vender"""
        while len(productsPerTurn)<numProducts:
        #rand es el producto aleatorio que se escoge para mostrar
            rand = random.randint(0,4)
            """se escoge el si el producto va a estar en rango de oferta, en demanda, o normal"""
            price = self.productos[rand].price(random.randint(0,3))
            #se crea un diccionario con el nombre del producto, el precio y si el rango es 'UP', 'DOWN' o ''
            dictionary = {'name':self.productos[rand].name, 'price': price[0], 
            'range':price[1]}
            """si el producto no esta añadido ya, se añade el diccionario y su nombre a la lista de productos"""
            if dictionary['name'] not in names:
                productsPerTurn.append(dictionary)
                names.append(dictionary['name'])
        return productsPerTurn

