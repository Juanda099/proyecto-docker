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

                    # Levantar sólo la base de datos
                    docker compose up -d db

                    # Crear carpeta htmlcov en el workspace
                    mkdir -p "${WORKSPACE}/${COVERAGE_DIR}"

                    # Ejecutar pytest dentro del contenedor, montando la carpeta del host:
                    # Usamos --entrypoint="" para ejecutar directamente 'pytest'.
                    docker compose run --rm \
                        -v "${WORKSPACE}/${COVERAGE_DIR}:/app/${COVERAGE_DIR}" \
                        --entrypoint="" web \
                        pytest --cov=main --cov-report=html tests

                    # Diagnóstico: listar contenido en el host
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
                // Antes de archivar, revisamos de nuevo
                sh """
                    echo "=== Verificando htmlcov justo antes de archiveArtifacts ==="
                    ls -la "${WORKSPACE}/${COVERAGE_DIR}" || true
                    ls -R "${WORKSPACE}/${COVERAGE_DIR}" || true
                """
                // Archivar los HTML de cobertura
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
            // Bajar contenedores
            sh 'docker compose down --remove-orphans || true'
            echo '✅ Pipeline completado'
        }
        failure {
            echo '❌ Pipeline falló'
        }
    }
}
