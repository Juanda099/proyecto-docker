from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

@app.route('/')
def hello():
    e = None  # Inicializa la variable
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host='db',
                user='root',
                password='password',
                database='test_db'
            )
            return "✅ Conexión a la base de datos exitosa."
        except Exception as ex:
            e = ex
            time.sleep(5)  # Espera 5 segundos antes de reintentar
    return f"❌ Error de conexión: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
