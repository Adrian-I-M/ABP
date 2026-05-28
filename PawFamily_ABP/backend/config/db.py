import os
import pymysql
from dotenv import load_dotenv

# Esto carga las variables del archivo .env en la memoria de Python
load_dotenv()

def get_connection():
    try:
        connection = pymysql.connect(
            # Aquí llamamos a lo que escribisteis en el .env
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)), # El puerto debe ser un número entero
            cursorclass=pymysql.cursors.DictCursor 
        )
        return connection
        
    except pymysql.MySQLError as err:
        print(f"Error conectando a la DB: {err}")
        return None