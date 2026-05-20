from flask import Flask, render_template
from routes.usuario_routes import usuario_bp
from routes.perro_routes import perro_bp  

app = Flask(__name__)

# Registramos todos los Blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(perro_bp)  

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)