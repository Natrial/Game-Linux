from flask import Flask
from game import Game

app = Flask(__name__)

# Crear una instancia de Game
game_instance = Game(app)

if __name__ == '__main__':
    app.run(debug=True)
