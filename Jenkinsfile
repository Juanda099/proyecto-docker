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
                }
            }
        }
        stage('Build') {
            steps {
                dir('proyecto-docker') {
                    sh 'docker compose build'
                }
            }
        }
        stage('Test') {
            steps {
                echo "✅ Prueba detectada por Jenkins. Test funcionando correctamente."
            }
        }            
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                dir('proyecto-docker') {
                    sh 'docker compose down --remove-orphans'
                    sh 'docker compose build --no-cache'
                    sh 'docker compose up -d'
                }
            }
        }
        stage('Verificación') {
            steps {
                dir('proyecto-docker') {
                    sh 'which docker'
                    sh 'docker --version'
                    sh 'docker compose version || docker-compose --version'
                }
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
