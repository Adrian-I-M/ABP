from flask import Flask, jsonify, redirect, render_template, request, url_for
import pymysql

app = Flask(__name__)

def get_connection():
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="testddbb",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/db")
def db_status():
    try:
        connection = get_connection()
        connection.close()
        return jsonify({
            "ok": True,
            "mensaje": "Conexión correcta con la base de datos"
        })
    except Exception as error:
        return jsonify({
            "ok": False,
            "error": str(error)
        }), 500
        
# SEGMENTO DE CODIGO USUARIOS

@app.route("/usuarios", methods=["POST"])
def create_user():
    # Recogemos y limpiamos espacios fantasmas
    nombre = request.form.get("nombre", "").strip()
    email = request.form.get("email", "").strip()
    
    #  Validación sintáctica básica
    if not nombre or not email:
        return jsonify({"error": "Faltan el nombre o el email"}), 400
        
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        #  Comprobar si el email ya existe
        cursor.execute("SELECT id FROM usuario WHERE email = %s LIMIT 1", (email,))
        existe_usuario = cursor.fetchone()
        
        if existe_usuario:
            cursor.close()
            connection.close()
            return jsonify({"error": "Este correo electrónico ya está registrado"}), 422

        # Si no existe, procedemos al registro
        cursor.execute(
            "INSERT INTO usuario (nombre, email) VALUES (%s, %s)",
            (nombre, email)
        )
        connection.commit()
        new_id = cursor.lastrowid
        
        cursor.close()
        connection.close()
        return redirect(url_for("get_user", user_id=new_id))
        
    except Exception as error:
        if 'connection' in locals() and connection.open:
            connection.close()
        return jsonify({"ok": False, "error": str(error)}), 500
        
# SEGMENTO DE CODIGO PERROS

# SEGMENTO DE CODIGO CITAS

if __name__ == "__main__":
    app.run(debug=True)