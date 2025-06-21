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
                sh """
                    # Bajar contenedores previos si existieran
                    docker compose down --remove-orphans || true

                    # Reconstruir la imagen web desde cero
                    docker compose build --no-cache web

                    # Levantar solo la base de datos
                    docker compose up -d db

                    # Crear carpeta htmlcov en el workspace
                    mkdir -p "${WORKSPACE}/${COVERAGE_DIR}"

                    # Ejecutar pytest con salida HTML explícita a /app/htmlcov
                    docker compose run --rm \
                        -v "${WORKSPACE}/${COVERAGE_DIR}:/app/${COVERAGE_DIR}" \
                        --entrypoint="" web \
                        pytest --cov=main --cov-report=html:/app/${COVERAGE_DIR} tests

                    # Diagnóstico: listar contenido generado
                    echo "=== Contenido de ${WORKSPACE}/${COVERAGE_DIR} tras pytest ==="
                    ls -la "${WORKSPACE}/${COVERAGE_DIR}" || true
                    ls -R "${WORKSPACE}/${COVERAGE_DIR}" || true

                    # Ajustar permisos para Jenkins
                    chmod -R a+rX "${WORKSPACE}/${COVERAGE_DIR}"
                """
            }
        }
        stage('Archive Coverage Report') {
            steps {
                sh """
                    echo "=== Verificando htmlcov justo antes de archiveArtifacts ==="
                    ls -la "${WORKSPACE}/${COVERAGE_DIR}" || true
                    ls -R "${WORKSPACE}/${COVERAGE_DIR}" || true
                """
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
            sh 'docker compose down --remove-orphans || true'
            echo '✅ Pipeline completado'
        }
        failure {
            echo '❌ Pipeline falló'
        }
    }
}
