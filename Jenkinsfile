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
                    docker compose down --remove-orphans || true
                    docker compose build --no-cache web
                    docker compose up -d db
                    mkdir -p htmlcov
                    docker compose run --rm -v $PWD/htmlcov:/app/htmlcov --entrypoint='' web pytest --cov=main --cov-report=html tests
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
