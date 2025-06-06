from flask import Blueprint, render_template, request, redirect
from services.database import get_db_connection

horarios_bp = Blueprint('horarios', __name__)

@horarios_bp.route('/horarios', methods=['GET', 'POST'])
def registrar_horarios():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obtener estudiantes y materias para mostrar en el formulario
    cursor.execute("SELECT id, nombre FROM estudiantes")
    estudiantes = cursor.fetchall()

    cursor.execute("SELECT id, nombre FROM materias")
    materias = cursor.fetchall()

    if request.method == 'POST':
        estudiante_id = request.form['estudiante_id']
        materia_id = request.form['materia_id']
        dia = request.form['dia']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']

        try:
            cursor.execute("""
                INSERT INTO horarios (estudiante_id, materia_id, dia, hora_inicio, hora_fin)
                VALUES (%s, %s, %s, %s, %s)
            """, (estudiante_id, materia_id, dia, hora_inicio, hora_fin))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar horario: {e}")
            conn.rollback()

        cursor.close()
        conn.close()
        return redirect('/horarios')

    cursor.close()
    conn.close()
    return render_template('horarios.html', estudiantes=estudiantes, materias=materias)

@horarios_bp.route('/listar_horarios')
def listar_horarios():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT h.id, e.nombre AS estudiante, m.nombre AS materia, h.dia, h.hora_inicio, h.hora_fin
        FROM horarios h
        JOIN estudiantes e ON h.estudiante_id = e.id
        JOIN materias m ON h.materia_id = m.id
    """)
    horarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('listar_horarios.html', horarios=horarios)

@horarios_bp.route('/horarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_horario(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obtener lista para los selects
    cursor.execute("SELECT id, nombre FROM estudiantes")
    estudiantes = cursor.fetchall()
    cursor.execute("SELECT id, nombre FROM materias")
    materias = cursor.fetchall()

    if request.method == 'POST':
        estudiante_id = request.form['estudiante_id']
        materia_id = request.form['materia_id']
        dia = request.form['dia']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']

        try:
            cursor.execute("""
                UPDATE horarios
                SET estudiante_id = %s, materia_id = %s, dia = %s, hora_inicio = %s, hora_fin = %s
                WHERE id = %s
            """, (estudiante_id, materia_id, dia, hora_inicio, hora_fin, id))
            conn.commit()
        except Exception as e:
            print(f"Error al actualizar horario: {e}")
            conn.rollback()

        cursor.close()
        conn.close()
        return redirect('/listar_horarios')

    # Obtener datos actuales del horario
    cursor.execute("SELECT * FROM horarios WHERE id = %s", (id,))
    horario = cursor.fetchone()

    cursor.close()
    conn.close()
    return render_template('editar_horario.html', horario=horario, estudiantes=estudiantes, materias=materias)

@horarios_bp.route('/horarios/eliminar/<int:id>', methods=['POST'])
def eliminar_horario(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM horarios WHERE id = %s", (id,))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar horario: {e}")
        conn.rollback()

    cursor.close()
    conn.close()
    return redirect('/listar_horarios')
