from flask import Blueprint, render_template, request, redirect, flash
from services.database import get_db_connection  # ✅ Import correcto

materias_bp = Blueprint('materias', __name__)

@materias_bp.route('/materias', methods=['GET', 'POST'])
def registrar_materias():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        semestre = request.form['semestre']

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Verifica si el código ya existe
            cursor.execute("SELECT COUNT(*) FROM materias WHERE codigo = %s", (codigo,))
            existe = cursor.fetchone()[0]

            if existe > 0:
                flash(f"⚠️ El código '{codigo}' ya está registrado. Usa otro código.", "error")
                return render_template('materias.html')  # Recarga el formulario con el mensaje

            # Si no existe, insertar normalmente
            cursor.execute("""
                INSERT INTO materias (codigo, nombre, semestre)
                VALUES (%s, %s, %s)
            """, (codigo, nombre, semestre))
            conn.commit()
            flash("✅ Materia registrada correctamente.", "success")

        except Exception as e:
            print(f"Error al registrar materia: {e}")
            conn.rollback()
            flash("❌ Error al registrar la materia.", "error")

        finally:
            cursor.close()
            conn.close()

        return redirect('/materias')

    return render_template('materias.html')


@materias_bp.route('/materias/listar', methods=['GET'])
def listar_materias():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Para obtener los resultados como diccionarios

    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('listar_materias.html', materias=materias)


@materias_bp.route('/materias/editar/<int:id>', methods=['GET', 'POST'])
def editar_materia(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        codigo = request.form['codigo']
        semestre = request.form['semestre']

        try:
            cursor.execute("""
                UPDATE materias SET nombre=%s, codigo=%s, semestre=%s WHERE id=%s
            """, (nombre, codigo, semestre, id))
            conn.commit()
            flash("✅ Materia actualizada correctamente.", "success")
        except Exception as e:
            print(f"Error al actualizar materia: {e}")
            conn.rollback()
            flash("❌ Error al actualizar la materia.", "error")
        finally:
            cursor.close()
            conn.close()
        
        return redirect('/materias/listar')

    # Si es GET, cargar la materia
    cursor.execute("SELECT * FROM materias WHERE id = %s", (id,))
    materia = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('editar_materia.html', materia=materia)

@materias_bp.route('/materias/eliminar/<int:id>', methods=['POST'])
def eliminar_materia(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM materias WHERE id = %s", (id,))
        conn.commit()
        flash("🗑️ Materia eliminada correctamente.", "success")
    except Exception as e:
        print(f"Error al eliminar materia: {e}")
        conn.rollback()
        flash("❌ Error al eliminar la materia.", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect('/materias/listar')
