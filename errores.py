class Errores():
    def __init__(self):
        """no tiene constructor"""
        pass

    def ciudad (self, dato: str):
        """se comprueba que la ciudad seleccionada es correcta"""

        """el dato solo puede ser de un digito y debe ser un numero entre 1 y 8"""
        while len(dato)!=1 or dato.isdigit() == False or (int(dato)<1 or int(dato)>8):
            dato = input('Numero: ')
        
        """se devuleve el indice de un a lista"""
        return int(dato)-1
    
    def pro_cant(self, producto, cantidad, longitud):
        """se comprueba que el producto seleccionado y la cantidad con correctos"""

        """el producto seleccionado solo puede ser de un digito y debe ser un numero entre 1
         y la longitud de la lista de productos ofrecidos"""
        while len(producto)!=1 or producto.isdigit() == False or (int(producto)<1 or int(producto)>longitud):
            producto = input('Producto: ')
        
        """la cantidad debe ser un numero positivo"""
        while len(cantidad)<1 or cantidad.isdigit() == False:
            cantidad = input('Cantidad: ')
        
        """el producto es el indice de una lista"""
        return int(producto)-1, int(cantidad)
    
    def error_venta(self, cantidad, nombre):
        """validar que la cantidad a vender existe en el inventario del jugador"""
        while cantidad > nombre:
            cantidad = int(input('Introduzca cantidad valida: '))
        return cantidad
    
    def error_compra(self, nPrecio, nCantidad, monedas):
        """validar que se compra sin gastar mas de lo que esl jugador tiene"""
        while nPrecio * nCantidad > monedas or nCantidad == 0:
            nCantidad = int(input('Introduzca cantidad valida: '))
        return nCantidad
        
        
