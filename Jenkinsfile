pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }
    stages {
        stage('Checkout') {
            steps {
                dir('proyecto-docker') {
                    git branch: 'main', url: 'https://github.com/Juanda099/proyecto-docker'
                    echo "✅ Checkout manual exitoso en subcarpeta"
                }
            }
        }
        stage('Build') {
            steps {
                echo "🚧 Etapa de construcción simulada"
            }
        }
        stage('Test') {
            steps {
                echo "🧪 Etapa de pruebas simulada"
            }
        }            
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "🚀 Etapa de despliegue simulada"
            }
        }
        stage('Verificación') {
            steps {
                echo "🔍 Verificación simulada: Docker está funcionando correctamente (simulado)"
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
