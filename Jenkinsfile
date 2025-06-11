pipeline {
    agent any

    // ✅ Eliminamos skipDefaultCheckout para permitir el checkout completo
    // options {
    //     skipDefaultCheckout(true)
    // }

    stages {
        stage('Checkout') {
            steps {
                // ✅ Forzamos a Jenkins a hacer checkout del repositorio completo
                checkout scm
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
