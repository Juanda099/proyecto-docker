pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Build') {
            steps {
                echo "🚧 Simulación del proceso de construcción"
            }
        }
        stage('Test') {
            steps {
                echo "🧪 Simulación de pruebas ejecutándose correctamente"
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "🚀 Simulación del despliegue (solo en rama main)"
            }
        }
        stage('Verificación') {
            steps {
                echo "🔍 Simulación de verificación del entorno"
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
