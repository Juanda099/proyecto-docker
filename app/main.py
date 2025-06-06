from flask import Flask, render_template
from routes import horarios, materias, registro

def create_app():
    app = Flask(__name__)
    
    # Configurar la clave secreta para sesiones y flash
    app.secret_key = '9d8f3a4c-7b6e-4f2a-91d3-8e5c1b7a2f9e'

    # Registrar blueprints
    app.register_blueprint(registro.registro_bp)
    app.register_blueprint(materias.materias_bp)
    app.register_blueprint(horarios.horarios_bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
