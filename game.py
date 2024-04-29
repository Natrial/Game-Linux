from flask import Flask, render_template, request, jsonify
from data import Data
from jugador import Jugador
from pantalla import Pantalla
from errores import Errores

app = Flask(__name__)

class Game():
    def __init__(self, app):
        """constructor"""
        self.turn = 0
        self.ciudades = Data().ciudades
        #ciudad recoge la ciudad donde esta el jugador
        self.ciudad = None
        self.productos = None
        self.eleccion = None
        self.jugador = Jugador()
        self.pantalla = Pantalla()
        self.error = Errores()
        self.app = app

        # Configurar rutas Flask
        self.configure_routes()
    
    def comprar(self):
        try:
            data = request.get_json()

            # Extract data from the JSON payload
            producto = data.get('producto')
            cantidad = int(data.get('cantidad'))
            precio = float(data.get('precio'))

            # Invoke your Python method with the data
            self.jugador.comprar(precio, cantidad, producto)


            # Return the updated data as a JSON response
            response_data = {
                'productos': render_template('productos_partial.html', productos=self.productos),
                'monedas': self.jugador.monedas,
                'inventario': render_template('inventario_partial.html', inventario=self.jugador.productos)
            }

            return jsonify(response_data)

        except Exception as e:
            # Log the exception details
            print('Exception in /comprar:', str(e))
            return jsonify({'error': 'Internal Server Error'}), 500
        
    
    def vender(self):
        try:
            data = request.get_json()

            # Extract data from the JSON payload
            producto = data.get('producto')
            cantidad = int(data.get('cantidad'))
            precio = float(data.get('precio'))

            # Invoke your Python method with the data
            self.jugador.vender(precio, cantidad, producto)

            # Return the updated data as a JSON response
            response_data = {
                'productos': render_template('productos_partial.html', productos=self.productos),
                'monedas': self.jugador.monedas,
                'inventario': render_template('inventario_partial.html', inventario=self.jugador.productos)
            }

            return jsonify(response_data)

        except Exception as e:
            # Log the exception details
            print('Exception in /vender:', str(e))
            return jsonify({'error': 'Internal Server Error'}), 500

    def mostrar_ciudades(self):
        return render_template('prueba_ciudades.html', ciudades=self.ciudades)
    
    def mostrar_instrucciones(self):
        return render_template('index.html')
    
    def mostrar_productos_ciudad(self, ciudad_posicion):
        # Accede a la ciudad usando el índice
        while self.turn <30:
            if self.eleccion != ciudad_posicion:
                self.eleccion = ciudad_posicion

                self.ciudad = self.ciudades[self.eleccion]
                self.productos = self.ciudad.turno()
                self.turn += 1
            
                return render_template('prueba_productos.html', ciudad=self.ciudad.name, productos=self.productos
                                    , turno_actual=self.turn, monedas=self.jugador.monedas, inventario=self.jugador.productos) 
            return render_template('prueba_ciudades.html', ciudades=self.ciudades)
        return render_template('index.html')
    
    def obtener_precio(self):
        producto = request.args.get('producto')
        # Aquí deberías obtener el precio del producto desde la ciudad u otra fuente de datos
        #print(self.productos)
        for i in range(len(self.productos)):
            if self.productos[i]['name'] == producto:
                precio = self.productos[i]['price']  # Debes implementar esta función
        return str(precio)


    def configure_routes(self):
        # Ruta de Flask para mostrar instrucciones
        @self.app.route('/')
        def mostrar_instrucciones_route():
            return self.mostrar_instrucciones()
        
        # Ruta de Flask para mostrar ciudades
        @self.app.route('/ciudades')
        def mostrar_ciudades_route():
            return self.mostrar_ciudades()         
        
        # Ruta de Flask para mostrar los productos de una ciudad
        @self.app.route('/productos/<int:ciudad_posicion>')
        def mostrar_productos_ciudad_route(ciudad_posicion):
            return self.mostrar_productos_ciudad(ciudad_posicion)
        
        # Ruta de Flask para la accion de comprar
        @self.app.route('/comprar', methods=['POST'])
        def comprar_route():
            return self.comprar()
        
        # Ruta de Flask para la accion de vender
        @self.app.route('/vender', methods=['POST'])
        def vender_route():
            return self.vender()
        
        @self.app.route("/obtener_precio")
        def obtener_precio_route():
            return self.obtener_precio()



