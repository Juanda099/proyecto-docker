pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    //environment {
        // DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') // Si vas a usar Docker Hub después
    //}

    stages {
        stage('Checkout') {
            steps {
                echo "✅ Código ya fue descargado automáticamente por Jenkins"
            }
        }

        stage('Build') {
            steps {
                echo "🚧 Ejecutando docker compose build..."
                sh 'docker compose build'
            }
        }

        stage('Test') {
            steps {
                echo "🧪 Aquí podrías ejecutar tests de tu app si existen."
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "🚀 Levantando servicios con docker compose up -d"
                sh 'docker compose up -d'
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
