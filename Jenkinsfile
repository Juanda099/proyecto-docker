pipeline {
    agent any

    // ❌ Quitar skipDefaultCheckout
    // options {
    //     skipDefaultCheckout(true)
    // }

    stages {
        stage('Checkout') {
            steps {
                echo "✅ Jenkins ya hizo checkout automáticamente"
            }
        }

        stage('Build') {
            steps {
                echo "🚧 Ejecutando docker compose build..."
                sh 'docker compose -f docker-compose.app.yml build'
            }
        }

        stage('Test') {
            steps {
                echo "🧪 Ejecutando tests (si hay)..."
            }
        }

        stage('Deploy') {
            steps {
                echo "🛑 Deteniendo servicios antiguos"
                sh 'docker compose -f docker-compose.app.yml down --remove-orphans'

                echo "🚀 Levantando servicios actualizados"
                sh 'docker compose -f docker-compose.app.yml up -d'
            }
        }

        stage('Verificación') {
            steps {
                echo "🔍 Verificando Docker..."
                sh 'which docker'
                sh 'docker --version'
                sh 'docker compose version || docker-compose --version'
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

