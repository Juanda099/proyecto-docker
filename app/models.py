import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def create_tables():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'test_db')
    )
    cursor = conn.cursor()

    # Tabla de estudiantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(100) UNIQUE NOT NULL,
            carrera VARCHAR(100) NOT NULL,
            contrasena VARCHAR(255) NOT NULL
        );
    ''')

    # Tabla de materias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            codigo VARCHAR(20) UNIQUE NOT NULL,
            nombre VARCHAR(100) NOT NULL,
            semestre INT NOT NULL
        );
    ''')

    # Tabla de inscripciones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inscripciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            estudiante_id INT,
            materia_id INT,
            FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY(materia_id) REFERENCES materias(id)
        );
    ''')

    # Tabla de horarios (corregida)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS horarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            estudiante_id INT,
            materia_id INT,
            dia VARCHAR(20) NOT NULL,
            hora_inicio TIME NOT NULL,
            hora_fin TIME NOT NULL,
            FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY(materia_id) REFERENCES materias(id)
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()