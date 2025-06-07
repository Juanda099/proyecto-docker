pipeline {
    agent any
    //environment {
    //    DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    //}
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Juanda099/proyecto-docker.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('Test') {
            steps {
                // Aquí irían los tests
                echo "Ejecutando pruebas..."
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker compose down --remove-orphans' // 🔥 Detiene y elimina contenedores viejos
                sh 'docker compose build --no-cache'      // 🔁 Fuerza rebuild de las imágenes
                sh 'docker compose up -d'                 // 🚀 Vuelve a levantar los servicios
            }
        }
        stage('Verificación') {
            steps {
                sh 'which docker'
                sh 'docker --version'
                sh 'docker compose version || docker-compose --version'
            }
        }

    }
    post {
        always {
            echo 'Pipeline completado'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
}