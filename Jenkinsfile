pipeline {
    agent any

    environment {
        COVERAGE_DIR = 'htmlcov'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Simulación del proceso de construcción"
            }
        }
        stage('Run Tests with Coverage') {
            steps {
                sh '''
                    # Bajar contenedores previos si existieran
                    docker compose down --remove-orphans || true

                    # Forzar reconstrucción de la imagen web
                    docker compose build --no-cache web

                    # Levantar sólo la base de datos
                    docker compose up -d db

                    # Crear carpeta en workspace para montar htmlcov
                    mkdir -p htmlcov

                    # Ejecutar pytest dentro del contenedor, montando htmlcov en host
                    # IMPORTANTE: usar --entrypoint="" para que Docker ejecute directamente 'pytest'
                    docker compose run --rm -v "$PWD/htmlcov:/app/htmlcov" --entrypoint="" web pytest --cov=main --cov-report=html tests

                    # Diagnóstico: listar contenido de htmlcov en host
                    echo "=== Contenido de htmlcov tras pytest ==="
                    ls -la htmlcov || true
                    ls -R htmlcov || true

                    # Ajustar permisos para que Jenkins pueda leer/copiar los archivos
                    chmod -R a+rX htmlcov
                '''
            }
        }
        stage('Archive Coverage Report') {
            steps {
                // Verificamos nuevamente antes de archivar
                sh '''
                    echo "=== Verificando htmlcov justo antes de archiveArtifacts ==="
                    ls -la htmlcov || true
                    ls -R htmlcov || true
                '''
                // Archivar los archivos HTML de cobertura
                archiveArtifacts artifacts: "${COVERAGE_DIR}/**", allowEmptyArchive: false
                echo "Reporte de cobertura archivado en ${WORKSPACE}/${COVERAGE_DIR}/"
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Simulación del despliegue (solo en rama main)"
            }
        }
        stage('Verificación') {
            steps {
                echo "Simulación de verificación del entorno"
            }
        }
    }

    post {
        always {
            // Bajar contenedores al finalizar
            sh 'docker compose down --remove-orphans || true'
            echo '✅ Pipeline completado'
        }
        failure {
            echo '❌ Pipeline falló'
        }
    }
}
