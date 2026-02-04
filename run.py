"""
Punto de entrada principal del servidor Flask.
Registra los Blueprints (controladores) y arranca la aplicación.
"""

from flask import Flask
from flask_cors import CORS

from controllers.producto_controller import producto_blueprint

app = Flask(__name__)

# Habilita CORS para permitir que el frontend acceda a la API del backend
CORS(app)

# Registramos el blueprint
app.register_blueprint(producto_blueprint, url_prefix="/api")

@app.route("/")
def home():
    return "Backend Flask de la Tienda Forestal funcionando correctamente."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

