from flask import Flask, render_template, send_from_directory
from routes.usuario_routes import usuario_bp
from routes.perro_routes import perro_bp  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitamos CORS para permitir peticiones desde el frontend
app.json.ensure_ascii = False  #Para que el JSON muestre caracteres especiales directamente (á, ñ, ç)

CARPETA_UPLOADS = r"C:\Users\Alex\Desktop\Imagen"

app.config['UPLOAD_FOLDER'] = CARPETA_UPLOADS

#Para que el frontend pueda ver las imágenes
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Registramos todos los Blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(perro_bp)  

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)