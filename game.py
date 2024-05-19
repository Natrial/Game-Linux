from flask import Flask, render_template, request, jsonify, redirect, url_for
from data import Data
from jugador import Jugador

app = Flask(__name__)

class Game():
    def __init__(self, app):
        """constructor"""
        self.turn = 0
        self.dataConexion = Data()
        self.ciudades = self.dataConexion.ciudades
        self.ciudad = None
        self.productos = None
        self.eleccion = None
        self.jugador = Jugador()
        self.app = app

        # Configurar rutas Flask
        self.configure_routes()
    
    def comprar(self):
        try:
            data = request.get_json()
            producto = data.get('producto')
            cantidad = int(data.get('cantidad'))
            precio = float(data.get('precio'))
            self.jugador.comprar(precio, cantidad, producto)

            response_data = {
                'productos': render_template('productos_partial.html', productos=self.productos),
                'monedas': self.jugador.monedas,
                'inventario': render_template('inventario_partial.html', inventario=self.jugador.productos)
            }

            return jsonify(response_data)

        except Exception as e:
            print('Exception in /comprar:', str(e))
            return jsonify({'error': 'Internal Server Error'}), 500
        
    
    def vender(self):
        try:
            data = request.get_json()
            producto = data.get('producto')
            cantidad = int(data.get('cantidad'))
            precio = float(data.get('precio'))
            self.jugador.vender(precio, cantidad, producto)

            response_data = {
                'productos': render_template('productos_partial.html', productos=self.productos),
                'monedas': self.jugador.monedas,
                'inventario': render_template('inventario_partial.html', inventario=self.jugador.productos)
            }

            return jsonify(response_data)

        except Exception as e:
            print('Exception in /vender:', str(e))
            return jsonify({'error': 'Internal Server Error'}), 500

    def mostrar_ciudades(self):
        return render_template('ciudades.html', ciudades=self.ciudades)
    
    def mostrar_instrucciones(self):
        return render_template('index.html')
    
    def mostrar_productos_ciudad(self, ciudad_posicion):
        # Accede a la ciudad usando el índice
        while self.turn <5:
            if self.eleccion != ciudad_posicion:
                self.eleccion = ciudad_posicion

                self.ciudad = self.ciudades[self.eleccion]
                self.productos = self.ciudad.turno()
                self.turn += 1
            
                return render_template('productos.html', ciudad=self.ciudad.name, productos=self.productos
                                    , turno_actual=self.turn, monedas=self.jugador.monedas, inventario=self.jugador.productos) 
            return render_template('ciudades.html', ciudades=self.ciudades)
        self.turn = 0
        return redirect(url_for('report'))
    
    def obtener_precio(self):
        producto = request.args.get('producto')

        if self.productos:
            for item in self.productos:
                if item['name'] == producto:
                    return str(item['price'])
        return '0'
    
    def report(self):
        informe = self.dataConexion.read_informe()
        return render_template('report.html', informe=informe)

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

        @self.app.route("/report")
        def report():
            return self.report()


