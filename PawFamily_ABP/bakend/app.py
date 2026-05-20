from flask import Flask, render_template
from PawFamily_ABP.bakend.routes.usuario_routes import usuario_bp

app = Flask(__name__)

# Registramos el Blueprint de usuarios
app.register_blueprint(usuario_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)