from flask import Flask, render_template
from routes.usuario_routes import usuario_bp
from flask_cors import CORS  # Importamos CORS para habilitarlo en la app
from routes.perro_routes import perro_bp  

app = Flask(__name__)
CORS(app)  # Habilitamos CORS para permitir peticiones desde el frontend
app.json.ensure_ascii = False  #Para que el JSON muestre caracteres especiales directamente (á, ñ, ç)

# Registramos todos los Blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(perro_bp)  

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)