pipeline {
    agent any

    // ❌ NO usamos skipDefaultCheckout aquí
    // options {
    //     skipDefaultCheckout(true)
    // }

    stages {
        stage('Checkout') {
            steps {
                echo "✅ Código ya fue descargado automáticamente por Jenkins"
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
                echo "🧪 Aquí podrías ejecutar tests de tu app si existen."
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
                echo "🔍 Verificando instalación de Docker"
                sh 'which docker'
                sh 'docker --version'
                sh 'docker compose version || docker-compose --version'
                echo "✅ Verificación de entorno Docker completa"
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
