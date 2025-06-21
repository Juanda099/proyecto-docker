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
            docker compose down --remove-orphans || true
            docker compose build --no-cache web
            docker compose up -d db
            mkdir -p "${WORKSPACE}/${COVERAGE_DIR}"

            # Ejecutar pytest y generar cobertura
            docker compose run --rm \
                -v "${WORKSPACE}/${COVERAGE_DIR}:/app/${COVERAGE_DIR}" \
                --entrypoint="" web sh -c "
                    mkdir -p /app/${COVERAGE_DIR} && \
                    pytest --cov=main --cov-report=html:/tmp/htmlcov tests && \
                    echo 'Contenido real en /tmp/htmlcov antes de copiar:' && \
                    ls -l /tmp/htmlcov && \
                    cp -r /tmp/htmlcov/. /app/${COVERAGE_DIR}/
                "

            echo "=== Contenido de ${WORKSPACE}/${COVERAGE_DIR} tras pytest ==="
            ls -la "${WORKSPACE}/${COVERAGE_DIR}" || true
            ls -R "${WORKSPACE}/${COVERAGE_DIR}" || true

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
