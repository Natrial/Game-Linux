class Errores():
    def __init__(self):
        #errores: desde jugador vender -> key error
        #main rangos

        pass

    def ciudad (self, dato):
        while (len(dato)>1 or len(dato)<1) or dato.isdigit() == False or (int(dato)<1 or int(dato)>8):
            dato = input('Numero: ')
        
        return int(dato)-1
    
    def pro_cant(self, producto, cantidad, longitud):
        while (len(producto)>1 or len(producto)<1) or producto.isdigit() == False or (int(producto)<1 or int(producto)>longitud):
            producto = input('Producto: ')
        
        while len(cantidad)<1 or cantidad.isdigit() == False:
            cantidad = input('Cantidad: ')
        
        return int(producto)-1, int(cantidad)
        
        
