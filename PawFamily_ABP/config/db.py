import pymysql

def get_connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="paw_family",

            cursorclass=pymysql.cursors.DictCursor 
        )

        return connection
        
    except pymysql.MySQLError as err:
        print(f"Error conectando a la DB: {err}")
        return None