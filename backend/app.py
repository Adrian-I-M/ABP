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

@app.route("/usuarios")
def list_users():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuario ORDER BY id")
        usuarios = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(usuarios)
    except Exception as error:
        return jsonify({
            "ok": False,
            "error": str(error)
        }), 500

@app.route("/usuarios/<int:user_id>")
def get_user(user_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM usuario WHERE id = %s",
            (user_id,)
        )
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        if usuario is None:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404
        return jsonify(usuario)
    except Exception as error:
        return jsonify({
            "ok": False,
            "error": str(error)
        }), 500

@app.route("/usuarios", methods=["POST"])
def create_user():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    if not nombre or not email:
        return jsonify({
            "error": "Faltan nombre o email"
        }), 400
    try:
        connection = get_connection()
        cursor = connection.cursor()
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
        return jsonify({
            "ok": False,
            "error": str(error)
        }), 500
        
# SEGMENTO DE CODIGO PERROS

# SEGMENTO DE CODIGO CITAS

if __name__ == "__main__":
    app.run(debug=True)