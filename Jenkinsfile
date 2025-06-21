pipeline {
    agent any

    options {
        // Evita el checkout automático que está causando el error
        skipDefaultCheckout(true)
    }

    environment {
        COVERAGE_DIR = 'htmlcov'
    }

    stages {
        stage('Build') {
            steps {
                echo "Simulación del proceso de construcción"
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                sh '''
                    docker compose down --remove-orphans || true
                    docker compose up -d db
                    docker compose run --rm web pytest --cov=main --cov-report=html tests
                '''
            }
        }

        stage('Publish Coverage Report') {
            steps {
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
            echo '✅ Pipeline completado'
        }
        failure {
            echo '❌ Pipeline falló'
        }
    }
}
