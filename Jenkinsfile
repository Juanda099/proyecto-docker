pipeline {
    agent any

    options {
        // Evita el checkout automático que está causando el error
        skipDefaultCheckout(true)
    }

   // environment {
   //     DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
   // }

    stages {

        stage('checkout'){
            steps {
                // Simulación de un checkout manual
                echo "Simulación del checkout del repositorio"
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Simulación del proceso de construcción"
                sh 'docker compose build'
            }
        }
        stage('Test') {
            steps {
                echo "Simulación de pruebas ejecutándose correctamente"
            }
        }
        stage('Deploy') {
            when {
                branch 'main' 
            }
            steps {
                echo "Simulación del despliegue (solo en rama main)"
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
