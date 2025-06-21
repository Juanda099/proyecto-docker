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
                    # Bajar contenedores previos
                    docker compose down --remove-orphans || true

                    # Forzar reconstrucción de la imagen web
                    docker compose build --no-cache web

                    # Levantar solo la base de datos
                    docker compose up -d db

                    # Crear carpeta en workspace para montar el htmlcov
                    mkdir -p htmlcov

                    # Ejecutar pytest dentro del contenedor, montando htmlcov en host
                    docker compose run --rm -v $PWD/htmlcov:/app/htmlcov --entrypoint='' web pytest --cov=main --cov-report=html tests

                    # Ajustar permisos para que Jenkins pueda leer/copiar los archivos
                    chmod -R a+rX htmlcov
                '''
            }
        }
        stage('Publish Coverage Report') {
            steps {
                // Asegúrate de que HTML Publisher Plugin esté instalado en Jenkins
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${COVERAGE_DIR}",
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
                // Si no tuvieras el plugin HTML Publisher, puedes en su lugar archivar:
                // archiveArtifacts artifacts: "${COVERAGE_DIR}/**", allowEmptyArchive: false
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
