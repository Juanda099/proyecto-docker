from flask import Blueprint, render_template, request, redirect
from services.database import get_db_connection
from utils.security import hash_password

registro_bp = Blueprint('registro', __name__)

@registro_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        carrera = request.form['carrera']
        contrasena = request.form['contrasena']
        contrasena_hash = hash_password(contrasena)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO estudiantes (nombre, correo, carrera, contrasena)
                VALUES (%s, %s, %s, %s)
            """, (nombre, correo, carrera, contrasena_hash))
            conn.commit()
        except Exception as e:
            print(f"Error al registrar estudiante: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return redirect('/registro')

    return render_template('registro.html')

@registro_bp.route('/listar_estudiantes')
def listar_estudiantes():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, correo, carrera FROM estudiantes")
    estudiantes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('listar_estudiantes.html', estudiantes=estudiantes)

@registro_bp.route('/registro/editar/<int:id>', methods=['GET', 'POST'])
def editar_estudiante(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        carrera = request.form['carrera']

        try:
            cursor.execute("""
                UPDATE estudiantes
                SET nombre = %s, correo = %s, carrera = %s
                WHERE id = %s
            """, (nombre, correo, carrera, id))
            conn.commit()
        except Exception as e:
            print(f"Error al actualizar estudiante: {e}")
            conn.rollback()

        cursor.close()
        conn.close()
        return redirect('/listar_estudiantes')

    cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
    estudiante = cursor.fetchone()

    cursor.close()
    conn.close()
    return render_template('editar_estudiante.html', estudiante=estudiante)

@registro_bp.route('/registro/eliminar/<int:id>', methods=['POST'])
def eliminar_estudiante(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id,))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar estudiante: {e}")
        conn.rollback()

    cursor.close()
    conn.close()
    return redirect('/listar_estudiantes')
