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
                // Usamos comillas dobles para el bloque sh y escapamos $PWD si fuera necesario
                sh """
                    # Bajar contenedores previos
                    docker compose down --remove-orphans || true

                    # Forzar reconstrucción de la imagen web
                    docker compose build --no-cache web

                    # Levantar solo la base de datos
                    docker compose up -d db

                    # Crear carpeta en workspace para montar htmlcov
                    mkdir -p htmlcov

                    # Ejecutar pytest dentro del contenedor, montando htmlcov en host
                    # NOTA: Es crucial que --entrypoint='' se pase literalmente al shell.
                    docker compose run --rm -v "\$PWD/htmlcov:/app/htmlcov" --entrypoint='' web pytest --cov=main --cov-report=html tests

                    # Ajustar permisos en workspace/htmlcov para garantizar lectura
                    chmod -R a+rX htmlcov
                """
            }
        }
        stage('Archive Coverage Report') {
            steps {
                // Archivamos los archivos HTML de cobertura para descarga desde Jenkins
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
